from packratparsergenerator.parser.grammar import parse
from packratparsergenerator.parser.core_parser import Parser
from os import getcwd
from os.path import join

if __name__ == "__main__":
    path = join(getcwd(),"packratparsergenerator", "parser", "Grammar.txt")
    print(path)
    ret = parse(path)
    x = Parser()
    x.pretty_print(ret)
