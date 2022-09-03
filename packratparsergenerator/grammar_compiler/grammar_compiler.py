from packratparsergenerator.grammar_compiler.comment_maker import Comment_Maker
from packratparsergenerator.grammar_compiler.parser_call_maker import Parser_Call_Maker
from packratparsergenerator.parser.core_parser import Node
from packratparsergenerator.parser.rules import Rules
import importlib.resources 

class Rule():

    def __init__(self, rule_node):
        if(rule_node.type != Rules.Rule):
            raise TypeError("This is not a valid rule for Rule")
        self.name = ""
        self.user_comments = None
        self.get_rule_name(rule_node)
        core = self.get_core(rule_node)
        self.comment = Comment_Maker(rule_node).comment
        parser_call_maker = Parser_Call_Maker(rule_node)
        self.parse_string = parser_call_maker.parse_string
        self.semantic_instr = self.get_sem_instr(rule_node)
        self.rule_function = self.generate_function()
        self.rule_enum_stmt = f"{self.name} = "

    def get_rule_name(self, rule_node):
        # Could be done more general but probably slower too
        LHS = rule_node.children[0]
        if(LHS.type != Rules.LHS):
            raise Exception("Something bad happened")
        Var_Name = LHS.children[0]
        self.name = Var_Name.content
        try:
            user_comment = rule_node.children[-1]
            if(user_comment.type == Rules.Comment):
                user_comment.content = user_comment.content[1:-1] #strips comment symbols
                self.user_comments = user_comment
        except IndexError:
            pass
    
    def get_sem_instr(self, rule_node):
        LHS = rule_node.children[0]
        try:
            sem_instr = LHS.children[1]
            return sem_instr
        except IndexError:
            pass

    def get_core(self, rule_node):
        return rule_node.children[1]

    def generate_function(self):
        indent = "    "
        string = "\n"
        string += indent + "@cache\n"
        string += indent + f"def {self.name}(self, position: int, dummy = None):\n"
        string += indent*2 + f'"""\n' 
        string += indent*2 + f'{self.comment}\n'
        if(self.user_comments != None):
            string += indent*2 + "\n"
            string += indent*2 + self.user_comments.content + "\n"
        string += indent*2 + '"""\n'
        string += indent*2 + f"return {self.parse_string}\n"
        return string

class Grammar_Compiler():

    def __init__(self):
        self.rules = []

    def compile(self, node: Node) -> str:
        """Sets what the source to compile is
        Must be a tree of nodes as defined in core_parser.py
        and then compiles
        """
        self.split_by_rule(node)
        grammar_parser = self.make_grammar_parser()
        rules_enum = self.make_rules_enum()
        #with open(join(getcwd(),"packratparsergenerator", "parser", "core_parser.py")) as fp:
        fp = importlib.resources.open_text("packratparsergenerator.parser", "core_parser.py")
        fp.readline() #Removes import so I can replace it correctly
        fp.readline()
        fp.readline()
        fp.readline() #Remove 4 imports I know it's brittle
        fp.readline()
        core_parser = fp.read()
        
        #the parser pass two
        pass_two = self.create_parser_pass_two()

        ret_string = "from collections import deque\n"
        ret_string += "from functools import lru_cache as cache\n"
        ret_string += rules_enum + "\n"
        ret_string += core_parser + "\n"
        ret_string += pass_two + "\n"
        ret_string += grammar_parser
        return ret_string

        
    def create_parser_pass_two(self):
        fp = importlib.resources.open_text("packratparsergenerator.parser", "parser_pass_two.py")
        for i in range(0,9):
            fp.readline() #remove first 10 lines so I can construct it with different typles(based on grammar)
        pass_two = fp.read()
        indent = "    "
        string = "class Parser_Pass_Two():\n\n"
        string += indent + "def __init__(self):\n"
        nodes = self.get_nodes(Rules.Delete)
        string += 2*indent + f"self.delete_nodes = {nodes}\n"
        nodes = self.get_nodes(Rules.Passthrough)
        string += 2*indent + f"self.passthrough_nodes = {nodes}\n"
        nodes = self.get_nodes(Rules.Collect)
        string += 2*indent + f"self.collect_nodes = {nodes}\n"
        string += pass_two
        return string
    
    def get_nodes(self, type):
        list = []
        for rule in self.rules:
            if(rule.semantic_instr == None):
                continue
            if(rule.semantic_instr.type == type):
                list.append(rule.name)
        str = "("
        for sem_instr in list:
            str += f"Rules.{sem_instr}, "
        str += ")"
        return str


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
        fp = importlib.resources.open_text("packratparsergenerator.grammar_compiler.core_blocks", "rules.py")
        string = fp.read()
        indent = "    "
        string += indent + "# Following enum values are all autogenerated from grammar file\n"
        for index, rule in enumerate(self.rules):
            string += indent + rule.rule_enum_stmt + f"{index+20}\n"
        return string




