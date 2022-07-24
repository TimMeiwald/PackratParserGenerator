import pytest



class Test_ordered_choice():

    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(1, True)), 
    ("ABC", "A", (1, True)), 
    ('stuff', "s", (0, False)), # Zero or more is always True
    ("ye", "A", (0, False))])
    def test_ordered_choice(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._ORDERED_CHOICE(0, ((parser._TERMINAL, "A"),(parser._TERMINAL, "B")))[:2] == (answer)

    #Nested Sequence
    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(1, True)), 
    ("BBC", "A", (1, True)), 
    ("ABCD", "A", (1, True)), 
    ('stuff', "s", (0, False)), # Zero or more is always True
    ("ye", "A", (0, False))])
    def test_ordered_choice_nested(self, parser, src, arg, answer):
        parser._set_src(src)
        tup1 = (parser._TERMINAL, "A")
        tup2 = (parser._TERMINAL, "B")
        tup3 = (parser._TERMINAL, "C")
        tup4 = (parser._TERMINAL, "D")
        tup5 = (parser._ORDERED_CHOICE, (tup1, tup2))
        tup6 = (parser._ORDERED_CHOICE, (tup5, tup3))
        ret = parser._ORDERED_CHOICE(0, (tup6, tup4))
        parser.pretty_print(ret[2])
        assert ret[:2] == (answer)
