import pytest



class Test_subexpr():

    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(1, True)), 
    ("ABC", "A", (1, True)), 
    ('stuff', "s", (1, True)), # Zero or more is always True
    ("ye", "A", (0, False))])
    def test_subexpr(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._SUBEXPR(0, (parser._test, arg))[:2] == (answer)
