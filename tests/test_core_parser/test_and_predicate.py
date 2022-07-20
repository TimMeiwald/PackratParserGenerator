import pytest



class Test_and_predicate():
    @pytest.mark.parametrize("src, arg, answer", [('A', "A" ,(0, True)), 
        ("ABC", "A", (0, True)), 
        ('stuff', "s", (0, True)),
        ("ye", "f", (0, False))])
    def test_and_predicate(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._AND_PREDICATE(0, (parser._TERMINAL, arg))[:2] == (answer)