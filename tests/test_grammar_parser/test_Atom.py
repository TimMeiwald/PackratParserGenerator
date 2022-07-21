import pytest



class Test_Atom():
    @pytest.mark.parametrize("src, answer", [('+' ,(0, False)), 
        ('<var>+' ,(6, True)), 
        ('<var>+   ' ,(9, True)), 
        ('<var>*' ,(6, True)), 
        ('<var>?' ,(6, True)), 
        ("!<var>", (6, True)), 
        ('&<var>',  (6, True)),
        ('"A"+' ,(4, True)), 
        ('"A"+   ' ,(7, True)), 
        ('"A"*' ,(4, True)), 
        ('"A"?' ,(4, True)), 
        ('!"A"', (4, True)), 
        ('&"A"',  (4, True)),
        ("<This_is_a_name>/ <Another_Name>", (16, True)), 
        ('"A"/ "B',  (3, True)),
        ("9", (0, False))])
    def test_Atom(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.Atom.cache_clear()
        tup = (gparser.Atom, ())
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        gparser.pretty_print(ret[2])
        gparser._set_src("")
        assert ret[:2] == (answer)
