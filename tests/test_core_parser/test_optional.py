import pytest

class Test_optional():

    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(1, True)), 
    ("ABC", "A", (1, True)), 
    ('stuff', "s", (1, True)), # Zero or more is always True
    ("ye", "f", (0, True))])
    def test_optional(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._OPTIONAL(0, (parser._TERMINAL, arg))[:2] == (answer)
