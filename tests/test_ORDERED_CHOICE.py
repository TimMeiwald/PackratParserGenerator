from packratparsergenerator.core import Core


def test_ORDERED_CHOICE():

    src = "a"
    c = Core()
    c._set_src(src)
    x = (c._TERMINAL, "a")
    y = (c._TERMINAL, "b")
    s = c._ORDERED_CHOICE((x, y))
    assert s == True
    c._set_src(src)
    s = c._ORDERED_CHOICE((x, y))
    assert s == True
