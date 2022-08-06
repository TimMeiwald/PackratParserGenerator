from ast import Index
from packratparsergenerator.parser.core_parser import Rules, Parser
from packratparsergenerator.parser.grammar_parser import Grammar_Parser
from packratparsergenerator.parser.grammar import parse

class Parser_Call_Maker():

    def __init__(self, node):
        if(node == None):
            raise TypeError("Inputted node is None, maybe the rule failed when you expected success")
        self.parse_string = self.create_parse_string(node)
        

    def create_parse_string(self, node):
        p_string = self.selector(node)
        return p_string
    
    def selector(self, node):
        if(node.content == "Sequence"):
            return self.p_sequence(node)
        elif(node.content == "Ordered_Choice"):
            return self.p_ordered_choice(node)
        elif(node.content == "One_Or_More"):
            return self.p_one_or_more(node)
        elif(node.content == "Zero_Or_More"):
            return self.p_zero_or_more(node)
        elif(node.content == "Optional"):
            return self.p_optional(node)
        elif(node.content == "And_Predicate"):
            return self.p_and_predicate(node)
        elif(node.content == "Not_Predicate"):
            return self.p_not_predicate(node)
        elif(node.content == "Subexpression"):
            return self.p_subexpression(node)
        elif(node.content == "Rule"):
            return self.p_rule(node)
        elif(node.content == "LHS"):
            return self.p_lhs(node)
        elif(node.content == "Terminal"):
            return self.p_terminal(node)
        elif(node.type == Rules._TERMINAL):
            return self.p_TERMINAL(node)
        else:
            return self.p_var_name(node)

    def p_sequence(self, node):
        p_string = ""
        for index in range(0, len(node.children)-1):
            if(index == 0):
                p_string = "(self._SEQUENCE, (" +  self.selector(node.children[index]) + ", " + self.selector(node.children[index+1])  + "))"
            else:
                p_string =  "(self._SEQUENCE, (" + p_string + ", " +self.selector(node.children[index+1]) + "))"
        return p_string
    
    def p_ordered_choice(self, node):
        p_string = ""
        for index in range(0, len(node.children)-1):
            if(index == 0):
                p_string = "(self._ORDERED_CHOICE, (" +  self.selector(node.children[index]) + ", " + self.selector(node.children[index+1])  + "))"
            else:
                p_string =  "(self._ORDERED_CHOICE, (" + p_string + ", " +self.selector(node.children[index+1]) + "))"
        return p_string
    
    def p_subexpression(self, node):
        try:
            child = node.children[0]
            child_str = self.selector(child)
            p_string = "(self._SUBEXPRESSION, " + child_str + ")"
        except IndexError:
            p_string = self.p_var_name(node)
        return p_string
    
    def p_var_name(self, node):
        p_string = "(self._VAR_NAME, (" + "self." + node.content + ",None))"
        return p_string
    
    def p_rule(self, node):
        try:
            p_string = self.selector(node.children[1])
            p_string = "self._VAR_NAME(position, " + p_string + ")"
        except IndexError:
            p_string = self.p_var_name(node)
        return p_string
    
    def p_lhs(self, node):
        try:
            p_string = self.selector(node.children[0])
        except IndexError:
            p_string = self.p_var_name(node)
        return p_string
    
    def p_and_predicate(self, node):
        p_string = "(self._AND_PREDICATE, " + self.selector(node.children[0]) + ")"
        return p_string
    
    def p_not_predicate(self, node):
        p_string = "(self._NOT_PREDICATE, " + self.selector(node.children[0]) + ")"
        return p_string
    
    def p_optional(self, node):
        p_string = "(self._OPTIONAL, " + self.selector(node.children[0]) + ")"
        return p_string
    
    def p_one_or_more(self, node):
        p_string = "(self._ONE_OR_MORE, " + self.selector(node.children[0]) + ")"
        return p_string
    
    def p_zero_or_more(self, node):
        p_string = "(self._ZERO_OR_MORE, " + self.selector(node.children[0]) + ")"
        return p_string
    
    def p_terminal(self, node):
        #p_string = "(self.Terminal, " + self.selector(node.children[0]) + ")"
        p_string = self.selector(node.children[0])
        return p_string

    def p_TERMINAL(self, node):
        if(node.content == '"'):
            p_string = "(self._TERMINAL, '" + node.content + "')"
        else:
            p_string = "(self._TERMINAL, " + '"' + node.content + '"' + ")"
        return p_string

if __name__ == "__main__":
    src = '<ASCII> = &(<Alphabet_Lower>/<Alphabet_Upper>+),!(<Num>/<Spaces>*/<Specials>), <Specials>?;'
    src = '<All> = "A","B","C","D","E";'
    src = '<All> = "A"*;' 
    node = parse(src = src)
    node = node.children[0]
    parser = Grammar_Parser()
    parser.pretty_print(node)
    
    x = Parser_Call_Maker(node)
    print(x.parse_string)

    position = 0
    parser._set_src("ABCDE")
    position, bool, node = parser._VAR_NAME(position, (parser._SEQUENCE, ((parser._SEQUENCE, ((parser._SEQUENCE, ((parser._SEQUENCE, ((parser._TERMINAL, "A"), (parser._TERMINAL, "B"))), (parser._TERMINAL, "C"))), (parser._TERMINAL, "D"))), (parser._TERMINAL, 
"E"))))
    print(position, bool)
    parser.pretty_print(node)

    position = 0
    parser._set_src("AAAAAA")
    position, bool, node = parser._VAR_NAME(position, (parser._ZERO_OR_MORE, (parser._TERMINAL, "A")))
    print(position, bool)
    parser.pretty_print(node)
    

    
 
    