# Must remain at top so it can be easily replaced
from packratparsergenerator.parser.rules import Rules
from packratparsergenerator.parser.parser_pass_two import Parser_Pass_Two
from collections import deque
from functools import lru_cache as cache


class Node():
    """Core data type"""

    def __init__(self, type: int, content: str = ""):
        """Constructor

        Args:
            type (int): int that corresponds to Rules IntEnum telling you what type of Node it is.
            content (str, optional): Content of Node. Defaults to "".
        """
        self.type = type
        self.content = content
        self.children = deque()
        self.parent = None

    def appender(self, node_deque):
        if (isinstance(node_deque, tuple)):
            print("Tuple apparently: ", node_deque)
            raise Exception
        if (node_deque is None):
            return None
        elif (not isinstance(node_deque, deque)):
            self.children.append(node_deque)
        else:
            for child in node_deque:
                self.appender(child)

    def __equals(self, __o: object) -> bool:
        if (__o is None):
            return False
        if (self.content == __o.content and self.type.name == __o.type.name):
            # By name of type as opposed to value because the value can change between
            # parser versions as the enum is autogenerated
            return True
        else:
            return False

    def __eq__(self, __o: object) -> bool:
        """Two Nodes are considered equal if they and all their subchildren have identical types and contents in order"""
        return self.__subtree_equals(__o)

    def __subtree_equals(self, __o: object) -> bool:
        if (self.__equals(__o) is False):
            return False
        else:
            count = 0
            for index, child in enumerate(self.children):
                try:
                    bool = child.__subtree_equals(__o.children[index])
                    count += bool
                except IndexError:
                    return False
            if (count != len(self.children)):
                return False
            else:
                return True

    def pretty_print(self):
        self._pretty_print(self)

    def _pretty_print(self, node, indent=0):
        indent_str = "  "
        if (node is not None):
            print(indent_str * indent +
                  f"Node: {node.type.name}, '{node.content}'")
            for child in node.children:
                self._pretty_print(child, indent + 1)


class Parser():

    def __init__(self):
        self.src = ""

    def _set_src(self, src: str):
        self.src = src
        # Ensures all caches are cleared on resetting the src
        # Resets state completely
        for rule in Rules:
            # Less than 20 is core parser stuff, greater than 20 is inherited
            # class stuff
            if (rule > 0 and rule < 20):
                func = getattr(self, rule.name)
                func.cache_clear()

    def caller(self, position, func, arg=None):
        """Calls generated functions, ensures converted to node not nested deques,
        Useful for testing or calling specific subterminals"""
        return self._VAR_NAME(position, (func, arg))

    def parse(self, src, func, *, arg=None):
        """Pass in the src and the function from the Grammar_Parser class you defined in the Grammar file
        and it will parse it and return the position at which halting stopped, whether the parse succeeded
        and the AST."""
        self._set_src(src)
        position, bool, node = self._VAR_NAME(0, (func, arg))
        if(node is not None):
            pass_two = Parser_Pass_Two()
            pass_two.parse(node)
            return position, bool, node
        else:
            return position, bool, None

    @cache
    def _token(self, position):
        if (position >= len(self.src)):
            return False
        return self.src[position]

    @cache
    def _TERMINAL(self, position: int, arg: str):
        #assert type(position) == int
        #assert type(Arg) == str
        if(arg == ""):
            return position, True, None
        token = self._token(position)
        if (token == arg):
            position += 1
            if (token == "\\"):
                token = self._token(position)
                if (token == "n"):
                    position += 1
                    token = "\\n"
                elif (token == "r"):
                    position += 1
                    token = "\\r"
                elif (token == "t"):
                    position += 1
                    token = "\\t"
                else:
                    token = "\\"
            node = Node(Rules._TERMINAL, token)
            return position, True, node
        else:
            # Don't generate anything other than terminal and var on run, means
            # no rationalizer
            return position, False, None

    @cache
    def _VAR_NAME(self, position: int, args):
        """True if called function evaluates to true else false, Is used to call other functions."""
        # where func is a grammar rule
        temp_position = position
        func, args = args
        position, bool, node = func(position, args)
        if (bool):
            key = func.__name__
            var_node = Node(Rules[key], None)
            if (node is not None):
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
        if (bool):
            return position, True, node
        position = temp_position
        position, bool, node = RHS_func(position, RHS_arg)
        if (bool):
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
        if (bool):
            position, bool, rnode = RHS_func(position, RHS_arg)
            if (bool):
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
        while (True):
            temp_position = position
            position, bool, term_node = func(temp_position, arg)
            if (bool):
                zero_nodes.append(term_node)
                continue
            else:
                position = temp_position
                break
        if (len(zero_nodes) == 0):
            return position, True, None
        else:
            return position, True, zero_nodes

    @cache
    def _ONE_OR_MORE(self, position: int, args):
        """Always True, increments position each time the expression matches else continues without doing anything"""
        func, arg = args
        one_nodes = deque()
        while (True):
            temp_position = position
            position, bool, term_node = func(temp_position, arg)
            if (bool):
                one_nodes.append(term_node)
                continue
            else:
                position = temp_position
                break
        if (len(one_nodes) == 0):
            return position, False, None
        else:
            return position, True, one_nodes

    @cache
    def _OPTIONAL(self, position: int, args):
        """Always True, increments position if option matches otherwise continues without doing anything"""
        func, arg = args
        temp_position = position
        position, bool, node = func(temp_position, arg)
        if (bool):
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
        if (bool):
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
        if (bool):
            return position, True, node
        else:
            position = temp_position
            return position, False, None

    @cache
    def _test(self, position: int, args):
        """For testing purposes, may be able to refactor somehow to test
        but not sure how"""
        return self._TERMINAL(position, args)
