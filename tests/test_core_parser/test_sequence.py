import pytest



class Test_sequence():

    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(0, False)), 
    ("ABC", "A", (2, False)), 
    ('stuff', "s", (0, False)), # Zero or more is always True
    ("ye", "A", (0, False))])
    def test_sequence(self, parser, src, arg, answer):
        parser._set_src(src)
        ret = parser._SEQUENCE(0, ((parser._TERMINAL, "A"),(parser._TERMINAL, "B")))
        parser.pretty_print(ret[2])
        assert ret[:2] == (answer)

    #Nested Sequence
    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A" ,(0, False)), 
    ("ABC", "A", (0, False)), 
    ("ABCD", "A", (0, False)), 
    ('stuff', "s", (0, False)), # Zero or more is always True
    ("ye", "A", (0, False))])
    def test_sequence_nested(self, parser, src, arg, answer):
        parser._set_src(src)
        tup1 = (parser._TERMINAL, "A")
        tup2 = (parser._TERMINAL, "B")
        tup3 = (parser._TERMINAL, "C")
        tup4 = (parser._TERMINAL, "D")
        tup5 = (parser._SEQUENCE, (tup1, tup2))
        tup6 = (parser._SEQUENCE, (tup5, tup3))
        tup7 =  (parser._SEQUENCE, (tup6, tup4))
        ret = parser._VAR_NAME(0, tup7)
        parser.pretty_print(ret[2])
        assert ret[:2] == (answer)
