from packratparsergenerator.core import Core


def test_AND_PREDICATE_true():
    src = "aaaaaaaa"
    c = Core()
    c._set_src(src)
    x = (c._TERMINAL, "a")
    s = c._AND_PREDICATE(x)
    assert s == True
    assert c.position == 0


def test_AND_PREDICATE_false():
    src = "aaaaaaaa"
    c = Core()
    c._set_src(src)
    x = (c._TERMINAL, "b")
    s = c._AND_PREDICATE(x)
    assert s == False
    assert c.position == 0
