import pytest

class Test_Var_Name():
    
    """@pytest.mark.parametrize("src, answer", [('0' ,(0, False)), 
        ("ABC", (0, False)), 
        ('001',  (0, False)),
        ('<A>',  (3, True)),
        ("<This_is_a_name>", (16, True)), 
        ("<name>", (6, True)), 
        ('001',  (0, False)),
        ("9", (0, False))])
    def test_var_name(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.Var_Name.cache_clear()
        tup = (gparser.Var_Name, None)
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        gparser.pretty_print(ret[2])
        assert ret[:2] == (answer)"""

    def test_A(self, gparser):
        gparser._set_src("<A>")
        gparser.Var_Name.cache_clear()
        tup = (gparser.Var_Name, None)
        ret = gparser._VAR_NAME(0, tup) 
        print(ret)
        gparser.pretty_print(ret[2])
        assert ret[:2] == (3, True)
    
    def test_B(self, gparser):
        gparser._set_src("<B>")
        gparser.Var_Name.cache_clear()
        tup = (gparser.Var_Name, None)
        ret = gparser._VAR_NAME(0, tup) 
        print(ret)
        gparser.pretty_print(ret[2])
        assert ret[:2] == (3, True)

if __name__ == "__main__":
    from src.grammar_parser import Grammar_Parser
    gparser = Grammar_Parser()
    gparser._set_src("<A>")
    gparser.Var_Name.cache_clear()
    tup = (gparser.Var_Name, None)
    ret = gparser._VAR_NAME(0, tup) 
    print(ret)
    gparser.pretty_print(ret[2])
    assert ret[:2] == (3, True)
