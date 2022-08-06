import pytest



class Test_ASCII():
    @pytest.mark.parametrize("src, answer", [('0' ,(1, True)), 
        ("ABC", (1, True)), 
        ('001',  (1, True)),
        ('*',  (1, True)),
        ('Ü',  (0, False)),
        ("9", (1, True))])
    def test_ASCII(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.ASCII.cache_clear()
        tup = (gparser.ASCII, None)
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        assert ret[:2] == (answer)