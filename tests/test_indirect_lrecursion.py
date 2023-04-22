from packratparsergenerator.core import Core
from packratparsergenerator.grammar_parser import Grammar_Parser


def test_indirect_correct():
    src = "ababab"
    c = Grammar_Parser()
    c._set_src(src)
    b = c.B(None)
    print(c.position, b)
    assert len(src) == c.position, f"Source Length {len(src)}, Position: {c.position}"
    assert b == True

def test_indirect_incorrect():
    src = "abababaaaaa"
    c = Grammar_Parser()
    c._set_src(src)
    b = c.B(None)
    print(c.position, b)
    assert len(src) == c.position, f"Source Length {len(src)}, Position: {c.position}"
    assert b == True