from packratparsergenerator.grammar_parser import Grammar_Parser
from os import getcwd
from os.path import join
def test_read_grammar():
    with open(join(getcwd(), "packratparsergenerator", "Grammar.txt"), "r") as fp:
        src = fp.read()
    c = Grammar_Parser()
    c._set_src(src)
    c.Grammar()
    assert len(src) == c.position, f"Source Length {len(src)}, Position: {c.position}"
    c.position=0
    c.Grammar() 
    assert len(src) == c.position, f"Source Length {len(src)}, Position: {c.position}"
    

    assert 0 == 1
