from packratparsergenerator.core import Core
from packratparsergenerator.grammar_parser import Grammar_Parser


def test_direct_left_recursion():

    src = "aaaa"
    c = Grammar_Parser()
    c._set_src(src)
    bool = c.many_A(None)
    assert bool == True
    assert c.position == 4


def test_direct_left_recursion_incorrect():

    src = "aabb"
    c = Grammar_Parser()
    c._set_src(src)
    bool = c.many_A(None)
    assert bool == True
    assert c.position == 2


def test_direct_left_recursion_incorrect2():

    src = "bbbb"
    c = Grammar_Parser()
    c._set_src(src)
    bool = c.many_A(None)
    assert bool == False
    assert c.position == 0