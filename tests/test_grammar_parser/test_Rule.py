import pytest



class Test_Rule():
    @pytest.mark.parametrize("src, answer", [('<hey> = "A";' ,True),
    ('<hey> = "A";' ,True),
    ('<Right_Bracket> = ")";', True),
    ('<Specials> = "+"/"*"/"-"/"&"/"!"/"?"/"<"/">"/"""/"("/")"/"_"/","/"/"/";"/"="/"\\"/"#"/":"/"|"/"."/"{"/"}"/"["/"]";', True),
    ('<Exclamation_Mark> = "!";\n  \n', True),
    ('<Var_Name> =<Left_Angle_Bracket>,(<Alphabet_Lower>/<Alphabet_Upper>),(<Alphabet_Lower>/<Alphabet_Upper>/"_")*,<Right_Angle_Bracket>;', True),
    ('<Whitespace> = (" "/"\n")*;', True),
    ('<One_Or_More> = <Nucleus>, <Whitespace>, <Plus>;', True),
    ('<Terminal> =(<Apostrophe>,<ASCII>,<Apostrophe>)/(<Apostrophe>,"\\",("n"/"r"/"t"),<Apostrophe>);', True),
    ('<Grammar> = <Rule>+, <Whitespace>;', True),
    ('<Rule> = <LHS>, <Whitespace>, <Assignment>, <Whitespace>, <RHS>, <Whitespace>, <End_Rule>, <Whitespace>;', True),
    ('<Atom> = (<And_Predicate>/<Not_Predicate>/<One_Or_More>/<Zero_Or_More>/<Optional>/<Nucleus>), <Whitespace>;', True),
    ('<Spaces> = "\n"/"\t"/"\r"/" ";', True)
    ])
    def test_Rule(self, gparser, src, answer):
        gparser._set_src(src)
        gparser.Rule.cache_clear()
        tup = (gparser.Rule, None)
        # Needs to be called from _VAR_NAME so that 
        # rule_name gets added to dict so that cache gets cleared correctly
        # not needed on core parser tests because they're statically defined and always get cleared with _set_src
        ret = gparser._VAR_NAME(0, tup) 
        #gparser.pretty_print(ret[2])
        #print(f"Position: {ret[0]}, Bool: {ret[1]}")
        gparser._set_src("")
        answer = (len(src), answer)
        assert ret[:2] == (answer)
