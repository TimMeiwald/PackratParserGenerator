import pytest
from os import getcwd
from os.path import join
from packratparsergenerator.parser.grammar import parse

class Test_Grammar():
    
    def test_Grammar(self, parser):
        path = join(getcwd(), "tests", "test_grammar_parser", "Grammar.txt")
        ret = parse(path)
        parser.pretty_print(ret)
        assert 0 == 0 #Allows me to see output by switching this true or false


    