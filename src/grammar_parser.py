from src.core_parser import Parser, Node
from functools import lru_cache as cache

class Grammar_Parser(Parser):

    @cache
    def Alphabet_Upper(self, position: int, dummy = None):
        args = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for val in range(0,len(args)-1):
            arg1, arg2 = (self._TERMINAL, args[val]), (self._TERMINAL, args[val+1])
            position, bool, node = self._ORDERED_CHOICE(position, (arg1, arg2))
            if(bool == True):
                return position, bool, node
        return position, False, None
    
    @cache
    def Alphabet_Lower(self, position: int, dummy = None):
        args = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        for val in range(0,len(args)-1):
            arg1, arg2 = (self._TERMINAL, args[val]), (self._TERMINAL, args[val+1])
            position, bool, node = self._ORDERED_CHOICE(position, (arg1, arg2))
            if(bool == True):
                return position, bool, node
        return position, False, None
    
    @cache
    def Num(self, position: int, dummy = None):
        args = ["0","1","2","3","4","5","6","7","8","9"]
        for val in range(0,len(args)-1):
            arg1, arg2 = (self._TERMINAL, args[val]), (self._TERMINAL, args[val+1])
            position, bool, node = self._ORDERED_CHOICE(position, (arg1, arg2))
            if(bool == True):
                return position, bool, node
        return position, False, None
    
    @cache
    def Spaces(self, position: int, dummy = None):
        args = ["\n","\t","\r"," "]
        for val in range(0,len(args)-1):
            arg1, arg2 = (self._TERMINAL, args[val]), (self._TERMINAL, args[val+1])
            position, bool, node = self._ORDERED_CHOICE(position, (arg1, arg2))
            if(bool == True):
                return position, bool, node
        return position, False, None
    
    @cache
    def Specials(self, position: int, dummy = None):
        args = ["+","*","-","&","!","?","<",">",'"',"(",")","_",",",",",";","=","\\","#",":","|",".","{","}","[","]"]
        for val in range(0,len(args)-1):
            arg1, arg2 = (self._TERMINAL, args[val]), (self._TERMINAL, args[val+1])
            position, bool, node = self._ORDERED_CHOICE(position, (arg1, arg2))
            if(bool == True):
                return position, bool, node
        return position, False, None

    @cache
    def ASCII(self, position: int, dummy = None):
        arg = self._token(position)
        args = [self.Alphabet_Lower, self.Alphabet_Upper, self.Num, self.Spaces, self.Specials]
        for val in range(0,len(args)-1):
            arg1, arg2 = (self._VAR_NAME, (args[val], arg)), (self._VAR_NAME, (args[val+1], arg))
            position, bool, node = self._ORDERED_CHOICE(position, (arg1, arg2))
            if(bool == True):
                return position, bool, node
        return position, False, None

    @cache 
    def Apostrophe(self, position: int, dummy = None):
        return self._TERMINAL(position, '"')
    
    @cache 
    def Left_Angle_Bracket(self, position: int, dummy = None):
        return self._TERMINAL(position, "<")
    
    @cache 
    def Right_Angle_Bracket(self, position: int, dummy = None):
        return self._TERMINAL(position, ">")
    
    @cache 
    def Left_Bracket(self, position: int, dummy = None):
        return self._TERMINAL(position, "(")
    
    @cache 
    def Right_Bracket(self, position: int, dummy = None):
        return self._TERMINAL(position, ")")
    
    @cache 
    def Assignment(self, position: int, dummy = None):
        return self._TERMINAL(position, "=")
    
    @cache 
    def End_Rule(self, position: int, dummy = None):
        return self._TERMINAL(position, ";")
    
    @cache 
    def Ampersand(self, position: int, dummy = None):
        return self._TERMINAL(position, "&")
    
    @cache 
    def Exclamation_Mark(self, position: int, dummy = None):
        return self._TERMINAL(position, "!")
    
    @cache 
    def Plus(self, position: int, dummy = None):
        return self._TERMINAL(position, "+")
    
    @cache 
    def Star(self, position: int, dummy = None):
        return self._TERMINAL(position, "*")
    
    @cache 
    def Question_Mark(self, position: int, dummy = None):
        return self._TERMINAL(position, "?")
    
    @cache 
    def Comma(self, position: int, dummy = None):
        return self._TERMINAL(position, ",")
    
    @cache 
    def Backslash(self, position: int, dummy = None):
        return self._TERMINAL(position, "/")
    
    @cache
    def Var_Name(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Left_Angle_Bracket, dummy))
        tup2 = (self._VAR_NAME, (self.Right_Angle_Bracket, dummy))

        tup3 = (self._VAR_NAME, (self.Alphabet_Lower, dummy))
        tup4 = (self._VAR_NAME, (self.Alphabet_Upper, dummy))
        tup5 = (self._TERMINAL, "_")

        tup6 = (self._ORDERED_CHOICE, (tup3, tup4)) # <Alphabet_Lower>/<Alphabet_Upper>
        tup7 = (self._ORDERED_CHOICE, (tup6, tup5)) # <Alphabet_Lower>/<Alphabet_Upper>/"_"
        
        tup8 = (self._SUBEXPR, tup6) # (<Alphabet_Lower>/<Alphabet_Upper>)
        tup9 = (self._SUBEXPR, tup7) # (<Alphabet_Lower>/<Alphabet_Upper>/"_")
        tup9 = (self._ZERO_OR_MORE, tup9) # (<Alphabet_Lower>/<Alphabet_Upper>/"_")*

        tup10 = (self._SEQUENCE, (tup1, tup8))
        tup11 = (self._SEQUENCE, (tup10, tup9))
        position, bool, node = self._SEQUENCE(position, (tup11, tup2))
        return position, bool, node
    
    @cache
    def Subexpression(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Left_Bracket, dummy))
        tup2 = (self._VAR_NAME, (self.RHS, dummy))
        tup3 = (self._VAR_NAME, (self.Right_Bracket, dummy))
        tup4 = (self._SEQUENCE, (tup1,tup2))
        position, bool, node = self._SEQUENCE(position, (tup4,tup3))
        return position, bool, node
    
    @cache
    def Terminal(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Apostrophe, dummy)) # <Apostrophe>
        tup2 = (self._VAR_NAME, (self.ASCII, dummy)) # <ASCII>
        tup4 = (self._SEQUENCE, (tup1,tup2)) # <Apostrophe>,<ASCII>
        tup5 = (self._SEQUENCE, (tup4,tup1)) # <Apostrophe>,<ASCII>, <Apostrophe>
        tup6_0 = (self._SUBEXPR, tup5) #(<Apostrophe>,<ASCII>,<Apostrophe>)
        tup2 = (self._TERMINAL, "\\") # "\"
        n = (self._TERMINAL, "n") # "n"
        r = (self._TERMINAL, "r") # "r"
        t = (self._TERMINAL, "t") # "t"
        tup3 = (self._ORDERED_CHOICE, (n,r)) # "n"/"r"
        tup4 = (self._ORDERED_CHOICE, (r,t)) # "r"/"t"
        tup5 = (self._ORDERED_CHOICE, (tup1,tup2)) # "n"/"r"/"t"
        tup6 = (self._SUBEXPR, tup3) # ("n"/"r"/"t")
        tup7 = (self._SEQUENCE,(tup1,tup2))
        tup8 = (self._SEQUENCE,(tup7,tup6))
        tup9 = (self._SEQUENCE,(tup8,tup1)) # <Apostrophe>,"\",("n"/"r"/"t"),<Apostrophe>
        tup10 = (self._SUBEXPR, tup9) # (<Apostrophe>,"\",("n"/"r"/"t"),<Apostrophe>)
        position, bool, node = self._ORDERED_CHOICE(position, (tup6_0,tup10))
        return position, bool, node

    @cache
    def Nucleus(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Subexpression, dummy))
        tup2 = (self._VAR_NAME, (self.Terminal, dummy))
        tup3 = (self._VAR_NAME, (self.Var_Name, dummy))
        tup4 = (self._VAR_NAME, (self.Whitespace, dummy))
        tup5 = (self._ORDERED_CHOICE, (tup1, tup2))
        tup6 = (self._ORDERED_CHOICE, (tup5, tup3))
        tup7 = (self._SUBEXPR, tup6)
        position, bool, node = self._SEQUENCE(position, (tup7, tup4))
        return position, bool, node

    @cache
    def Atom(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.And_Predicate, dummy))
        tup2 = (self._VAR_NAME, (self.Not_Predicate, dummy))
        tup3 = (self._VAR_NAME, (self.One_Or_More, dummy))
        tup4 = (self._VAR_NAME, (self.Zero_Or_More, dummy))
        tup5 = (self._VAR_NAME, (self.Optional, dummy))
        tup6 = (self._VAR_NAME, (self.Nucleus, dummy))
        tup7 = (self._VAR_NAME, (self.Whitespace, dummy))
        tup8 = (self._ORDERED_CHOICE, (tup1, tup2))
        tup9 = (self._ORDERED_CHOICE, (tup8, tup3))
        tup10 = (self._ORDERED_CHOICE, (tup9, tup4))
        tup11 = (self._ORDERED_CHOICE, (tup10, tup5))
        tup12 = (self._ORDERED_CHOICE, (tup11, tup6))
        tup13 = (self._SUBEXPR, tup12)
        position, bool, node = self._SEQUENCE(position, (tup13, tup7))
        return position, bool, node
    
    @cache
    def And_Predicate(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Ampersand, dummy))
        tup2 = (self._VAR_NAME, (self.Nucleus, dummy))
        position, bool, node = self._SEQUENCE(position, (tup1, tup2))
        return position, bool, node
    
    @cache
    def Not_Predicate(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Exclamation_Mark, dummy))
        tup2 = (self._VAR_NAME, (self.Nucleus, dummy))
        position, bool, node = self._SEQUENCE(position, (tup1, tup2))
        return position, bool, node

    @cache
    def Sequence(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Atom, dummy))
        tup2 = (self._VAR_NAME, (self.Whitespace, dummy))
        tup3 = (self._VAR_NAME, (self.Comma, dummy))
        
        tup4 = (self._SEQUENCE, (tup3, tup2))
        tup5 = (self._SEQUENCE, (tup4, tup1))
        tup6 = (self._SUBEXPR, tup5)
        tup7 = (self._ZERO_OR_MORE, tup6) # (<Comma>, <Whitespace>, <Atom>)*

        tup8 = (self._SEQUENCE, (tup1, tup2))
        tup9 = (self._SEQUENCE, (tup8, tup3))
        tup10 = (self._SEQUENCE, (tup9, tup2))
        tup11 = (self._SEQUENCE, (tup10, tup1))
        position, bool, node = self._SEQUENCE(position, (tup11, tup7))
        return position, bool, node

    @cache
    def Ordered_Choice(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Atom, dummy))
        tup2 = (self._VAR_NAME, (self.Whitespace, dummy))
        tup3 = (self._VAR_NAME, (self.Backslash, dummy))
        
        tup4 = (self._SEQUENCE, (tup3, tup2))
        tup5 = (self._SEQUENCE, (tup4, tup1))
        tup6 = (self._SUBEXPR, tup5)
        tup7 = (self._ZERO_OR_MORE, tup6) # (<Backslash>, <Whitespace>, <Atom>)*

        tup8 = (self._SEQUENCE, (tup1, tup2))
        tup9 = (self._SEQUENCE, (tup8, tup3))
        tup10 = (self._SEQUENCE, (tup9, tup2))
        tup11 = (self._SEQUENCE, (tup10, tup1))
        position, bool, node = self._SEQUENCE(position, (tup11, tup7))
        return position, bool, node
    
    @cache
    def One_Or_More(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Nucleus, dummy))
        tup2 = (self._VAR_NAME, (self.Whitespace, dummy))
        tup3 = (self._VAR_NAME, (self.Plus, dummy))
        tup4 = (self._SEQUENCE, (tup1, tup2))
        position, bool, node = self._SEQUENCE(position, (tup4, tup3))
        return position, bool, node
    
    @cache
    def Zero_Or_More(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Nucleus, dummy))
        tup2 = (self._VAR_NAME, (self.Whitespace, dummy))
        tup3 = (self._VAR_NAME, (self.Star, dummy))
        tup4 = (self._SEQUENCE, (tup1, tup2))
        position, bool, node = self._SEQUENCE(position, (tup4, tup3))
        return position, bool, node
    
    @cache
    def Optional(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Nucleus, dummy))
        tup2 = (self._VAR_NAME, (self.Whitespace, dummy))
        tup3 = (self._VAR_NAME, (self.Question_Mark, dummy))
        tup4 = (self._SEQUENCE, (tup1, tup2))
        position, bool, node = self._SEQUENCE(position, (tup4, tup3))
        return position, bool, node

    @cache
    def Whitespace(self, position: int, dummy = None):
        tup1 = (self._TERMINAL, " ")
        tup2 = (self._TERMINAL, "\n")
        tup3 = (self._ORDERED_CHOICE,(tup1, tup2))
        tup4 = (self._SUBEXPR, tup3)
        position, bool, node = self._ZERO_OR_MORE(position, tup4)
        return position, bool, node
    
    @cache
    def RHS(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Sequence, dummy))
        tup2 = (self._VAR_NAME, (self.Ordered_Choice, dummy))
        tup3 = (self._VAR_NAME, (self.Atom, dummy))
        tup4 = (self._ORDERED_CHOICE, (tup1, tup2))
        position, bool, node = self.Ordered_Choice(position, tup4, tup3)
        return position, bool, node
    
    @cache
    def LHS(self, position: int, dummy = None):
        position, bool, node = self._VAR_NAME(self.Var_Name, dummy)
        return position, bool, node

    @cache
    def Rule(self, position: int, dummy = None):
        arg = self._token(position)
        args = [self.LHS, self.Whitespace, self.Assignment, self.Whitespace, self.RHS, self.Whitespace, self.End_Rule, self.Whitespace]
        for val in range(0,len(args)-1):
            arg1, arg2 = (self._VAR_NAME, (args[val], arg)), (self._VAR_NAME, (args[val+1], arg))
            position, bool, node = self._ORDERED_CHOICE(position, (arg1, arg2))
            if(bool == True):
                return position, bool, node
        return position, False, None

    @cache
    def Grammar(self, position: int, dummy = None):
        tup1 = (self._VAR_NAME, (self.Rule, dummy))
        position, bool, node = self._ONE_OR_MORE(position, tup1)
        return position, bool, node
    


if __name__ == "__main__":
    #parser = Grammar_Parser()
    #parser._set_src("Z")
    #position1, bool1, node1 = parser._VAR_NAME(0, (parser.Alphabet_Upper, "Z"))
    #parser.pretty_print(node1)
    #parser._set_src("0")
    #position1, bool1, node1 = parser._VAR_NAME(0, (parser.Num, "0"))
    #parser.pretty_print(node1)
    #parser = Grammar_Parser()
    #parser._set_src("]")
    #position1, bool1, node1 = parser._VAR_NAME(0, (parser.Specials, "]"))
    #parser.pretty_print(node1)
    #parser = Grammar_Parser()
    #parser._set_src("]")
    #position1, bool1, node1 = parser._VAR_NAME(0, (parser.ASCII, "]"))
    #parser.pretty_print(node1)
    #parser = Grammar_Parser()
    #parser._set_src('"')
    #position1, bool1, node1 = parser.Apostrophe(0)
    #parser.pretty_print(node1)
    #parser = Grammar_Parser()
    #parser._set_src('<a_name>')
    #position1, bool1, node1 = parser.Var_Name(0)
    #print(position1, bool1, node1)
    #parser.pretty_print(node1)

    parser = Grammar_Parser()
    parser._set_src('<name>')
    tup = (parser.Var_Name, None)
    position1, bool1, node1 = parser._VAR_NAME(0, tup)
    print(position1, bool1, node1)
    parser.pretty_print(node1)
    parser._set_src('<yo>')
    tup = (parser.Var_Name, None)
    position1, bool1, node1 = parser._VAR_NAME(0, tup)
    print(position1, bool1, node1)
    parser.pretty_print(node1)


    
    