from packratparsergenerator.core import Core


def test_TERMINAL():

    s = "a"
    c = Core()
    c._set_src(s)
    assert c._TERMINAL("a") == True
    assert c.position == 1
    print("\n", c.cache)

    c._set_src(s)
    assert c._TERMINAL("b") == False
    assert c.position == 0
    print("\n", c.cache)
