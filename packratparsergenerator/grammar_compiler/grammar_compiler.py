from packratparsergenerator.parser.grammar import parse
from packratparsergenerator.grammar_compiler.comment_maker import Comment_Maker
from packratparsergenerator.grammar_compiler.parser_call_maker import Parser_Call_Maker
from packratparsergenerator.parser.rules import Rules
from os import getcwd
from os.path import join

class Rule():

    def __init__(self, rule_node):
        if(rule_node.type != Rules.Rule):
            raise TypeError("This is not a valid rule for Rule")
        self.name = ""
        self.get_rule_name(rule_node)
        core = self.get_core(rule_node)
        self.comment = Comment_Maker(rule_node).comment
        self.parse_string = Parser_Call_Maker(rule_node).parse_string
        self.rule_function = self.generate_function()
        self.rule_enum_stmt = f"{self.name} = "

    def get_rule_name(self, rule_node):
        # Could be done more general but probably slower too
        LHS = rule_node.children[0]
        if(LHS.type != Rules.LHS):
            raise Exception("Something bad happened")
        Var_Name = LHS.children[0]
        self.name = Var_Name.content

    def get_core(self, rule_node):
        return rule_node.children[1]

    def generate_function(self):
        indent = "    "
        string = indent + "@cache\n"
        string += indent + f"def {self.name}(self, position: int, dummy = None):\n"
        string += indent*2 + f'""" {self.comment} """' + "\n"
        string += indent*2 + f"return {self.parse_string}\n"
        return string

class Grammar_Compiler():

    def __init__(self):
        self.rules = []

    def compile(self, node, dest_filepath):
        """Sets what the source to compile is
        Must be a tree of nodes as defined in core_parser.py
        and then compiles"""
        self.split_by_rule(node)
        grammar_parser = self.make_grammar_parser()
        rules_enum = self.make_rules_enum()
        with open(join(getcwd(),"packratparsergenerator", "parser", "core_parser.py")) as fp:
            fp.readline() #Removes import so I can replace it correctly
            fp.readline()
            fp.readline()
            fp.readline() #Remove 4 imports I know it's brittle
            fp.readline()
            core_parser = fp.read()
        
        #the parser pass two
        with open(join(getcwd(),"packratparsergenerator", "parser", "parser_pass_two.py")) as fp:
            fp.readline()
            fp.readline()
            pass_two = fp.read()

        with open(join(dest_filepath, "parser.py"), "w") as fp:
            fp.write("from collections import deque\n")
            fp.write("from functools import lru_cache as cache\n")
            fp.write(rules_enum)
            fp.write(core_parser)
            fp.write(pass_two)
            fp.write(grammar_parser)
        


    def split_by_rule(self, node):
        for rule in node.children:
            assert rule.type == Rules.Rule
            self.rules.append(Rule(rule))
    
    def make_grammar_parser(self):
        indent = "    "
        string = f"""

class Grammar_Parser(Parser):

    def _set_src(self, src: str):
        super()._set_src(src)
        for rule in Rules:
            if(rule >= 20): #Less than 20 is core parser stuff, greatereq than 20 is inherited class stuff
                func = getattr(self, rule.name)
                func.cache_clear()
"""
        for rule in self.rules:
            string += rule.rule_function
        return string
    
    def make_rules_enum(self):
        path = join(getcwd(),"packratparsergenerator", "grammar_compiler", "core_blocks", "rules.py")
        with open(path) as fp:
            string = fp.read()
        indent = "    "
        for index, rule in enumerate(self.rules):
            string += indent + rule.rule_enum_stmt + f"{index+20}\n"
        return string




if __name__ == "__main__":
    path = join(getcwd(),"packratparsergenerator", "parser", "Grammar.txt")
    print(path)
    import cProfile
    #cProfile.run("node = parse(src_filepath =path)")
    node = parse(src_filepath = path)
    #node.pretty_print()
    compiler = Grammar_Compiler()
    path = join(getcwd(), "Generated_Output")
    compiler.compile(node, path)


    