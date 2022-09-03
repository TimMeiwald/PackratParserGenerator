import pytest


class Test_Terminal():

    @pytest.mark.parametrize("src, arg, answer", [('A', "A", (1, True)),
                                                  ("ABC", "A", (1, True)),
                                                  ('stuff', "s", (1, True)),
                                                  ('\n', "\n", (1, True)),
                                                  ('\r', "\r", (1, True)),
                                                  ('\t', "\t", (1, True)),
                                                  ('\\', "\\", (1, True)),
                                                  ("ye", "f", (0, False))])
    def test_terminal(self, parser, src, arg, answer):
        parser._set_src(src)
        assert parser._TERMINAL(0, arg)[:2] == (answer)

    @pytest.mark.parametrize("src, arg, answer", [
        ("AAC", "A", (2, True)),  # Succeeds because 2 A
        ("\t\t A", "\t", (2, True)),
        ("ABC", "A", (1, False)),
        ('stuff', "s", (1, False)),  # Fails cause only 1 s#
        ("ye", "f", (0, False))])
    def test_sequential_terminals(self, parser, src, arg, answer):
        parser._set_src(src)
        position, bool, node = parser._TERMINAL(0, arg)
        assert parser._TERMINAL(position, arg)[:2] == (answer)
