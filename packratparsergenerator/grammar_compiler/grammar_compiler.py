from packratparsergenerator.parser.grammar import parse
from packratparsergenerator.parser.core_parser import Parser
from packratparsergenerator.grammar_compiler.comment_maker import Comment_Maker
from packratparsergenerator.grammar_compiler.parser_call_maker import Parser_Call_Maker
from os import getcwd
from os.path import join


class Rule():

    def __init__(self, rule_node):
        if(rule_node.content != "Rule"):
            raise TypeError("This is not a valid rule for Rule")
        self.name = ""
        self.get_rule_name(rule_node)
        core = self.get_core(rule_node)
        Parser().pretty_print(rule_node) 
        print("\n")
        self.comment = Comment_Maker(rule_node).comment
        self.parse_string = Parser_Call_Maker(rule_node).parse_string


    def match(self, node, type=None, content=None):
        if(type == None):
            if(node.content == content):
                return True
            else:
                raise ValueError(f"Not a match, Got: {node.content}, Expected: {content}")
        elif(content == None):
            if(node.type == content):
                return True
            else:
                raise ValueError(f"Not a match, Got: {node.type}, Expected: {type}")
        elif(node.type.value == type and node.content == content):
            return True
        else:
            raise ValueError("Must pass type or content")

    def get_rule_name(self, rule_node):
        # Could be done more general but probably slower too
        LHS = rule_node.children[0]
        self.match(LHS, content = "LHS")
        Var_Name = LHS.children[0]
        self.name = Var_Name.content

    def get_core(self, rule_node):
        return rule_node.children[1]


class Grammar_Compiler():

    def __init__(self):
        self.rules = []

    def compile(self, node):
        """Sets what the source to compile is
        Must be a tree of nodes as defined in core_parser.py
        and then compiles"""
        self.split_by_rule(node)
    
    def split_by_rule(self, node):
        for rule in node.children:
            self.rules.append(Rule(rule))




if __name__ == "__main__":
    path = join(getcwd(),"packratparsergenerator", "parser", "Grammar.txt")
    print(path)
    import cProfile
    cProfile.run("node = parse(src_filepath =path)")
    #node = parse(src_filepath =path)
    #compiler = Grammar_Compiler()
    #compiler.compile(node)

    #parser = Parser()

    #parser.pretty_print(node)

    #for rule in compiler.rules:
    #    print(rule.comment + "\n")