from packratparsergenerator.core import Core
from packratparsergenerator.grammar_parser import Grammar_Parser


def test_direct_left_recursion():

    src = "aaaa"
    c = Grammar_Parser()
    c._set_src(src)
    bool = c.many_A()
    assert bool == True
    assert c.position == 4