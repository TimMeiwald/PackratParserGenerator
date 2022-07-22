import enum
from collections import deque
from functools import lru_cache as cache

class Rules(enum.Enum):
    _TERMINAL = 1
    _SEQUENCE = 2
    _ORDERED_CHOICE = 3
    _NOT_PREDICATE = 4
    _AND_PREDICATE = 5
    _OPTIONAL = 6
    _ZERO_OR_MORE = 7
    _ONE_OR_MORE = 8
    _SUBEXPRESSION = 10
    _VAR = 11


class Node():
    """Core data type"""
    def __init__(self, type: Rules | int, content: str = ""):
        self.parent = None
        self.type = type
        self.content = content
        self.children = deque()

class Parser():

    def __init__(self):
        """
        TODO: Remember to clear all caches between parses
        TODO: remember to deep copy on data extraction as AST because many nodes will be shared due to cache
        This could cause issues when manipulating the AST"""
        self.src = ""
        self._rules_count = 20 # So it doesn't clash with enum, 20 so I have space for other stuff
        self._rules_dict = {}
        self._rules_dict_inverse = {}
    
    def _set_src(self, src: str):
        self.src = src
        # Ensures all caches are cleared on resetting the src
        # Resets state completely 
        native_rules = [
            Parser._token, 
            Parser._TERMINAL,
            Parser._VAR_NAME,
            Parser._ORDERED_CHOICE,
            Parser._SEQUENCE,
            Parser._ZERO_OR_MORE,
            Parser._ONE_OR_MORE, 
            Parser._AND_PREDICATE,
            Parser._NOT_PREDICATE,
            Parser._NOT_PREDICATE,
            Parser._SUBEXPR,
            Parser._test,
        ]
        cache_info = []
        for rule in native_rules:
            cache_info.append(rule.cache_info())
            rule.cache_clear()
        for rule in self._rules_dict_inverse:
            key, func = self._rules_dict_inverse[rule]
            cache_info.append(func.cache_info())
            print(key, func)
            func.cache_clear()
        self._rules_count = 20
        self._rules_dict = {}
        self._rules_dict_inverse = {}
        return cache_info

    def pretty_print(self, node, indent = 0):
        indent_str = "  "
        if(node != None):
            if(type(node.type) == int):
                if(node.type < 20):
                    print(indent_str*indent + f"Node: {self.__rules_dict_inverse[node.type]}, {node.content}, {node.parent}")
                else:
                    print(indent_str*indent + f"Node: {self.__rules_dict_inverse[node.type]}, {node.content}, {node.parent}")
            else:
                print(indent_str*indent + f"Node: {node.type}, {node.content}, {node.parent}")
            for child in node.children:
                self.pretty_print(child, indent+1)

    @cache
    def _token(self, position):
        if(position >= len(self.src)):
            return False 
        return self.src[position]

    @cache
    def _TERMINAL(self, position: int, Arg: str):
        assert type(position) == int
        assert type(Arg) == str
        token = self._token(position)
        if(token == Arg):
            position += 1
            node = Node(Rules._TERMINAL, token)
            return position, True, node
        else:
            return position, False, None

    @cache
    def _VAR_NAME(self, position: int, args):
        """True if called function evaluates to true else false, Is used to call other functions."""
        #where func is a grammar rule
        temp_position = position
        func, args = args
        position, bool, node = func(position, args)
        if(bool == True):
            key = func.__name__
            if(key not in self._rules_dict):
                self._rules_dict[key] = self._rules_count
                self._rules_dict_inverse[self._rules_count] = (key, func)
                self._rules_count += 1
                #print(f"\nAdded Rule: {key} with int: {self._rules_count-1}")
            var_node = Node(Rules._VAR, key)
            if(node != None):
                var_node.children.append(node)
                node.parent = var_node
            return position, True, var_node
        else:
            position = temp_position
            return position, False, None

    @cache
    def _ORDERED_CHOICE(self, position: int, args):
        """True if one expression matches, then updates position, else false, no positional update"""
        LHS_func, LHS_arg = args[0]
        RHS_func, RHS_arg = args[1]
        temp_position = position
        position, bool, node = LHS_func(position, LHS_arg)
        if(bool == True):
            ordered_choice_node = Node(Rules._ORDERED_CHOICE)
            ordered_choice_node.children.append(node)
            node.parent = ordered_choice_node
            return position, True, ordered_choice_node
        position = temp_position
        position, bool, node = RHS_func(position, RHS_arg)
        if(bool == True):
            ordered_choice_node = Node(Rules._ORDERED_CHOICE)
            ordered_choice_node.children.append(node)
            node.parent = ordered_choice_node
            return position, True, ordered_choice_node
        position = temp_position
        return position, False, None    

    @cache
    def _SEQUENCE(self, position: int, args):
        """True if all expressions match, then updates position, else false, no positional update"""
        temp_position = position
        LHS_func, LHS_arg = args[0]
        RHS_func, RHS_arg = args[1]
        position, bool, lnode = LHS_func(position, LHS_arg)
        if(bool == True):
            position, bool, rnode = RHS_func(position, RHS_arg)
            if(bool == True):
                node = Node(Rules._SEQUENCE)
                if(lnode != None):
                    node.children.append(lnode)
                    lnode.parent = node
                if(rnode != None):
                    node.children.append(rnode)
                    rnode.parent = node
                return position, True, node
            else:
                position = temp_position
                return position, False, None
        else:
            position = temp_position
            return position, False, None

    @cache
    def _ZERO_OR_MORE(self, position: int, args):
        """Always True, increments position each time the expression matches else continues without doing anything"""
        func, arg = args
        zero_node = Node(Rules._ZERO_OR_MORE)
        while(True):
            temp_position = position
            position, bool, term_node = func(temp_position, arg)
            if(bool == True):
                term_node.parent = zero_node
                zero_node.children.append(term_node)
                continue
            else:
                position = temp_position
                break
        if(len(zero_node.children) == 0):
            return position, True, None
        else:
            return position, True, zero_node

    @cache
    def _ONE_OR_MORE(self, position: int, args):
        """True if there is at least one of the expression, increments position each time the expression matches else false"""
        func, arg = args
        temp_position = position
        position, bool, opt_node = self._OPTIONAL(position, args)
        if(position != temp_position): #Should have incremented by one expression if optional was successful
            position, bool, zero_node = self._ZERO_OR_MORE(position, args)
            if(bool == True):
                node = Node(Rules._ONE_OR_MORE)
                node.children.append(opt_node.children[0])
                opt_node.children[0].parent = node
                if(zero_node != None):
                    for child in zero_node.children:
                        node.children.append(child) #Don't actually want to append zero or more or optinal as such
                        child.parent = node
                return position, True, node
            else:
                # Should never happen?
                position = temp_position
                return position, False, None
        else:
            position = temp_position
            return position, False, None

    @cache
    def _OPTIONAL(self, position: int, args):
        """Always True, increments position if option matches otherwise continues without doing anything"""
        func, arg = args
        temp_position = position
        position, bool, term_node = func(temp_position, arg)
        if(bool == True):
            node = Node(Rules._OPTIONAL)
            node.children.append(term_node)
            term_node.parent = node
            return position, True, node
        else:
            position = temp_position
            return position, True, None

    @cache
    def _AND_PREDICATE(self, position: int, args):
        """True if the function results in True, never increments position"""
        func, arg = args
        temp_position = position
        position, bool, node = func(position, arg)
        if(bool == True):
            position = temp_position
            return position, True, None
        else:
            position = temp_position
            return position, False, None

    @cache
    def _NOT_PREDICATE(self, position: int, args):
        """True if the function results in False, never increments position"""
        position, bool, node = self._AND_PREDICATE(position, args)
        return position, not bool, None

    @cache
    def _SUBEXPR(self, position: int, args):
        """Subexpression is any expression inside a pair of () brackets
        SUBEXPR essentially does nothing but allows for order of precedent 
        more importantly order of precedence is very restricted because it made my life hard
        (mostly because I can't find a good definition of what order of precedence is in PEG) so use SUBEXPR
        to make more complicated rules"""
        func, arg = args
        temp_position = position
        position, bool, node = func(position, arg)
        if(bool == True):
            subexpr_node = Node(Rules._SUBEXPRESSION)
            subexpr_node.children.append(node)
            node.parent = subexpr_node
            return position, True, subexpr_node
        else:
            position = temp_position
            return position, False, None

    @cache 
    def _test(self, position: int, args):
        """For testing purposes, may be able to refactor somehow to test
        but not sure how"""
        return self._TERMINAL(position, args)