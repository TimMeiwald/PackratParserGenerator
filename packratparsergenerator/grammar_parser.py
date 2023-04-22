from packratparsergenerator.core import Core, cache, direct_left_recursion

class Grammar_Parser(Core):

    @cache
    def Alphabet_Upper(self,  dummy = None):
        """
        <Alphabet_Upper> = "A"/"B"/"C"/"D"/"E"/"F"/"G"/"H"/"I"/"J"/"K"/"L"/"M"/"N"/"O"/"P"/"Q"/"R"/"S"/"T"/"U"/"V"/"W"/"X"/"Y"/"Z" ;
        
        We all love commments
        """
        return self._SUBEXPRESSION((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "A"), (self._TERMINAL, "B"))), (self._TERMINAL, "C"))), (self._TERMINAL, "D"))), (self._TERMINAL, "E"))), (self._TERMINAL, "F"))), (self._TERMINAL, "G"))), (self._TERMINAL, "H"))), (self._TERMINAL, "I"))), (self._TERMINAL, "J"))), (self._TERMINAL, "K"))), (self._TERMINAL, "L"))), (self._TERMINAL, "M"))), (self._TERMINAL, "N"))), (self._TERMINAL, "O"))), (self._TERMINAL, "P"))), (self._TERMINAL, "Q"))), (self._TERMINAL, "R"))), (self._TERMINAL, "S"))), (self._TERMINAL, "T"))), (self._TERMINAL, "U"))), (self._TERMINAL, "V"))), (self._TERMINAL, "W"))), (self._TERMINAL, "X"))), (self._TERMINAL, "Y"))), (self._TERMINAL, "Z"))))

    @cache
    def Alphabet_Lower(self,  dummy = None):
        """
        <Alphabet_Lower> = "a"/"b"/"c"/"d"/"e"/"f"/"g"/"h"/"i"/"j"/"k"/"l"/"m"/"n"/"o"/"p"/"q"/"r"/"s"/"t"/"u"/"v"/"w"/"x"/"y"/"z" ;
        """
        return self._SUBEXPRESSION((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "a"), (self._TERMINAL, "b"))), (self._TERMINAL, "c"))), (self._TERMINAL, "d"))), (self._TERMINAL, "e"))), (self._TERMINAL, "f"))), (self._TERMINAL, "g"))), (self._TERMINAL, "h"))), (self._TERMINAL, "i"))), (self._TERMINAL, "j"))), (self._TERMINAL, "k"))), (self._TERMINAL, "l"))), (self._TERMINAL, "m"))), (self._TERMINAL, "n"))), (self._TERMINAL, "o"))), (self._TERMINAL, "p"))), (self._TERMINAL, "q"))), (self._TERMINAL, "r"))), (self._TERMINAL, "s"))), (self._TERMINAL, "t"))), (self._TERMINAL, "u"))), (self._TERMINAL, "v"))), (self._TERMINAL, "w"))), (self._TERMINAL, "x"))), (self._TERMINAL, "y"))), (self._TERMINAL, "z"))))

    @cache
    def Num(self,  dummy = None):
        """
        <Num> = "0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9" ;
        """
        return self._SUBEXPRESSION((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "0"), (self._TERMINAL, "1"))), (self._TERMINAL, "2"))), (self._TERMINAL, "3"))), (self._TERMINAL, "4"))), (self._TERMINAL, "5"))), (self._TERMINAL, "6"))), (self._TERMINAL, "7"))), (self._TERMINAL, "8"))), (self._TERMINAL, "9"))))

    @cache
    def Spaces(self,  dummy = None):
        """
        <Spaces> = "\n"/"\t"/"\r"/" " ;
        """
        return self._SUBEXPRESSION((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "\n"), (self._TERMINAL, "\t"))), (self._TERMINAL, "\r"))), (self._TERMINAL, " "))))

    @cache
    def Specials(self,  dummy = None):
        """
        <Specials> = "+"/"*"/"-"/"&"/"!"/"?"/"<"/">"/'"'/"("/")"/"_"/","/"/"/";"/"="/"\\"/"#"/":"/"|"/"."/"{"/"}"/"["/"]"/"%"/"'"/"^"/"~" ;
        """
        return self._SUBEXPRESSION((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "+"), (self._TERMINAL, "*"))), (self._TERMINAL, "-"))), (self._TERMINAL, "&"))), (self._TERMINAL, "!"))), (self._TERMINAL, "?"))), (self._TERMINAL, "<"))), (self._TERMINAL, ">"))), (self._TERMINAL, '"'))), (self._TERMINAL, "("))), (self._TERMINAL, ")"))), (self._TERMINAL, "_"))), (self._TERMINAL, ","))), (self._TERMINAL, "/"))), (self._TERMINAL, ";"))), (self._TERMINAL, "="))), (self._TERMINAL, '\\'))), (self._TERMINAL, "#"))), (self._TERMINAL, ":"))), (self._TERMINAL, "|"))), (self._TERMINAL, "."))), (self._TERMINAL, "{"))), (self._TERMINAL, "}"))), (self._TERMINAL, "["))), (self._TERMINAL, "]"))), (self._TERMINAL, "%"))), (self._TERMINAL, "'"))), (self._TERMINAL, "^"))), (self._TERMINAL, "~"))))

    @cache
    def ASCII(self,  dummy = None):
        """
        <ASCII> = <Alphabet_Lower>/<Alphabet_Upper>/<Num>/<Spaces>/<Specials> ;
        """
        return self._SUBEXPRESSION((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Alphabet_Lower, None)), (self._VAR_NAME, (self.Alphabet_Upper, None)))), (self._VAR_NAME, (self.Num, None)))), (self._VAR_NAME, (self.Spaces, None)))), (self._VAR_NAME, (self.Specials, None)))))

    @cache
    def Apostrophe(self,  dummy = None):
        """
        <Apostrophe> = '"' ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, '"'))

    @cache
    def Left_Angle_Bracket(self,  dummy = None):
        """
        <Left_Angle_Bracket> = "<" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, "<"))

    @cache
    def Right_Angle_Bracket(self,  dummy = None):
        """
        <Right_Angle_Bracket> = ">" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, ">"))

    @cache
    def Left_Bracket(self,  dummy = None):
        """
        <Left_Bracket> = "(" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, "("))

    @cache
    def Right_Bracket(self,  dummy = None):
        """
        <Right_Bracket> = ")" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, ")"))

    @cache
    def Assignment(self,  dummy = None):
        """
        <Assignment> = "=" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, "="))

    @cache
    def End_Rule(self,  dummy = None):
        """
        <End_Rule> = ";" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, ";"))

    @cache
    def Ampersand(self,  dummy = None):
        """
        <Ampersand> = "&" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, "&"))

    @cache
    def Exclamation_Mark(self,  dummy = None):
        """
        <Exclamation_Mark> = "!" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, "!"))

    @cache
    def Plus(self,  dummy = None):
        """
        <Plus> = "+" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, "+"))

    @cache
    def Star(self,  dummy = None):
        """
        <Star> = "*" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, "*"))

    @cache
    def Question_Mark(self,  dummy = None):
        """
        <Question_Mark> = "?" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, "?"))

    @cache
    def Comma(self,  dummy = None):
        """
        <Comma> = "," ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, ","))

    @cache
    def Backslash(self,  dummy = None):
        """
        <Backslash> = "/" ;
        """
        return self._SUBEXPRESSION((self._TERMINAL, "/"))

    @cache
    def Var_Name(self,  dummy = None):
        """
        <Var_Name> = <Left_Angle_Bracket>, (<Alphabet_Lower>/<Alphabet_Upper>), (<Alphabet_Lower>/<Alphabet_Upper>/"_")*, <Right_Angle_Bracket> ;
        
        Not whitespace dependent, feel free to use multiple lines for readability
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Left_Angle_Bracket, None)), (self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Alphabet_Lower, None)), (self._VAR_NAME, (self.Alphabet_Upper, None))))))), (self._ZERO_OR_MORE, (self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Alphabet_Lower, None)), (self._VAR_NAME, (self.Alphabet_Upper, None)))), (self._TERMINAL, "_"))))))), (self._VAR_NAME, (self.Right_Angle_Bracket, None)))))

    @cache
    def Subexpression(self,  dummy = None):
        """
        <Subexpression> = <Left_Bracket>, <RHS>, <Right_Bracket> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Left_Bracket, None)), (self._VAR_NAME, (self.RHS, None)))), (self._VAR_NAME, (self.Right_Bracket, None)))))

    @cache
    def Epsilon(self,  dummy = None):
        """
        <Epsilon> = <Apostrophe>, <Apostrophe> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._VAR_NAME, (self.Apostrophe, None)), (self._VAR_NAME, (self.Apostrophe, None)))))

    @cache
    def Terminal(self,  dummy = None):
        """
        <Terminal> = (<Apostrophe>, <ASCII>, <Apostrophe>)/(<Apostrophe>, "\\", ("n"/"r"/"t"), <Apostrophe>)/<Epsilon> ;
        """
        return self._SUBEXPRESSION((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._SUBEXPRESSION, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Apostrophe, None)), (self._VAR_NAME, (self.ASCII, None)))), (self._VAR_NAME, (self.Apostrophe, None))))), (self._SUBEXPRESSION, (self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Apostrophe, None)), (self._TERMINAL, '\\'))), (self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._TERMINAL, "n"), (self._TERMINAL, "r"))), (self._TERMINAL, "t")))))), (self._VAR_NAME, (self.Apostrophe, None))))))), (self._VAR_NAME, (self.Epsilon, None)))))

    @cache
    def Nucleus(self,  dummy = None):
        """
        <Nucleus> = (<Subexpression>/<Terminal>/<Var_Name>), <Whitespace> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Subexpression, None)), (self._VAR_NAME, (self.Terminal, None)))), (self._VAR_NAME, (self.Var_Name, None))))), (self._VAR_NAME, (self.Whitespace, None)))))

    @cache
    def Atom(self,  dummy = None):
        """
        <Atom> = (<And_Predicate>/<Not_Predicate>/<One_Or_More>/<Zero_Or_More>/<Optional>/<Nucleus>), <Whitespace> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.And_Predicate, None)), (self._VAR_NAME, (self.Not_Predicate, None)))), (self._VAR_NAME, (self.One_Or_More, None)))), (self._VAR_NAME, (self.Zero_Or_More, None)))), (self._VAR_NAME, (self.Optional, None)))), (self._VAR_NAME, (self.Nucleus, None))))), (self._VAR_NAME, (self.Whitespace, None)))))

    @cache
    def And_Predicate(self,  dummy = None):
        """
        <And_Predicate> = <Ampersand>, <Nucleus> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._VAR_NAME, (self.Ampersand, None)), (self._VAR_NAME, (self.Nucleus, None)))))

    @cache
    def Not_Predicate(self,  dummy = None):
        """
        <Not_Predicate> = <Exclamation_Mark>, <Nucleus> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._VAR_NAME, (self.Exclamation_Mark, None)), (self._VAR_NAME, (self.Nucleus, None)))))

    @cache
    def Sequence(self,  dummy = None):
        """
        <Sequence> = <Atom>, <Whitespace>, <Comma>, <Whitespace>, <Atom>, (<Comma>, <Whitespace>, <Atom>)* ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Atom, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Comma, None)))), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Atom, None)))), (self._ZERO_OR_MORE, (self._SUBEXPRESSION, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Comma, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Atom, None)))))))))

    @cache
    def Ordered_Choice(self,  dummy = None):
        """
        <Ordered_Choice> = <Atom>, <Whitespace>, <Backslash>, <Whitespace>, <Atom>, (<Backslash>, <Whitespace>, <Atom>)* ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Atom, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Backslash, None)))), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Atom, None)))), (self._ZERO_OR_MORE, (self._SUBEXPRESSION, (self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Backslash, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Atom, None)))))))))

    @cache
    def One_Or_More(self,  dummy = None):
        """
        <One_Or_More> = <Nucleus>, <Whitespace>, <Plus> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Nucleus, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Plus, None)))))

    @cache
    def Zero_Or_More(self,  dummy = None):
        """
        <Zero_Or_More> = <Nucleus>, <Whitespace>, <Star> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Nucleus, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Star, None)))))

    @cache
    def Optional(self,  dummy = None):
        """
        <Optional> = <Nucleus>, <Whitespace>, <Question_Mark> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Nucleus, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Question_Mark, None)))))

    @cache
    def Whitespace(self,  dummy = None):
        """
        <Whitespace> = (" "/"\n")* ;
        """
        return self._SUBEXPRESSION((self._ZERO_OR_MORE, (self._SUBEXPRESSION, (self._ORDERED_CHOICE, ((self._TERMINAL, " "), (self._TERMINAL, "\n"))))))

    @cache
    def RHS(self,  dummy = None):
        """
        <RHS> = <Sequence>/<Ordered_Choice>/<Atom> ;
        """
        return self._SUBEXPRESSION((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Sequence, None)), (self._VAR_NAME, (self.Ordered_Choice, None)))), (self._VAR_NAME, (self.Atom, None)))))

    @cache
    def LHS(self,  dummy = None):
        """
        <LHS> = <Var_Name>, (<Whitespace>, <Semantic_Instructions>, <Whitespace>)? ;

        """
        bool = self.Var_Name()
        self.Whitespace()
        self._OPTIONAL((self.Semantic_Instructions, None))
        self.Whitespace()
        return bool
    
    @cache
    def Rule(self,  dummy = None):
        """
        <Rule> = <LHS>, <Whitespace>, <Assignment>, <Whitespace>, <RHS>, <Whitespace>, <End_Rule>, <Whitespace>, <Comment>* ;
        """   

        bool = self.LHS()
        if(bool):
            #print("LHS")
            bool = self.Whitespace()
            if(bool):
                #print("Whitespace")
                bool = self.Assignment()
                if(bool):
                    #print("Assignment")
                    bool = self.Whitespace()
                    if(bool):
                        #print("Whitespace")
                        bool = self.RHS()
                        if(bool):
                            #print("RHS")
                            bool = self.Whitespace()
                            if(bool):
                                #print("Whitespace")
                                bool = self.End_Rule()
                                if(bool):
                                    #print("End Rule")
                                    self.Whitespace()
                                    bool = self._ZERO_OR_MORE((self.Comment, None))
                                    return True
                                else: 
                                    raise Exception("Missing ;")
        return False


        #return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.LHS, None)), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.Assignment, None)))), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.RHS, None)))), (self._VAR_NAME, (self.Whitespace, None)))), (self._VAR_NAME, (self.End_Rule, None)))), (self._VAR_NAME, (self.Whitespace, None)))), None)))

    @cache
    def Grammar(self,  dummy = None):
        """
        <Grammar> = <Rule>+, <Whitespace> ;
        
        Double up dem comments
        """
        bool = self._SUBEXPRESSION((self._SEQUENCE, ((self._ONE_OR_MORE, (self._VAR_NAME, (self.Rule, None))), (self._VAR_NAME, (self.Whitespace, None)))))
        print("Finished Grammar")
        return bool

    @cache
    def Comment(self,  dummy = None):
        """
        <Comment> = <Whitespace>, "#", (!"#", <ASCII>)*, "#", <Whitespace> ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._VAR_NAME, (self.Whitespace, None)), (self._TERMINAL, "#"))), (self._ZERO_OR_MORE, (self._SUBEXPRESSION, (self._SEQUENCE, ((self._NOT_PREDICATE, (self._TERMINAL, "#")), (self._VAR_NAME, (self.ASCII, None)))))))), (self._TERMINAL, "#"))), (self._VAR_NAME, (self.Whitespace, None)))))

    @cache
    def Semantic_Instructions(self,  dummy = None):
        """
        <Semantic_Instructions> = <Delete>/<Passthrough>/<Collect> ;
        """
        return self._SUBEXPRESSION((self._ORDERED_CHOICE, ((self._ORDERED_CHOICE, ((self._VAR_NAME, (self.Delete, None)), (self._VAR_NAME, (self.Passthrough, None)))), (self._VAR_NAME, (self.Collect, None)))))

    @cache
    def Delete(self,  dummy = None):
        """
        <Delete> = "D", "E", "L", "E", "T", "E" ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._TERMINAL, "D"), (self._TERMINAL, "E"))), (self._TERMINAL, "L"))), (self._TERMINAL, "E"))), (self._TERMINAL, "T"))), (self._TERMINAL, "E"))))

    @cache
    def Passthrough(self,  dummy = None):
        """
        <Passthrough> = "P", "A", "S", "S", "T", "H", "R", "O", "U", "G", "H" ;
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._TERMINAL, "P"), (self._TERMINAL, "A"))), (self._TERMINAL, "S"))), (self._TERMINAL, "S"))), (self._TERMINAL, "T"))), (self._TERMINAL, "H"))), (self._TERMINAL, "R"))), (self._TERMINAL, "O"))), (self._TERMINAL, "U"))), (self._TERMINAL, "G"))), (self._TERMINAL, "H"))))

    @cache
    def Collect(self,  dummy = None):
        """
        <Collect> = "C", "O", "L", "L", "E", "C", "T" ;
        
        Comment
        """
        return self._SUBEXPRESSION((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._SEQUENCE, ((self._TERMINAL, "C"), (self._TERMINAL, "O"))), (self._TERMINAL, "L"))), (self._TERMINAL, "L"))), (self._TERMINAL, "E"))), (self._TERMINAL, "C"))), (self._TERMINAL, "T"))))
    
    @direct_left_recursion 
    def many_A(self, dummy = None):
        """Left recursive test"""
        return self._SEQUENCE(((self.many_A, dummy),(self._TERMINAL, "a")))


if __name__ == "__main__":

    
    # src =  "<LHS> = <Var_Name>, (<Whitespace>, <Semantic_Instructions>,<Whitespace>)?;"
    # c = Grammar_Parser()
    # c._set_src(src)
    # print(c.Var_Name())
    # print(c.Whitespace())
    # print(c.Assignment())
    # print(c.Whitespace())
    # print(c.RHS())
    # print(c.Whitespace())
    # print(c.Comment())
    # assert len(src) == c.position+1, f"Source Length {len(src)}, Position: {c.position}"

    # src =  "<LHS> = <Var_Name>, (<Whitespace>, <Semantic_Instructions>,<Whitespace>)?;"
    # c = Grammar_Parser()
    # c._set_src(src)
    # c.Grammar()
    # assert len(src) == c.position, f"Source Length {len(src)}, Position: {c.position}"

    # src = '<Num> PASSTHROUGH = "0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9";'
    # c = Grammar_Parser()
    # c._set_src(src)
    # c.Grammar()
    # assert len(src) == c.position, f"Source Length {len(src)}, Position: {c.position}"

    # from os import getcwd
    # from os.path import join
    # with open(join(getcwd(), "packratparsergenerator", "Grammar.txt"), "r") as fp:
    #     src = fp.read()
    # c = Grammar_Parser()
    # c._set_src(src)
    # c.Grammar()
    # assert len(src) == c.position, f"Source Length {len(src)}, Position: {c.position}"



    src = 'aaaabaa'
    c = Grammar_Parser()
    c._set_src(src)
    b = c.many_A(None)
    print(c.position, b)
    assert 4 == c.position, f"Source Position {3}, Position: {c.position}"
    assert b == True

    src = 'aaaaaa'
    c = Grammar_Parser()
    c._set_src(src)
    b = c.many_A(None)
    print(c.position, b)
    assert len(src) == c.position, f"Source Length {len(src)}, Position: {c.position}"
    assert b == True