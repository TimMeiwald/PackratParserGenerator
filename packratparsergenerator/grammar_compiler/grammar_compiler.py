from packratparsergenerator.parser.grammar import parse
from packratparsergenerator.parser.core_parser import Parser
from os import getcwd
from os.path import join


class Rule():

    def __init__(self, rule_node):
        if(rule_node.content != "Rule"):
            raise TypeError("This is not a valid rule for Rule")



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
            x = Rule(rule)
            self.rules.append(Rule(rule))




if __name__ == "__main__":
    path = join(getcwd(),"packratparsergenerator", "parser", "Grammar.txt")
    print(path)
    node = parse(path)
    compiler = Grammar_Compiler()
    compiler.compile(node)