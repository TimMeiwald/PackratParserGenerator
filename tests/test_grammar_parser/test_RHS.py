import pytest


class Test_RHS():
    @pytest.mark.parametrize("src, answer", [('"A"', (3, True)),
                                             ('"A"*', (4, True)),
                                             ('"A"+', (4, True)),
                                             ('"A"?', (4, True)),
                                             ('!"A"', (4, True)),
                                             ('&"A"', (4, True)),
                                             ('!("A")', (6, True)),
                                             ('&(<var>)', (8, True)),
                                             ('("A" /"B")', (10, True)),
                                             ('"A"/ "B"', (8, True)),
                                             ('("A")', (5, True)),
                                             ('(<var>)', (7, True)),
                                             ("ABC", (0, False)),
                                             ('001', (0, False)),
                                             ("<This_is_a_name>/ <Another_Name>",
                                              (32, True)),
                                             ('"A"/ "B', (3, True)),
                                             ("9", (0, False))])
    def test_RHS(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.RHS.cache_clear()
        tup = (gparser.RHS, None)
        # Needs to be called from _VAR_NAME so that
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined
        # and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup)
        gparser._set_src("")
        assert ret[:2] == (answer)
