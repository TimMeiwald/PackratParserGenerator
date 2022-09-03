import pytest


class Test_LHS():

    @pytest.mark.parametrize("src, answer", [('0', (0, False)),
                                             ("ABC", (0, False)),
                                             ('001', (0, False)),
                                             ('<A>', (3, True)),
                                             ("<This_is_a_name>", (16, True)),
                                             ("<name>", (6, True)),
                                             ('001', (0, False)),
                                             ("9", (0, False))])
    def test_LHS(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.LHS.cache_clear()
        tup = (gparser.LHS, None)
        # Needs to be called from _VAR_NAME so that
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined
        # and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup)
        assert ret[:2] == (answer)
