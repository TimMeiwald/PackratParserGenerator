from enum import Enum
from collections import deque
from functools import lru_cache as cache
from packratparsergenerator.parser.rules import Rules

    

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

    def pretty_print(self):
        self._pretty_print(self)

    def _pretty_print(self, node, indent = 0):
        indent_str = "  "
        if(node != None):
            print(indent_str*indent + f"Node: {node.type.name}, '{node.content}'")
            for child in node.children:
                self._pretty_print(child, indent+1)


class Parser():

    def __init__(self):
        self.src = ""
    
    def _set_src(self, src: str):
        self.src = src
        # Ensures all caches are cleared on resetting the src
        # Resets state completely 
        for rule in Rules:
            if(rule > 0 and rule < 20): #Less than 20 is core parser stuff, greater than 20 is inherited class stuff
                func = getattr(self, rule.name)
                func.cache_clear()


    def caller(self, position, func, arg = None):
        """Calls generated functions, ensures converted to node not nested deques, 
        Useful for testing or calling specific subterminals"""
        return self._VAR_NAME(position, (func, arg))[2]
    
    
    @cache
    def _token(self, position):
        if(position >= len(self.src)):
            return False 
        return self.src[position]

    @cache
    def _TERMINAL(self, position: int, arg: str):
        #assert type(position) == int
        #assert type(Arg) == str
        token = self._token(position)
        if(token == arg):
            position += 1
            if(token == "\\"):
                token = self._token(position)
                if(token == "n"):
                    position += 1
                    token = "\\n"
                elif(token == "r"):
                    position += 1
                    token = "\\r"
                elif(token == "t"):
                    position += 1
                    token = "\\t"
                else:
                    token = "\\"
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
            var_node = Node(Rules[key], None)
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
    def _SUBEXPRESSION(self, position: int, args):
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