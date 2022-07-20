import pytest



class Test_not_predicate():
    @pytest.mark.parametrize("src, arg, answer", [('A', "A" ,(0, False)), 
        ("ABC", "A", (0, False)), 
        ('stuff', "s", (0, False)),
        ("ye", "f", (0, True))])
    def test_not_predicate(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._NOT_PREDICATE(0, (parser._TERMINAL, arg))[:2] == (answer)