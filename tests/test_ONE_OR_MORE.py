from packratparsergenerator.core import Core


def test_ONE_OR_MORE():
    src = "aaaaaaaa"
    c = Core()
    c._set_src(src)
    x = (c._TERMINAL, "a")
    s = c._ONE_OR_MORE(x)
    print(s)
    print(c.cache)
    assert s == True
    assert c.position == 8
    s = c._ONE_OR_MORE(x)
    assert s == False
    x = (c._TERMINAL, "b")
    c._set_src(src)
    s = c._ONE_OR_MORE(x)
    assert c.position == 0
    assert s == False
