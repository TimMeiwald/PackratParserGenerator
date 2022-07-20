import pytest

class Test_zero_or_more():

    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(4, True)), 
    ("ABC", "A", (1, True)), 
    ('stuff', "s", (1, True)), # Zero or more is always True
    ("ye", "f", (0, True))])
    def test_zero_or_more_terminal(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._ZERO_OR_MORE(0, (parser._TERMINAL, arg))[:2] == (answer)
    
    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(4, True)), 
    ("ABC", "A", (3, True)), 
    ('stuff', "s", (0, True)), # Zero or more is always True
    ("ye", "f", (0, True))])
    def test_zero_or_more_var_name(self, gparser, src, arg, answer):
        gparser._set_src(src)
        tup3 = (gparser._VAR_NAME, (gparser.Alphabet_Upper, None))
        assert gparser._ZERO_OR_MORE(0, tup3)[:2] == (answer)

    
