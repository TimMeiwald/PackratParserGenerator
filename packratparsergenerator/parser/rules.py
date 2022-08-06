from enum import Enum

class Rules(Enum):
    _ROOT = 0
    _TERMINAL = 1
    _SEQUENCE = 2
    _ORDERED_CHOICE = 3
    _NOT_PREDICATE = 4
    _AND_PREDICATE = 5
    _OPTIONAL = 6
    _ZERO_OR_MORE = 7
    _ONE_OR_MORE = 8
    _SUBEXPRESSION = 10
    _VAR = 11

    Alphabet_Upper = 21
    Alphabet_Lower = 22
    Num = 23
    Specials = 24
    Spaces = 25
    ASCII = 26
    Apostrophe = 27
    Left_Angle_Bracket = 28
    Right_Angle_Bracket = 29
    Left_Bracket = 30
    Right_Bracket = 31
    Assignment = 32
    End_Rule = 33
    Ampersand = 34
    Exclamation_Mark = 35
    Plus = 36
    Star = 37
    Question_Mark = 38
    Comma = 39
    Backslash = 40


    Var_Name = 41
    Subexpression = 42
    Terminal = 43
    Nucleus = 44
    Atom = 45

    And_Predicate = 46
    Not_Predicate = 47
    Sequence = 48
    Ordered_Choice = 49
    One_Or_More = 50
    Zero_Or_More = 51
    Optional = 52

    Whitespace = 53
    RHS = 54
    LHS = 55
    Rule = 56
    Grammar = 57