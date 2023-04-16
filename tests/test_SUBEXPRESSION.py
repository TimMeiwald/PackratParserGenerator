from packratparsergenerator.core import Core


def test_SEQUENCE():

    s = "ab"
    c = Core()
    c._set_src(s)
    x = (c._TERMINAL, "a")
    y = (c._TERMINAL, "b")
    z = (c._SEQUENCE, (x, y))
    s = c._SUBEXPRESSION(z)
    assert s == True
    assert c.position == 2
