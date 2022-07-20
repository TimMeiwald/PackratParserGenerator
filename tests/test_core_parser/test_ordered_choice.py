import pytest



class Test_ordered_choice():

    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(1, True)), 
    ("ABC", "A", (1, True)), 
    ('stuff', "s", (0, False)), # Zero or more is always True
    ("ye", "A", (0, False))])
    def test_ordered_choice(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._ORDERED_CHOICE(0, ((parser._TERMINAL, "A"),(parser._TERMINAL, "B")))[:2] == (answer)
