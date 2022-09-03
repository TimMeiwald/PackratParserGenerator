from packratparsergenerator.parser.core_parser import Parser, Node, Rules
from functools import lru_cache as cache


class Grammar_Parser(Parser):

    def _set_src(self, src: str):
        super()._set_src(src)
        for rule in Rules:
            if (rule >= 20):  # Less than 20 is core parser stuff, greatereq than 20 is inherited class stuff
                func = getattr(self, rule.name)
                func.cache_clear()

    @cache
    def Alphabet_Upper(self, position: int, dummy=None):
        """ <Alphabet_Upper> = "A"/"B"/"C"/"D"/"E"/"F"/"G"/"H"/"I"/"J"/"K"/"L"/"M"/"N"/"O"/"P"/"Q"/"R"/"S"/"T"/"U"/"V"/"W"/"X"/"Y"/"Z" ; """
        return self._SUBEXPRESSION(
            position,
            (self._ORDERED_CHOICE,
             ((self._ORDERED_CHOICE,
               ((self._ORDERED_CHOICE,
                 ((self._ORDERED_CHOICE,
                   ((self._ORDERED_CHOICE,
                     ((self._ORDERED_CHOICE,
                       ((self._ORDERED_CHOICE,
                         ((self._ORDERED_CHOICE,
                           ((self._ORDERED_CHOICE,
                             ((self._ORDERED_CHOICE,
                               ((self._ORDERED_CHOICE,
                                 ((self._ORDERED_CHOICE,
                                   ((self._ORDERED_CHOICE,
                                     ((self._ORDERED_CHOICE,
                                       ((self._ORDERED_CHOICE,
                                         ((self._ORDERED_CHOICE,
                                           ((self._ORDERED_CHOICE,
                                             ((self._ORDERED_CHOICE,
                                               ((self._ORDERED_CHOICE,
                                                 ((self._ORDERED_CHOICE,
                                                   ((self._ORDERED_CHOICE,
                                                     ((self._ORDERED_CHOICE,
                                                       ((self._ORDERED_CHOICE,
                                                         ((self._ORDERED_CHOICE,
                                                           ((self._ORDERED_CHOICE,
                                                             ((self._TERMINAL,
                                                               "A"),
                                                              (self._TERMINAL,
                                                                 "B"))),
                                                               (self._TERMINAL,
                                                                "C"))),
                                                             (self._TERMINAL,
                                                              "D"))),
                                                           (self._TERMINAL,
                                                            "E"))),
                                                         (self._TERMINAL,
                                                          "F"))),
                                                       (self._TERMINAL,
                                                        "G"))),
                                                     (self._TERMINAL,
                                                      "H"))),
                                                   (self._TERMINAL,
                                                    "I"))),
                                                 (self._TERMINAL,
                                                  "J"))),
                                               (self._TERMINAL,
                                                "K"))),
                                             (self._TERMINAL,
                                              "L"))),
                                           (self._TERMINAL,
                                            "M"))),
                                         (self._TERMINAL,
                                          "N"))),
                                       (self._TERMINAL,
                                        "O"))),
                                     (self._TERMINAL,
                                      "P"))),
                                   (self._TERMINAL,
                                    "Q"))),
                                 (self._TERMINAL,
                                  "R"))),
                               (self._TERMINAL,
                                "S"))),
                             (self._TERMINAL,
                              "T"))),
                           (self._TERMINAL,
                            "U"))),
                         (self._TERMINAL,
                          "V"))),
                       (self._TERMINAL,
                        "W"))),
                     (self._TERMINAL,
                      "X"))),
                   (self._TERMINAL,
                    "Y"))),
                 (self._TERMINAL,
                  "Z"))))

    @cache
    def Alphabet_Lower(self, position: int, dummy=None):
        """ <Alphabet_Lower> = "a"/"b"/"c"/"d"/"e"/"f"/"g"/"h"/"i"/"j"/"k"/"l"/"m"/"n"/"o"/"p"/"q"/"r"/"s"/"t"/"u"/"v"/"w"/"x"/"y"/"z" ; """
        return self._SUBEXPRESSION(
            position,
            (self._ORDERED_CHOICE,
             ((self._ORDERED_CHOICE,
               ((self._ORDERED_CHOICE,
                 ((self._ORDERED_CHOICE,
                   ((self._ORDERED_CHOICE,
                     ((self._ORDERED_CHOICE,
                       ((self._ORDERED_CHOICE,
                         ((self._ORDERED_CHOICE,
                           ((self._ORDERED_CHOICE,
                             ((self._ORDERED_CHOICE,
                               ((self._ORDERED_CHOICE,
                                 ((self._ORDERED_CHOICE,
                                   ((self._ORDERED_CHOICE,
                                     ((self._ORDERED_CHOICE,
                                       ((self._ORDERED_CHOICE,
                                         ((self._ORDERED_CHOICE,
                                           ((self._ORDERED_CHOICE,
                                             ((self._ORDERED_CHOICE,
                                               ((self._ORDERED_CHOICE,
                                                 ((self._ORDERED_CHOICE,
                                                   ((self._ORDERED_CHOICE,
                                                     ((self._ORDERED_CHOICE,
                                                       ((self._ORDERED_CHOICE,
                                                         ((self._ORDERED_CHOICE,
                                                           ((self._ORDERED_CHOICE,
                                                             ((self._TERMINAL,
                                                               "a"),
                                                              (self._TERMINAL,
                                                                 "b"))),
                                                               (self._TERMINAL,
                                                                "c"))),
                                                             (self._TERMINAL,
                                                              "d"))),
                                                           (self._TERMINAL,
                                                            "e"))),
                                                         (self._TERMINAL,
                                                          "f"))),
                                                       (self._TERMINAL,
                                                        "g"))),
                                                     (self._TERMINAL,
                                                      "h"))),
                                                   (self._TERMINAL,
                                                    "i"))),
                                                 (self._TERMINAL,
                                                  "j"))),
                                               (self._TERMINAL,
                                                "k"))),
                                             (self._TERMINAL,
                                              "l"))),
                                           (self._TERMINAL,
                                            "m"))),
                                         (self._TERMINAL,
                                          "n"))),
                                       (self._TERMINAL,
                                        "o"))),
                                     (self._TERMINAL,
                                      "p"))),
                                   (self._TERMINAL,
                                    "q"))),
                                 (self._TERMINAL,
                                  "r"))),
                               (self._TERMINAL,
                                "s"))),
                             (self._TERMINAL,
                              "t"))),
                           (self._TERMINAL,
                            "u"))),
                         (self._TERMINAL,
                          "v"))),
                       (self._TERMINAL,
                        "w"))),
                     (self._TERMINAL,
                      "x"))),
                   (self._TERMINAL,
                    "y"))),
                 (self._TERMINAL,
                  "z"))))

    @cache
    def Num(self, position: int, dummy=None):
        """ <Num> = "0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9" ; """
        return self._SUBEXPRESSION(
            position,
            (self._ORDERED_CHOICE,
             ((self._ORDERED_CHOICE,
               ((self._ORDERED_CHOICE,
                 ((self._ORDERED_CHOICE,
                   ((self._ORDERED_CHOICE,
                     ((self._ORDERED_CHOICE,
                       ((self._ORDERED_CHOICE,
                         ((self._ORDERED_CHOICE,
                           ((self._ORDERED_CHOICE,
                             ((self._TERMINAL,
                               "0"),
                              (self._TERMINAL,
                                 "1"))),
                               (self._TERMINAL,
                                "2"))),
                             (self._TERMINAL,
                              "3"))),
                           (self._TERMINAL,
                            "4"))),
                         (self._TERMINAL,
                          "5"))),
                       (self._TERMINAL,
                        "6"))),
                     (self._TERMINAL,
                      "7"))),
                   (self._TERMINAL,
                    "8"))),
                 (self._TERMINAL,
                  "9"))))

    @cache
    def Spaces(self, position: int, dummy=None):
        """ <Spaces> = "\n"/"\t"/"\r"/" " ; """
        return self._SUBEXPRESSION(
            position,
            (self._ORDERED_CHOICE,
             ((self._ORDERED_CHOICE,
               ((self._ORDERED_CHOICE,
                 ((self._TERMINAL,
                   "\n"),
                  (self._TERMINAL,
                     "\t"))),
                   (self._TERMINAL,
                    "\r"))),
                 (self._TERMINAL,
                  " "))))

    @cache
    def Specials(self, position: int, dummy=None):
        """ <Specials> = "+"/"*"/"-"/"&"/"!"/"?"/"<"/">"/'"'/"("/")"/"_"/","/"/"/";"/"="/"\\"/"#"/":"/"|"/"."/"{"/"}"/"["/"]" ; """
        return self._SUBEXPRESSION(
            position,
            (self._ORDERED_CHOICE,
             ((self._ORDERED_CHOICE,
               ((self._ORDERED_CHOICE,
                 ((self._ORDERED_CHOICE,
                   ((self._ORDERED_CHOICE,
                     ((self._ORDERED_CHOICE,
                       ((self._ORDERED_CHOICE,
                         ((self._ORDERED_CHOICE,
                           ((self._ORDERED_CHOICE,
                             ((self._ORDERED_CHOICE,
                               ((self._ORDERED_CHOICE,
                                 ((self._ORDERED_CHOICE,
                                   ((self._ORDERED_CHOICE,
                                     ((self._ORDERED_CHOICE,
                                       ((self._ORDERED_CHOICE,
                                         ((self._ORDERED_CHOICE,
                                           ((self._ORDERED_CHOICE,
                                             ((self._ORDERED_CHOICE,
                                               ((self._ORDERED_CHOICE,
                                                 ((self._ORDERED_CHOICE,
                                                   ((self._ORDERED_CHOICE,
                                                     ((self._ORDERED_CHOICE,
                                                       ((self._ORDERED_CHOICE,
                                                         ((self._ORDERED_CHOICE,
                                                           ((self._TERMINAL,
                                                             "+"),
                                                            (self._TERMINAL,
                                                               "*"))),
                                                             (self._TERMINAL,
                                                              "-"))),
                                                           (self._TERMINAL,
                                                            "&"))),
                                                         (self._TERMINAL,
                                                          "!"))),
                                                       (self._TERMINAL,
                                                        "?"))),
                                                     (self._TERMINAL,
                                                      "<"))),
                                                   (self._TERMINAL,
                                                    ">"))),
                                                 (self._TERMINAL,
                                                  '"'))),
                                               (self._TERMINAL,
                                                "("))),
                                             (self._TERMINAL,
                                              ")"))),
                                           (self._TERMINAL,
                                            "_"))),
                                         (self._TERMINAL,
                                          ","))),
                                       (self._TERMINAL,
                                        "/"))),
                                     (self._TERMINAL,
                                      ";"))),
                                   (self._TERMINAL,
                                    "="))),
                                 (self._TERMINAL,
                                  '\\'))),
                               (self._TERMINAL,
                                "#"))),
                             (self._TERMINAL,
                              ":"))),
                           (self._TERMINAL,
                            "|"))),
                         (self._TERMINAL,
                          "."))),
                       (self._TERMINAL,
                        "{"))),
                     (self._TERMINAL,
                      "}"))),
                   (self._TERMINAL,
                    "["))),
                 (self._TERMINAL,
                  "]"))))

    @cache
    def ASCII(self, position: int, dummy=None):
        """ <ASCII> = <Alphabet_Lower>/<Alphabet_Upper>/<Num>/<Spaces>/<Specials> ; """
        return self._SUBEXPRESSION(
            position,
            (self._ORDERED_CHOICE,
             ((self._ORDERED_CHOICE,
               ((self._ORDERED_CHOICE,
                 ((self._ORDERED_CHOICE,
                   ((self._VAR_NAME,
                     (self.Alphabet_Lower,
                      None)),
                       (self._VAR_NAME,
                        (self.Alphabet_Upper,
                         None)))),
                     (self._VAR_NAME,
                      (self.Num,
                       None)))),
                   (self._VAR_NAME,
                    (self.Spaces,
                     None)))),
                 (self._VAR_NAME,
                  (self.Specials,
                   None)))))

    @cache
    def Apostrophe(self, position: int, dummy=None):
        """ <Apostrophe> = '"' ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, '"'))

    @cache
    def Left_Angle_Bracket(self, position: int, dummy=None):
        """ <Left_Angle_Bracket> = "<" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "<"))

    @cache
    def Right_Angle_Bracket(self, position: int, dummy=None):
        """ <Right_Angle_Bracket> = ">" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, ">"))

    @cache
    def Left_Bracket(self, position: int, dummy=None):
        """ <Left_Bracket> = "(" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "("))

    @cache
    def Right_Bracket(self, position: int, dummy=None):
        """ <Right_Bracket> = ")" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, ")"))

    @cache
    def Assignment(self, position: int, dummy=None):
        """ <Assignment> = "=" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "="))

    @cache
    def End_Rule(self, position: int, dummy=None):
        """ <End_Rule> = ";" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, ";"))

    @cache
    def Ampersand(self, position: int, dummy=None):
        """ <Ampersand> = "&" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "&"))

    @cache
    def Exclamation_Mark(self, position: int, dummy=None):
        """ <Exclamation_Mark> = "!" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "!"))

    @cache
    def Plus(self, position: int, dummy=None):
        """ <Plus> = "+" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "+"))

    @cache
    def Star(self, position: int, dummy=None):
        """ <Star> = "*" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "*"))

    @cache
    def Question_Mark(self, position: int, dummy=None):
        """ <Question_Mark> = "?" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "?"))

    @cache
    def Comma(self, position: int, dummy=None):
        """ <Comma> = "," ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, ","))

    @cache
    def Backslash(self, position: int, dummy=None):
        """ <Backslash> = "/" ; """
        return self._SUBEXPRESSION(position, (self._TERMINAL, "/"))

    @cache
    def Var_Name(self, position: int, dummy=None):
        """ <Var_Name> = <Left_Angle_Bracket>, (<Alphabet_Lower>/<Alphabet_Upper>), (<Alphabet_Lower>/<Alphabet_Upper>/"_")*, <Right_Angle_Bracket> ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._SEQUENCE,
                 ((self._VAR_NAME,
                   (self.Left_Angle_Bracket,
                    None)),
                     (self._SUBEXPRESSION,
                      (self._ORDERED_CHOICE,
                       ((self._VAR_NAME,
                        (self.Alphabet_Lower,
                         None)),
                        (self._VAR_NAME,
                           (self.Alphabet_Upper,
                            None))))))),
                   (self._ZERO_OR_MORE,
                    (self._SUBEXPRESSION,
                     (self._ORDERED_CHOICE,
                      ((self._ORDERED_CHOICE,
                       ((self._VAR_NAME,
                         (self.Alphabet_Lower,
                          None)),
                           (self._VAR_NAME,
                            (self.Alphabet_Upper,
                             None)))),
                          (self._TERMINAL,
                           "_"))))))),
                 (self._VAR_NAME,
                  (self.Right_Angle_Bracket,
                   None)))))

    @cache
    def Subexpression(self, position: int, dummy=None):
        """ <Subexpression> = <Left_Bracket>, <RHS>, <Right_Bracket> ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._VAR_NAME,
                 (self.Left_Bracket,
                  None)),
                   (self._VAR_NAME,
                    (self.RHS,
                     None)))),
                 (self._VAR_NAME,
                  (self.Right_Bracket,
                   None)))))

    @cache
    def Terminal(self, position: int, dummy=None):
        """ <Terminal> = (<Apostrophe>, <ASCII>, <Apostrophe>)/(<Apostrophe>, "\\", ("n"/"r"/"t"), <Apostrophe>) ; """
        return self._SUBEXPRESSION(
            position,
            (self._ORDERED_CHOICE,
             ((self._SUBEXPRESSION,
               (self._SEQUENCE,
                ((self._SEQUENCE,
                  ((self._VAR_NAME,
                    (self.Apostrophe,
                     None)),
                      (self._VAR_NAME,
                       (self.ASCII,
                        None)))),
                    (self._VAR_NAME,
                     (self.Apostrophe,
                      None))))),
                 (self._SUBEXPRESSION,
                  (self._SEQUENCE,
                   ((self._SEQUENCE,
                     ((self._SEQUENCE,
                       ((self._VAR_NAME,
                         (self.Apostrophe,
                          None)),
                           (self._TERMINAL,
                            '\\'))),
                         (self._SUBEXPRESSION,
                          (self._ORDERED_CHOICE,
                           ((self._ORDERED_CHOICE,
                            ((self._TERMINAL,
                              "n"),
                             (self._TERMINAL,
                                "r"))),
                               (self._TERMINAL,
                                "t")))))),
                       (self._VAR_NAME,
                        (self.Apostrophe,
                         None))))))))

    @cache
    def Nucleus(self, position: int, dummy=None):
        """ <Nucleus> = (<Subexpression>/<Terminal>/<Var_Name>), <Whitespace> ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SUBEXPRESSION,
               (self._ORDERED_CHOICE,
                ((self._ORDERED_CHOICE,
                  ((self._VAR_NAME,
                    (self.Subexpression,
                     None)),
                      (self._VAR_NAME,
                       (self.Terminal,
                        None)))),
                    (self._VAR_NAME,
                     (self.Var_Name,
                      None))))),
                 (self._VAR_NAME,
                  (self.Whitespace,
                   None)))))

    @cache
    def Atom(self, position: int, dummy=None):
        """ <Atom> = (<And_Predicate>/<Not_Predicate>/<One_Or_More>/<Zero_Or_More>/<Optional>/<Nucleus>), <Whitespace> ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SUBEXPRESSION,
               (self._ORDERED_CHOICE,
                ((self._ORDERED_CHOICE,
                  ((self._ORDERED_CHOICE,
                    ((self._ORDERED_CHOICE,
                      ((self._ORDERED_CHOICE,
                        ((self._VAR_NAME,
                          (self.And_Predicate,
                           None)),
                            (self._VAR_NAME,
                             (self.Not_Predicate,
                              None)))),
                          (self._VAR_NAME,
                           (self.One_Or_More,
                            None)))),
                        (self._VAR_NAME,
                         (self.Zero_Or_More,
                          None)))),
                      (self._VAR_NAME,
                       (self.Optional,
                        None)))),
                    (self._VAR_NAME,
                     (self.Nucleus,
                      None))))),
                 (self._VAR_NAME,
                  (self.Whitespace,
                   None)))))

    @cache
    def And_Predicate(self, position: int, dummy=None):
        """ <And_Predicate> = <Ampersand>, <Nucleus> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((
            self._VAR_NAME, (self.Ampersand, None)), (self._VAR_NAME, (self.Nucleus, None)))))

    @cache
    def Not_Predicate(self, position: int, dummy=None):
        """ <Not_Predicate> = <Exclamation_Mark>, <Nucleus> ; """
        return self._SUBEXPRESSION(position, (self._SEQUENCE, ((
            self._VAR_NAME, (self.Exclamation_Mark, None)), (self._VAR_NAME, (self.Nucleus, None)))))

    @cache
    def Sequence(self, position: int, dummy=None):
        """ <Sequence> = <Atom>, <Whitespace>, <Comma>, <Whitespace>, <Atom>, (<Comma>, <Whitespace>, <Atom>)* ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._SEQUENCE,
                 ((self._SEQUENCE,
                   ((self._SEQUENCE,
                     ((self._VAR_NAME,
                       (self.Atom,
                        None)),
                         (self._VAR_NAME,
                          (self.Whitespace,
                           None)))),
                       (self._VAR_NAME,
                        (self.Comma,
                         None)))),
                     (self._VAR_NAME,
                      (self.Whitespace,
                       None)))),
                   (self._VAR_NAME,
                    (self.Atom,
                     None)))),
                 (self._ZERO_OR_MORE,
                  (self._SUBEXPRESSION,
                   (self._SEQUENCE,
                    ((self._SEQUENCE,
                      ((self._VAR_NAME,
                        (self.Comma,
                         None)),
                          (self._VAR_NAME,
                           (self.Whitespace,
                            None)))),
                        (self._VAR_NAME,
                         (self.Atom,
                          None)))))))))

    @cache
    def Ordered_Choice(self, position: int, dummy=None):
        """ <Ordered_Choice> = <Atom>, <Whitespace>, <Backslash>, <Whitespace>, <Atom>, (<Backslash>, <Whitespace>, <Atom>)* ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._SEQUENCE,
                 ((self._SEQUENCE,
                   ((self._SEQUENCE,
                     ((self._VAR_NAME,
                       (self.Atom,
                        None)),
                         (self._VAR_NAME,
                          (self.Whitespace,
                           None)))),
                       (self._VAR_NAME,
                        (self.Backslash,
                         None)))),
                     (self._VAR_NAME,
                      (self.Whitespace,
                       None)))),
                   (self._VAR_NAME,
                    (self.Atom,
                     None)))),
                 (self._ZERO_OR_MORE,
                  (self._SUBEXPRESSION,
                   (self._SEQUENCE,
                    ((self._SEQUENCE,
                      ((self._VAR_NAME,
                        (self.Backslash,
                         None)),
                          (self._VAR_NAME,
                           (self.Whitespace,
                            None)))),
                        (self._VAR_NAME,
                         (self.Atom,
                          None)))))))))

    @cache
    def One_Or_More(self, position: int, dummy=None):
        """ <One_Or_More> = <Nucleus>, <Whitespace>, <Plus> ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._VAR_NAME,
                 (self.Nucleus,
                  None)),
                   (self._VAR_NAME,
                    (self.Whitespace,
                     None)))),
                 (self._VAR_NAME,
                  (self.Plus,
                   None)))))

    @cache
    def Zero_Or_More(self, position: int, dummy=None):
        """ <Zero_Or_More> = <Nucleus>, <Whitespace>, <Star> ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._VAR_NAME,
                 (self.Nucleus,
                  None)),
                   (self._VAR_NAME,
                    (self.Whitespace,
                     None)))),
                 (self._VAR_NAME,
                  (self.Star,
                   None)))))

    @cache
    def Optional(self, position: int, dummy=None):
        """ <Optional> = <Nucleus>, <Whitespace>, <Question_Mark> ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._VAR_NAME,
                 (self.Nucleus,
                  None)),
                   (self._VAR_NAME,
                    (self.Whitespace,
                     None)))),
                 (self._VAR_NAME,
                  (self.Question_Mark,
                   None)))))

    @cache
    def Whitespace(self, position: int, dummy=None):
        """ <Whitespace> = (" "/"\n")* ; """
        return self._SUBEXPRESSION(
            position,
            (self._ZERO_OR_MORE,
             (self._SUBEXPRESSION,
              (self._ORDERED_CHOICE,
               ((self._TERMINAL,
                 " "),
                (self._TERMINAL,
                 "\n"))))))

    @cache
    def RHS(self, position: int, dummy=None):
        """ <RHS> = <Sequence>/<Ordered_Choice>/<Atom> ; """
        return self._SUBEXPRESSION(
            position,
            (self._ORDERED_CHOICE,
             ((self._ORDERED_CHOICE,
               ((self._VAR_NAME,
                 (self.Sequence,
                  None)),
                   (self._VAR_NAME,
                    (self.Ordered_Choice,
                     None)))),
                 (self._VAR_NAME,
                  (self.Atom,
                   None)))))

    @cache
    def LHS(self, position: int, dummy=None):
        """ <LHS> = <Var_Name>, (<Whitespace>, <Semantic_Instructions>, <Whitespace>)? ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._VAR_NAME,
               (self.Var_Name,
                None)),
                 (self._OPTIONAL,
                  (self._SUBEXPRESSION,
                   (self._SEQUENCE,
                    ((self._SEQUENCE,
                     ((self._VAR_NAME,
                       (self.Whitespace,
                        None)),
                         (self._VAR_NAME,
                          (self.Semantic_Instructions,
                           None)))),
                        (self._VAR_NAME,
                         (self.Whitespace,
                          None)))))))))

    @cache
    def Rule(self, position: int, dummy=None):
        """ <Rule> = <LHS>, <Whitespace>, <Assignment>, <Whitespace>, <RHS>, <Whitespace>, <End_Rule>, <Whitespace>, <Comment>* ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._SEQUENCE,
                 ((self._SEQUENCE,
                   ((self._SEQUENCE,
                     ((self._SEQUENCE,
                       ((self._SEQUENCE,
                         ((self._SEQUENCE,
                           ((self._VAR_NAME,
                             (self.LHS,
                              None)),
                               (self._VAR_NAME,
                                (self.Whitespace,
                                 None)))),
                             (self._VAR_NAME,
                              (self.Assignment,
                               None)))),
                           (self._VAR_NAME,
                            (self.Whitespace,
                             None)))),
                         (self._VAR_NAME,
                          (self.RHS,
                           None)))),
                       (self._VAR_NAME,
                        (self.Whitespace,
                         None)))),
                     (self._VAR_NAME,
                      (self.End_Rule,
                       None)))),
                   (self._VAR_NAME,
                    (self.Whitespace,
                     None)))),
                 (self._ZERO_OR_MORE,
                  (self._VAR_NAME,
                   (self.Comment,
                    None))))))

    #Double up dem comments#
    @cache
    def Grammar(self, position: int, dummy=None):
        """ <Grammar> = <Rule>+, <Whitespace> ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._ONE_OR_MORE,
               (self._VAR_NAME,
                (self.Rule,
                 None))),
                 (self._VAR_NAME,
                  (self.Whitespace,
                   None)))))

    @cache
    def Comment(self, position: int, dummy=None):
        """ <Comment> = <Whitespace>, "#", (!"#", <ASCII>)*, "#", <Whitespace> ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._SEQUENCE,
                 ((self._SEQUENCE,
                   ((self._VAR_NAME,
                     (self.Whitespace,
                      None)),
                       (self._TERMINAL,
                        "#"))),
                     (self._ZERO_OR_MORE,
                      (self._SUBEXPRESSION,
                       (self._SEQUENCE,
                        ((self._NOT_PREDICATE,
                         (self._TERMINAL,
                          "#")),
                         (self._VAR_NAME,
                            (self.ASCII,
                             None)))))))),
                   (self._TERMINAL,
                    "#"))),
                 (self._VAR_NAME,
                  (self.Whitespace,
                   None)))))

    @cache
    def Semantic_Instructions(self, position: int, dummy=None):
        """ <Semantic_Instructions> = <Delete>/<Passthrough>/<Collect> ; """
        return self._SUBEXPRESSION(
            position,
            (self._ORDERED_CHOICE,
             ((self._ORDERED_CHOICE,
               ((self._VAR_NAME,
                 (self.Delete,
                  None)),
                   (self._VAR_NAME,
                    (self.Passthrough,
                     None)))),
                 (self._VAR_NAME,
                  (self.Collect,
                   None)))))

    @cache
    def Delete(self, position: int, dummy=None):
        """ <Delete> = "D", "E", "L", "E", "T", "E" ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._SEQUENCE,
                 ((self._SEQUENCE,
                   ((self._SEQUENCE,
                     ((self._TERMINAL,
                       "D"),
                      (self._TERMINAL,
                         "E"))),
                       (self._TERMINAL,
                        "L"))),
                     (self._TERMINAL,
                      "E"))),
                   (self._TERMINAL,
                    "T"))),
                 (self._TERMINAL,
                  "E"))))

    @cache
    def Passthrough(self, position: int, dummy=None):
        """ <Passthrough> = "P", "A", "S", "S", "T", "H", "R", "O", "U", "G", "H" ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._SEQUENCE,
                 ((self._SEQUENCE,
                   ((self._SEQUENCE,
                     ((self._SEQUENCE,
                       ((self._SEQUENCE,
                         ((self._SEQUENCE,
                           ((self._SEQUENCE,
                             ((self._SEQUENCE,
                               ((self._TERMINAL,
                                 "P"),
                                (self._TERMINAL,
                                   "A"))),
                                 (self._TERMINAL,
                                  "S"))),
                               (self._TERMINAL,
                                "S"))),
                             (self._TERMINAL,
                              "T"))),
                           (self._TERMINAL,
                            "H"))),
                         (self._TERMINAL,
                          "R"))),
                       (self._TERMINAL,
                        "O"))),
                     (self._TERMINAL,
                      "U"))),
                   (self._TERMINAL,
                    "G"))),
                 (self._TERMINAL,
                  "H"))))

    #Comment#
    @cache
    def Collect(self, position: int, dummy=None):
        """ <Collect> = "C", "O", "L", "L", "E", "C", "T" ; """
        return self._SUBEXPRESSION(
            position,
            (self._SEQUENCE,
             ((self._SEQUENCE,
               ((self._SEQUENCE,
                 ((self._SEQUENCE,
                   ((self._SEQUENCE,
                     ((self._SEQUENCE,
                       ((self._TERMINAL,
                         "C"),
                        (self._TERMINAL,
                           "O"))),
                         (self._TERMINAL,
                          "L"))),
                       (self._TERMINAL,
                        "L"))),
                     (self._TERMINAL,
                      "E"))),
                   (self._TERMINAL,
                    "C"))),
                 (self._TERMINAL,
                  "T"))))
