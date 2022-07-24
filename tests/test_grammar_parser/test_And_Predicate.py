import pytest



class Test_And_Predicate():
    @pytest.mark.parametrize("src, answer", [('&"A"' ,(4, True)), 
        ('&<var>' ,(6, True)), 
        ('&(<var>)' ,(8, True)), 
        ('&("A")' ,(6, True)), 
        ('&(<var>)   ' ,(11, True)), 
        ('&(<var>)' ,(8, True)), 
        ('<var>?' ,(0, False))])
    def test_And_Predicate(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.And_Predicate.cache_clear()
        tup = (gparser.And_Predicate, ())
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        gparser.pretty_print(ret[2])
        gparser._set_src("")
        assert ret[:2] == (answer)
