from enum import Enum
from collections import deque
from functools import lru_cache as cache

class Rules(Enum):
    _ROOT = 0
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
        self.type = type
        self.content = content
        self.children = deque()
        self.parent = None

    #Appends nested deque if needed
    def appender(self, node_deque):
        if(type(node_deque) == tuple):
            print("Tuple apparently: ",node_deque)
            raise Exception
        if(node_deque == None):
            return None
        elif(type(node_deque) != deque):
            self.children.append(node_deque)
        else:
            for child in node_deque:
                self.appender(child)


class Parser():

    def __init__(self):
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
                    print(indent_str*indent + f"Node: {self._rules_dict_inverse[node.type]}, {node.content}")
                else:
                    print(indent_str*indent + f"Node: {self._rules_dict_inverse[node.type]}, {node.content}")
            else:
                print(indent_str*indent + f"Node: {node.type}, {node.content}")
            for child in node.children:
                self.pretty_print(child, indent+1)

    @cache
    def _token(self, position):
        if(position >= len(self.src)):
            return False 
        return self.src[position]

    @cache
    def _TERMINAL(self, position: int, Arg: str):
        #assert type(position) == int
        #assert type(Arg) == str
        token = self._token(position)
        if(token == Arg):
            position += 1
            node = Node(Rules._TERMINAL, token)
            return position, True, node
        else:
            return position, False, None # Don't generate anything other than terminal and var on run, means no rationalizer

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
                var_node.appender(node)
                return position, True, var_node
            else:
                return position, True, None
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
            return position, True, node
        position = temp_position
        position, bool, node = RHS_func(position, RHS_arg)
        if(bool == True):
            return position, True, node
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
                node = deque()
                node.append(lnode)
                node.append(rnode)
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
        zero_nodes = deque()
        while(True):
            temp_position = position
            position, bool, term_node = func(temp_position, arg)
            if(bool == True):
                zero_nodes.append(term_node)
                continue
            else:
                position = temp_position
                break
        if(len(zero_nodes) == 0):
            return position, True, None
        else:
            return position, True, zero_nodes

    @cache
    def _ONE_OR_MORE(self, position: int, args):
        """Always True, increments position each time the expression matches else continues without doing anything"""
        func, arg = args
        one_nodes = deque()
        while(True):
            temp_position = position
            position, bool, term_node = func(temp_position, arg)
            if(bool == True):
                one_nodes.append(term_node)
                continue
            else:
                position = temp_position
                break
        if(len(one_nodes) == 0):
            return position, False, None
        else:
            return position, True, one_nodes

    @cache
    def _OPTIONAL(self, position: int, args):
        """Always True, increments position if option matches otherwise continues without doing anything"""
        func, arg = args
        temp_position = position
        position, bool, node = func(temp_position, arg)
        if(bool == True):
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
            return position, True, node
        else:
            position = temp_position
            return position, False, None

    @cache 
    def _test(self, position: int, args):
        """For testing purposes, may be able to refactor somehow to test
        but not sure how"""
        return self._TERMINAL(position, args)
