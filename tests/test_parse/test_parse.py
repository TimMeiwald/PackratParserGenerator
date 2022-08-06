import pytest
from os import getcwd
from os.path import join
from packratparsergenerator.parser.grammar import parse

class Test_parse():
    
    def test_parse(self, parser):
        path = join(getcwd(), "tests", "test_grammar_parser", "Grammar.txt")
        ret = parse(src_filepath=path)
        ret.pretty_print()
        assert 0 == 0 #Allows me to see output by switching this true or false


    