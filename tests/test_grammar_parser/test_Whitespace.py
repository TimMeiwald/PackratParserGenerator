import pytest



class Test_Whitespace():
    @pytest.mark.parametrize("src, answer", [('0' ,(0, True)), 
        ("ABC", (0, True)), 
        ('001',  (0, True)),
        ("<This_is_a_name>", (0, True)), 
        ('\n',  (1, True)),
        ('\n\n',  (2, True)),
        (' ',  (1, True)),
        ('  ',  (2, True)),
        ("9", (0, True))])
    def test_Whitespace(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.Whitespace.cache_clear()
        tup = (gparser.Whitespace, ())
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        gparser.pretty_print(ret[2])
        gparser._set_src("")
        assert ret[:2] == (answer)