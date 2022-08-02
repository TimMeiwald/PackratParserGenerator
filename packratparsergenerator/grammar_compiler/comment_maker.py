from packratparsergenerator.parser.core_parser import Rules, Parser
from packratparsergenerator.parser.grammar_parser import Grammar_Parser
from packratparsergenerator.parser.grammar import parse

class Comment_Maker():

    def __init__(self, node):
        if(node == None):
            raise TypeError("Inputted node is None, maybe the rule failed when you expected success")
        self.comment = self.create_comment(node)

    def create_comment(self, node):
        c_string = self.selector(node)
        return c_string
    
    def selector(self, node):
        if(node.content == "Sequence"):
            return self.c_sequence(node)
        elif(node.content == "Ordered_Choice"):
            return self.c_ordered_choice(node)
        elif(node.content == "One_Or_More"):
            return self.c_one_or_more(node)
        elif(node.content == "Zero_Or_More"):
            return self.c_zero_or_more(node)
        elif(node.content == "Optional"):
            return self.c_optional(node)
        elif(node.content == "And_Predicate"):
            return self.c_and_predicate(node)
        elif(node.content == "Not_Predicate"):
            return self.c_not_predicate(node)
        elif(node.content == "Subexpression"):
            return self.c_subexpression(node)
        elif(node.content == "Rule"):
            return self.c_rule(node)
        elif(node.content == "LHS"):
            return self.c_lhs(node)
        elif(node.type == Rules._TERMINAL):
            return self.c_terminal(node)
        else:
            return self.c_var_name(node)

    def c_sequence(self, node):
        c_string = ""
        for child in node.children:
            child_str = self.selector(child)
            c_string += child_str + ", "
        c_string = c_string[:-2] #removes last comma and space
        return c_string
    
    def c_ordered_choice(self, node):
        c_string = ""
        for child in node.children:
            child_str = self.selector(child)
            c_string += child_str + "/"
        c_string = c_string[:-1] #removes last comma and space
        return c_string
    
    def c_subexpression(self, node):
        c_string = "("
        child = node.children[0]
        child_str = self.selector(child)
        c_string += child_str + ")"
        return c_string
    
    def c_var_name(self, node):
        c_string = "<"
        c_string += node.content
        c_string += ">"
        return c_string
    
    def c_rule(self, node):
        c_string = ""
        c_string += self.selector(node.children[0])
        c_string += self.selector(node.children[1])
        c_string += " ;"
        return c_string
    
    def c_lhs(self, node):
        c_string = self.selector(node.children[0])
        c_string += " = "
        return c_string
    
    def c_and_predicate(self, node):
        c_string = "&" + self.selector(node.children[0])
        return c_string
    
    def c_not_predicate(self, node):
        c_string = "!" + self.selector(node.children[0])
        return c_string
    
    def c_optional(self, node):
        c_string = self.selector(node.children[0]) + "?"
        return c_string
    
    def c_one_or_more(self, node):
        c_string = self.selector(node.children[0]) + "+"
        return c_string
    
    def c_zero_or_more(self, node):
        c_string = self.selector(node.children[0]) + "*"
        return c_string

if __name__ == "__main__":
    src = '<ASCII> = &(<Alphabet_Lower>/<Alphabet_Upper>+),!(<Num>/<Spaces>*/<Specials>), <Specials>?;'
    node = parse(src = src)
    node = node.children[0]
    parser = Parser()
    parser.pretty_print(node)

    x = Comment_Maker(node)
    print(x.comment)
    
 
    
