import pytest



class Test_Alphabet_Upper():
    @pytest.mark.parametrize("src, answer", [('A' ,(1, True)), 
        ("BBC", (1, True)), 
        ('stuff', (0, False)),
        ("ye", (0, False))])
    def test_alphabet_upper(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.Alphabet_Upper.cache_clear()
        tup = (gparser.Alphabet_Upper, None)
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        gparser.pretty_print(ret[2])
        assert ret[:2] == (answer)