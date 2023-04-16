from packratparsergenerator.core import Core


def test_SEQUENCE():

    s = "ab"
    c = Core()
    c._set_src(s)
    x = (c._TERMINAL, "a")
    y = (c._TERMINAL, "b")
    s = c._SEQUENCE((x, y))
    print(s)
    print(c.cache)
    assert s == True
