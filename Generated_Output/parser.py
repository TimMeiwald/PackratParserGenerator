from collections import deque
from functools import lru_cache as cache
from enum import IntEnum

class Rules(IntEnum):
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
    _VAR_NAME = 11
    _test = 12
    # Following enum values are all autogenerated from grammar file
    Alphabet_Upper = 20
    Alphabet_Lower = 21
    Num = 22
    Specials = 23
    Spaces = 24
    ASCII = 25
    Apostrophe = 26
    Left_Angle_Bracket = 27
    Right_Angle_Bracket = 28
    Left_Bracket = 29
    Right_Bracket = 30
    Assignment = 31
    End_Rule = 32
    Ampersand = 33
    Exclamation_Mark = 34
    Plus = 35
    Star = 36
    Question_Mark = 37
    Comma = 38
    Backslash = 39
    Var_Name = 40
    Subexpression = 41
    Terminal = 42
    Nucleus = 43
    Atom = 44
    And_Predicate = 45
    Not_Predicate = 46
    Sequence = 47
    Ordered_Choice = 48
    One_Or_More = 49
    Zero_Or_More = 50
    Optional = 51
    Whitespace = 52
    RHS = 53
    LHS = 54
    Rule = 55
    Grammar = 56

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
    
    def __equals(self, __o: object) -> bool:
        if(__o is None):
            return False
        if(self.content == __o.content and self.type.name == __o.type.name):
            # By name of type as opposed to value because the value can change between
            # parser versions as the enum is autogenerated
            return True
        else:
            return False
    
    def __eq__(self, __o: object) -> bool:
        return self.__subtree_equals(__o)
    
    def __subtree_equals(self, __o: object) -> bool:
        if(self.__equals(__o) is False):
            return False
        else:
            count = 0
            for index, child in enumerate(self.children):
                try:
                    bool = child.__subtree_equals(__o.children[index])
                    count += bool
                except IndexError:
                    return False
            if(count != len(self.children)):
                return False
            else:
                return True

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
    
    def parse(self, src, func, *, arg = None):
        """Pass in the src and the function from the Grammar_Parser class you defined in the Grammar file
        and it will parse it and return the position at which halting stopped, whether the parse succeeded
        and the AST."""
        self._set_src(src)
        position, bool, node = self._VAR_NAME(0, (func, arg))
        pass_two = Parser_Pass_Two()
        pass_two.parse(node)
        return position, bool, node
    
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




class Parser_Pass_Two():

    def __init__(self):
        self.delete_nodes = (Rules.Whitespace, Rules.Apostrophe, Rules.Left_Angle_Bracket, Rules.Right_Angle_Bracket, Rules.Left_Bracket, 
        Rules.Right_Bracket, Rules.Plus, Rules.Star, Rules.Question_Mark, Rules.Backslash, Rules.Comma, Rules.End_Rule, Rules.Assignment,Rules.Exclamation_Mark, Rules.Ampersand)
        self.passthrough_nodes = (Rules.ASCII, Rules.Alphabet_Upper, Rules.Alphabet_Lower, Rules.Atom, Rules.Nucleus, Rules.RHS, Rules.Specials, Rules.Num, Rules.Spaces)
        self.collect_nodes = (Rules.Var_Name,)
        self.tokens = deque()
      
    def token_generator(self, node):
        self.tokens.append(node)
        for child in node.children:
            child.parent = node
            self.token_generator(child)

    def delete_kernel(self, node):
        if(node.type in self.delete_nodes):
            node.children = deque()
            node.parent.children.remove(node)
            del node
        else:
            return node

    def passthrough_kernel(self, node):
        if(node.type in self.passthrough_nodes):
            index = node.parent.children.index(node)
            for child in node.children:
                node.parent.children.insert(index, child)
            node.parent.children.remove(node)
            del node
        else:
            return node

    def collect_kernel(self, node):
        if(node.type in self.collect_nodes): 
            for child in node.children:
                if(child.type != Rules._TERMINAL):
                    raise ValueError(f"Cannot collect if there are non terminals in the nodes childrens. Node_Type: {node.type.name}, Child_Type: {child.type.name}")
            node.content = ""
            for child in node.children:
                node.content += child.content
            node.children = deque()
            return node
        else:
            return node

    def __parse(self, nodes):
        new_deq = deque()
        for index in range(0, len(nodes)):
            node = nodes.pop()
            node = self.delete_kernel(node)
            if(node != None):
                node = self.passthrough_kernel(node)
            if(node != None):
                node = self.collect_kernel(node)
            if(node != None):
                new_deq.append(node)
        return new_deq


    def parse(self, node):
        self.token_generator(node)
        nodes = deque(self.tokens)
        nodes = self.__parse(nodes)
        return nodes



class Grammar_Parser(Parser):

    def _set_src(self, src: str):
        super()._set_src(src)
        for rule in Rules:
            if(rule >= 20): #Less than 20 is core parser stuff, greatereq than 20 is inherited class stuff
                func = getattr(self, rule.name)
                func.cache_clear()
    @cache
    def Alphabet_Upper(self, position: int, dummy = None):
        """ <Alphabet_Upper> = "A"/"B"/"C"/"D"/"E"/"F"/"G"/"H"/"I"/"J"/"K"/"L"/"M"/"N"/"O"/"P"/"Q"/"R"/"S"/"T"/"U"/"V"/"W"/"X"/"Y"/"Z" ; """
        return self._SUBEXPRESSION(position, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "A"), (self._TERMINAL, "B"))), (self._TERMINAL, "C"))), (self._TERMINAL, "D"))), (self._TERMINAL, "E"))), (self._TERMINAL, "F"))), (self._TERMINAL, "G"))), (self._TERMINAL, "H"))), (self._TERMINAL, "I"))), (self._TERMINAL, "J"))), (self._TERMINAL, "K"))), (self._TERMINAL, "L"))), (self._TERMINAL, "M"))), (self._TERMINAL, "N"))), (self._TERMINAL, "O"))), (self._TERMINAL, "P"))), (self._TERMINAL, "Q"))), (self._TERMINAL, "R"))), (self._TERMINAL, "S"))), (self._TERMINAL, "T"))), (self._TERMINAL, "U"))), (self._TERMINAL, "V"))), (self._TERMINAL, "W"))), (self._TERMINAL, "X"))), (self._TERMINAL, "Y"))), (self._TERMINAL, "Z"))))
    @cache
    def Alphabet_Lower(self, position: int, dummy = None):
        """ <Alphabet_Lower> = "a"/"b"/"c"/"d"/"e"/"f"/"g"/"h"/"i"/"j"/"k"/"l"/"m"/"n"/"o"/"p"/"q"/"r"/"s"/"t"/"u"/"v"/"w"/"x"/"y"/"z" ; """
        return self._SUBEXPRESSION(position, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "a"), (self._TERMINAL, "b"))), (self._TERMINAL, "c"))), (self._TERMINAL, "d"))), (self._TERMINAL, "e"))), (self._TERMINAL, "f"))), (self._TERMINAL, "g"))), (self._TERMINAL, "h"))), (self._TERMINAL, "i"))), (self._TERMINAL, "j"))), (self._TERMINAL, "k"))), (self._TERMINAL, "l"))), (self._TERMINAL, "m"))), (self._TERMINAL, "n"))), (self._TERMINAL, "o"))), (self._TERMINAL, "p"))), (self._TERMINAL, "q"))), (self._TERMINAL, "r"))), (self._TERMINAL, "s"))), (self._TERMINAL, "t"))), (self._TERMINAL, "u"))), (self._TERMINAL, "v"))), (self._TERMINAL, "w"))), (self._TERMINAL, "x"))), (self._TERMINAL, "y"))), (self._TERMINAL, "z"))))
    @cache
    def Num(self, position: int, dummy = None):
        """ <Num> = "0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9" ; """
        return self._SUBEXPRESSION(position, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "0"), (self._TERMINAL, "1"))), (self._TERMINAL, "2"))), (self._TERMINAL, "3"))), (self._TERMINAL, "4"))), (self._TERMINAL, "5"))), (self._TERMINAL, "6"))), (self._TERMINAL, "7"))), (self._TERMINAL, "8"))), (self._TERMINAL, "9"))))
    @cache
    def Specials(self, position: int, dummy = None):
        """ <Specials> = "+"/"*"/"-"/"&"/"!"/"?"/"<"/">"/'"'/"("/")"/"_"/","/"/"/";"/"="/"\\"/"#"/":"/"|"/"."/"{"/"}"/"["/"]" ; """
        return self._SUBEXPRESSION(position, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "+"), (self._TERMINAL, "*"))), (self._TERMINAL, "-"))), (self._TERMINAL, "&"))), (self._TERMINAL, "!"))), (self._TERMINAL, "?"))), (self._TERMINAL, "<"))), (self._TERMINAL, ">"))), (self._TERMINAL, '"'))), (self._TERMINAL, "("))), (self._TERMINAL, ")"))), (self._TERMINAL, "_"))), (self._TERMINAL, ","))), (self._TERMINAL, "/"))), (self._TERMINAL, ";"))), (self._TERMINAL, "="))), (self._TERMINAL, '\\'))), (self._TERMINAL, "#"))), (self._TERMINAL, ":"))), (self._TERMINAL, "|"))), (self._TERMINAL, "."))), (self._TERMINAL, "{"))), (self._TERMINAL, "}"))), (self._TERMINAL, "["))), (self._TERMINAL, "]"))))
    @cache
    def Spaces(self, position: int, dummy = None):
        """ <Spaces> = "\n"/"\t"/"\r"/" " ; """
        return self._SUBEXPRESSION(position, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "\n"), (self._TERMINAL, "\t"))), (self._TERMINAL, "\r"))), (self._TERMINAL, " "))))
    @cache
    def ASCII(self, position: int, dummy = None):
        """ <ASCII> = <Alphabet_Lower>/<Alphabet_Upper>/<Num>/<Spaces>/<Specials> ; """
        return self._SUBEXPRESSION(position, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Alphabet_Lower, None)), (self._VAR_NAME, (self.Alphabet_Upper, None)))), (self._VAR_NAME, (self.Num, None)))), (self._VAR_NAME, (self.Spaces, None)))), (self._VAR_NAME, (self.Specials, None)))))
    @cache
    def Apostrophe(self, position: int, dummy = None):
        """ <Apostrophe> = '"' ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, '"'))
    @cache
    def Left_Angle_Bracket(self, position: int, dummy = None):
        """ <Left_Angle_Bracket> = "<" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "<"))
    @cache
    def Right_Angle_Bracket(self, position: int, dummy = None):
        """ <Right_Angle_Bracket> = ">" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, ">"))
    @cache
    def Left_Bracket(self, position: int, dummy = None):
        """ <Left_Bracket> = "(" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "("))
    @cache
    def Right_Bracket(self, position: int, dummy = None):
        """ <Right_Bracket> = ")" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, ")"))
    @cache
    def Assignment(self, position: int, dummy = None):
        """ <Assignment> = "=" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "="))
    @cache
    def End_Rule(self, position: int, dummy = None):
        """ <End_Rule> = ";" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, ";"))
    @cache
    def Ampersand(self, position: int, dummy = None):
        """ <Ampersand> = "&" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "&"))
    @cache
    def Exclamation_Mark(self, position: int, dummy = None):
        """ <Exclamation_Mark> = "!" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "!"))
    @cache
    def Plus(self, position: int, dummy = None):
        """ <Plus> = "+" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "+"))
    @cache
    def Star(self, position: int, dummy = None):
        """ <Star> = "*" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "*"))
    @cache
    def Question_Mark(self, position: int, dummy = None):
        """ <Question_Mark> = "?" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "?"))
    @cache
    def Comma(self, position: int, dummy = None):
        """ <Comma> = "," ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, ","))
    @cache
    def Backslash(self, position: int, dummy = None):
        """ <Backslash> = "/" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "/"))
    @cache
    def Var_Name(self, position: int, dummy = None):
        """ <Var_Name> = <Left_Angle_Bracket>, (<Alphabet_Lower>/<Alphabet_Upper>), (<Alphabet_Lower>/<Alphabet_Upper>/"_")*, <Right_Angle_Bracket> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Left_Angle_Bracket, None)), (self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Alphabet_Lower, None)), (self._VAR_NAME, (self.Alphabet_Upper, None))))))), (self._ZERO_OR_MORE, (self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Alphabet_Lower, None)), (self._VAR_NAME, (self.Alphabet_Upper, None)))), (self._TERMINAL, "_"))))))), (self._VAR_NAME, (self.Right_Angle_Bracket, None)))))
    @cache
    def Subexpression(self, position: int, dummy = None):
        """ <Subexpression> = <Left_Bracket>, <RHS>, <Right_Bracket> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Left_Bracket, None)), (self._VAR_NAME, (self.RHS, None)))), (self._VAR_NAME, (self.Right_Bracket, None)))))
    @cache
    def Terminal(self, position: int, dummy = None):
        """ <Terminal> = (<Apostrophe>, <ASCII>, <Apostrophe>)/(<Apostrophe>, "\\", ("n"/"r"/"t"), <Apostrophe>) ; """
        return self._SUBEXPRESSION(position, (self._ORDERED_CHOICE, ((self._SUBEXPRESSION, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Apostrophe, None)), (self._VAR_NAME, (self.ASCII, None)))), (self._VAR_NAME, (self.Apostrophe, None))))), (self._SUBEXPRESSION, (self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Apostrophe, None)), (self._TERMINAL, '\\'))), (self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "n"), (self._TERMINAL, "r"))), (self._TERMINAL, "t")))))), (self._VAR_NAME, (self.Apostrophe, None))))))))
    @cache
    def Nucleus(self, position: int, dummy = None):
        """ <Nucleus> = (<Subexpression>/<Terminal>/<Var_Name>), <Whitespace> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Subexpression, None)), (self._VAR_NAME, (self.Terminal, None)))), (self._VAR_NAME, (self.Var_Name, None))))), (self._VAR_NAME, (self.Whitespace, None)))))
    @cache
    def Atom(self, position: int, dummy = None):
        """ <Atom> = (<And_Predicate>/<Not_Predicate>/<One_Or_More>/<Zero_Or_More>/<Optional>/<Nucleus>), <Whitespace> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.And_Predicate, None)), (self._VAR_NAME, (self.Not_Predicate, None)))), (self._VAR_NAME, (self.One_Or_More, None)))), (self._VAR_NAME, (self.Zero_Or_More, None)))), (self._VAR_NAME, (self.Optional, None)))), (self._VAR_NAME, (self.Nucleus, None))))), (self._VAR_NAME, (self.Whitespace, None)))))
    @cache
    def And_Predicate(self, position: int, dummy = None):
        """ <And_Predicate> = <Ampersand>, <Nucleus> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._VAR_NAME, (self.Ampersand, None)), (self._VAR_NAME, (self.Nucleus, None)))))
    @cache
    def Not_Predicate(self, position: int, dummy = None):
        """ <Not_Predicate> = <Exclamation_Mark>, <Nucleus> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._VAR_NAME, (self.Exclamation_Mark, None)), (self._VAR_NAME, (self.Nucleus, None)))))
    @cache
    def Sequence(self, position: int, dummy = None):
        """ <Sequence> = <Atom>, <Whitespace>, <Comma>, <Whitespace>, <Atom>, (<Comma>, <Whitespace>, <Atom>)* ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Atom, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Comma, None)))), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Atom, None)))), (self._ZERO_OR_MORE, (self._SUBEXPRESSION, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Comma, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Atom, None)))))))))
    @cache
    def Ordered_Choice(self, position: int, dummy = None):
        """ <Ordered_Choice> = <Atom>, <Whitespace>, <Backslash>, <Whitespace>, <Atom>, (<Backslash>, <Whitespace>, <Atom>)* ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Atom, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Backslash, None)))), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Atom, None)))), (self._ZERO_OR_MORE, (self._SUBEXPRESSION, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Backslash, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Atom, None)))))))))
    @cache
    def One_Or_More(self, position: int, dummy = None):
        """ <One_Or_More> = <Nucleus>, <Whitespace>, <Plus> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Nucleus, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Plus, None)))))
    @cache
    def Zero_Or_More(self, position: int, dummy = None):
        """ <Zero_Or_More> = <Nucleus>, <Whitespace>, <Star> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Nucleus, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Star, None)))))
    @cache
    def Optional(self, position: int, dummy = None):
        """ <Optional> = <Nucleus>, <Whitespace>, <Question_Mark> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Nucleus, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Question_Mark, None)))))
    @cache
    def Whitespace(self, position: int, dummy = None):
        """ <Whitespace> = (" "/"\n")* ; """
        return self._SUBEXPRESSION(position, (self._ZERO_OR_MORE, (self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._TERMINAL, " "), (self._TERMINAL, "\n"))))))
    @cache
    def RHS(self, position: int, dummy = None):
        """ <RHS> = <Sequence>/<Ordered_Choice>/<Atom> ; """
        return self._SUBEXPRESSION(position, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Sequence, None)), (self._VAR_NAME, (self.Ordered_Choice, None)))), (self._VAR_NAME, (self.Atom, None)))))
    @cache
    def LHS(self, position: int, dummy = None):
        """ <LHS> = <Var_Name> ; """
        return self._SUBEXPRESSION(position, (self._VAR_NAME, (self.Var_Name, None)))
    @cache
    def Rule(self, position: int, dummy = None):
        """ <Rule> = <LHS>, <Whitespace>, <Assignment>, <Whitespace>, <RHS>, <Whitespace>, <End_Rule>, <Whitespace> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.LHS, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Assignment, None)))), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.RHS, None)))), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.End_Rule, None)))), (self._VAR_NAME, (self.Whitespace, None)))))
    @cache
    def Grammar(self, position: int, dummy = None):
        """ <Grammar> = <Rule>+, <Whitespace> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((self._ONE_OR_MORE, (self._VAR_NAME, (self.Rule, None))), (self._VAR_NAME, (self.Whitespace, None)))))
