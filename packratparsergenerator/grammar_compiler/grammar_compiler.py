from packratparsergenerator.grammar_compiler.comment_maker import Comment_Maker
from packratparsergenerator.grammar_compiler.parser_call_maker import Parser_Call_Maker
from packratparsergenerator.parser.core_parser import Node
from packratparsergenerator.parser.rules import Rules
import importlib.resources

def camel_case(name):
    c= name.split("_")
    camelcase = ""
    for i in c:
        camelcase += i.title()
    return camelcase

def create_rule_header(count, rule_name, rule_content):
    camelcase = camel_case(rule_name)
    rule = f"""
    #[derive(Copy, Clone)]
    pub struct {camelcase};
    impl Resolvable for {camelcase} {{
    fn resolve(&self, cache: &mut Cache, position: u32, source: &str) -> (bool, u32) {{ 
        let rule = {rule_content};
        let hook = cache_struct_wrapper(cache, rule, Rules::{camelcase} as u32, position, source);
        return hook;
        }}
    }}
    """
    return rule


class Grammar_Compiler():

    def __init__(self):
        self.rules = []
        self.enum_list = []
        self.count = 0

    def compile(self, node: Node) -> str:
        """Sets what the source to compile is
        Must be a tree of nodes as defined in core_parser.py
        and then compiles
        """
        for child in node.children:
            rule_name = child.children[0].children[0].content
            crule_name = camel_case(rule_name)
            self.enum_list.append(crule_name)
            rule_content = Parser_Call_Maker(child).parse_string
            header = create_rule_header(self.count, rule_name, rule_content)
            self.count += 1
            self.rules.append(header)
        
        result = "enum Rules{"
        for i in self.enum_list:
            result += i + ",\n"
        result += "}\n\n"
        for i in self.rules:
            result += i
            result += "\n"
        

        return result