import pytest



class Test_Alphabet_Lower():
    @pytest.mark.parametrize("src, answer", [('A' ,(0, False)), 
        ("ABC", (0, False)), 
        ('stuff', (1, True)),
        ('n', (1, True)),
        ("ye", (1, True))])
    def test_alphabet_lower(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.Alphabet_Lower.cache_clear()
        tup = (gparser.Alphabet_Lower, None)
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        assert ret[:2] == (answer)