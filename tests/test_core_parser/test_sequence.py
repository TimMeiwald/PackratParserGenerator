import pytest



class Test_sequence():

    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(0, False)), 
    ("ABC", "A", (2, True)), 
    ('stuff', "s", (0, False)), # Zero or more is always True
    ("ye", "A", (0, False))])
    def test_sequence(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._SEQUENCE(0, ((parser._TERMINAL, "A"),(parser._TERMINAL, "B")))[:2] == (answer)
