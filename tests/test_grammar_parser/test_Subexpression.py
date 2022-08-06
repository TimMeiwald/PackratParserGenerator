import pytest

class Test_Subexpression():
    
    @pytest.mark.parametrize("src, answer", [('0' ,(0, False)), 
        ("ABC", (0, False)), 
        ('001',  (0, False)),
        ('<A>',  (0, False)),
        ("<This_is_a_name>", (0, False)), 
        ("<name>", (0, False)), 
        ('001',  (0, False)),
        ("9", (0, False)),
        ('("A")',  (5, True)),
        ("(<a>)", (5, True)),
        ('("A"',  (0, False)),
        ("'A')", (0, False)),
        ])
    def test_Subexpression(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.Subexpression.cache_clear()
        tup = (gparser.Subexpression, None)
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        assert ret[:2] == (answer)