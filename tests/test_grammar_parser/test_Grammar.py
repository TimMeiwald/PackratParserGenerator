import pytest
from os import getcwd
from os.path import join
class Test_Grammar():
    
    def test_Grammar(self, gparser):
        path = join(getcwd(), "src", "Grammar.txt")
        with open(path, "r") as fp:
            src = fp.read()
        print(f"Length of File is : {len(src)}")
        gparser._set_src(src)
        gparser.Grammar.cache_clear()
        tup = (gparser.Grammar, None)
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        #gparser.pretty_print(ret[2])
        answer = (len(src), True)
        failure = src[ret[0]:]
        print(failure)
        assert ret[:2] == (answer)