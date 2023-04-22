from packratparsergenerator.core import Core
from packratparsergenerator.grammar_parser import Grammar_Parser


def test_OPTIONAL():

    src = "aaaa"
    c = Grammar_Parser()
    c._set_src(src)
    c.many_A()
    