import pytest


class Test_Sequence():
    @pytest.mark.parametrize("src, answer", [('"A" , "B"', (9, True)),
                                             ('"A" ,"B"', (8, True)),
                                             ('"A", "B"', (8, True)),
                                             ("ABC", (0, False)),
                                             ('001', (0, False)),
                                             ("<This_is_a_name>, <Another_Name>",
                                              (32, True)),
                                             ('"A", "B', (0, False)),
                                             ("9", (0, False))])
    def test_Sequence(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.Sequence.cache_clear()
        tup = (gparser.Sequence, ())
        # Needs to be called from _VAR_NAME so that
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined
        # and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup)
        gparser._set_src("")
        assert ret[:2] == (answer)
