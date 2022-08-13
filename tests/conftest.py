import pytest
from packratparsergenerator.parser.grammar_parser import Grammar_Parser
from Generated_Output.grammar_parser import Grammar_Parser as Grammar_Parser_2
from packratparsergenerator.parser.core_parser import Parser

@pytest.fixture(autouse = True)
def parser():
    parser = Parser()
    return parser

@pytest.fixture(autouse = True)
def gparser():
    parser = Grammar_Parser()
    return parser

