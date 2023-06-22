from packratparsergenerator.grammar_compiler.comment_maker import Comment_Maker
from packratparsergenerator.grammar_compiler.parser_call_maker import Parser_Call_Maker
from packratparsergenerator.parser.core_parser import Node
from packratparsergenerator.parser.rules import Rules
import importlib.resources


def create_rule_header(rule_name):
    c= rule_name.split("_")
    camelcase = ""
    for i in c:
        camelcase += i.title()
    
    rule = f"""
    #[derive(Copy, Clone)]
    pub struct {camelcase};
    impl Resolvable for {camelcase} {{
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {{
        let hook = {rule_name.lower()}(position, source); 
        return hook;
        }}
    }}
    
    fn {rule_name.lower()}(position: u32, source: &str) -> (bool, u32) {{
    """
    return rule


class Grammar_Compiler():

    def __init__(self):
        self.rules = []

    def compile(self, node: Node) -> str:
        """Sets what the source to compile is
        Must be a tree of nodes as defined in core_parser.py
        and then compiles
        """

        for child in node.children:
            rule_name = child.children[0].children[0].content
            header = create_rule_header(rule_name)
            header += "return " + Parser_Call_Maker(child).parse_string + ";"
            header += "}"
            self.rules.append(header)
        
        result = ""
        for i in self.rules:
            result += i
            result += "\n"
        return result