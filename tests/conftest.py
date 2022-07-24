import pytest
from packratparsergenerator.parser.grammar_parser import Grammar_Parser
from packratparsergenerator.parser.core_parser import Parser

@pytest.fixture(autouse = True)
def parser():
    parser = Parser()
    return parser

@pytest.fixture(autouse = True)
def gparser():
    parser = Grammar_Parser()
    return parser

