import pytest


class Test_zone_or_more():

    @pytest.mark.parametrize("src, arg, answer", [('AAAA', "A", (4, True)),
                                                  ("ABC", "A", (1, True)),
                                                  ('stuff', "s", (1, True)),
                                                  ("ye", "f", (0, False))])
    def test_one_or_more(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._ONE_OR_MORE(0, (parser._TERMINAL, arg))[:2] == (answer)
