import pytest
from src.grammar_parser import Grammar_Parser
from src.core_parser import Parser

@pytest.fixture(scope="module",autouse = True)
def parser():
    parser = Parser()
    return parser

@pytest.fixture(scope="module",autouse = True)
def gparser():
    parser = Grammar_Parser()
    return parser

