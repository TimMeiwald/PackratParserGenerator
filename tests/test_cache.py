from packratparsergenerator.cache import Cache
from packratparsergenerator.core import Core


def test_cache():
    c = Cache()
    c.set(test_cache.__name__, 0, "blah blah", False)
    assert c.get(test_cache.__name__, 0, "blah blah") == False


def test_TERMINAL():

    s = "b"
    c = Core()
    c._set_src(s)
    assert c._TERMINAL("a") == False
    c._set_src(s)
    assert c._TERMINAL("b") == True
    print(c.cache)
