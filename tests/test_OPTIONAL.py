from packratparsergenerator.core import Core


def test_OPTIONAL():

    src = "a"
    c = Core()
    c._set_src(src)
    x = (c._TERMINAL, "a")
    s = c._OPTIONAL((x))
    assert s == True
    assert c.position == 1
    c._set_src(src)
    x = (c._TERMINAL, "b")
    s = c._OPTIONAL((x))
    assert s == False
    assert c.position == 0
