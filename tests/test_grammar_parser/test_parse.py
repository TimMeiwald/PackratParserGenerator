from packratparsergenerator.parser.grammar_parser import Grammar_Parser
from os import getcwd
from os.path import join


def test_parse():
    parser = Grammar_Parser()
    with open(join(getcwd(), "packratparsergenerator","parser", "Grammar.txt")) as fp:
        src = fp.read()
    position, bool, node = parser.parse(src, parser.Grammar)
    node.pretty_print()