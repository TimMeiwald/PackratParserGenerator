

enum Rules{
    _ROOT,
    _TERMINAL,
    _SEQUENCE,
    _ORDERED_CHOICE,
    _NOT_PREDICATE,
    _AND_PREDICATE,
    _OPTIONAL,
    _ZERO_OR_MORE,
    _ONE_OR_MORE,
    _SUBEXPRESSION,
    _VAR_NAME,
    _test,


    // Following enum values are all autogenerated from grammar file
    Alphabet_Upper,
    Alphabet_Lower,
    Num,
    Spaces,
    Specials,
    ASCII,
    Apostrophe,
    Left_Angle_Bracket,
    Right_Angle_Bracket,
    Left_Bracket,
    Right_Bracket,
    Assignment,
    End_Rule,
    Ampersand,
    Exclamation_Mark,
    Plus,
    Star,
    Question_Mark,
    Comma,
    Backslash,
    Var_Name,
    Subexpression,
    Epsilon,
    Terminal,
    Nucleus,
    Atom,
    And_Predicate,
    Not_Predicate,
    Sequence,
    Ordered_Choice,
    One_Or_More,
    Zero_Or_More,
    Optional,
    Whitespace,
    RHS,
    LHS,
    Rule,
    Grammar,
    Comment,
    Semantic_Instructions,
    Delete,
    Passthrough,
    Collect,
}
#[derive(Debug)]
#[derive(PartialEq)]
struct ParserObject{
    position: u32,
    source: String,
}

fn main() {
    let something: &str = "This is a string";
}

fn c_token(po: &ParserObject) -> Option<u8> {
    if po.position >= po.source.chars().count() as u32 {
        return Option::None;
    }
    let s: u8 = po.source.as_bytes()[po.position as usize];
    return Option::Some(s);
}

fn c_terminal(po: &mut ParserObject, arg: u8) -> bool {
    /* If character at po.position is equal to arg, increment position and return True, else return False */

    if arg == c_token(&po).unwrap() {
        po.position = po.position + 1;
        return true;
    }
    else{
        return false;
    }
}

fn c_optional<T: Copy>(po: &mut ParserObject, pair: (&dyn Fn(&mut ParserObject, T) -> bool, T))-> bool {
    /* True if matches, False if not. Increments position on a match */

    // Fn(&u8), u8
    // Fn(&Fn), Fn
    let temp_position = po.position;
    let (func, arg) = pair; // unpack
    let bool = func(po, arg);

    if bool == true {
        return true
    }
    else{
        po.position = temp_position;
        return true;
    }
}


fn c_sequence<T: Copy, U: Copy>(po: &mut ParserObject, pair: ((&dyn Fn(&mut ParserObject, T) -> bool,T), (&dyn Fn(&mut ParserObject, U) -> bool,U))) -> bool{
//fn c_sequence<T: Copy, U: Copy>(po: &mut ParserObject, lhs: (&dyn Fn(&mut ParserObject, T) -> bool, T), rhs:(&dyn Fn(&mut ParserObject, U) -> bool, U)) -> bool {
    /* True if all expressions match, then updates position, else false, no positional update */

    let tmp_pos = po.position;
    let (lhs, rhs) = pair;
    let (lhs_func, lhs_arg) = lhs;
    let (rhs_func, rhs_arg) = rhs;

    let lhs_bool: bool = lhs_func(po, lhs_arg);
    let rhs_bool: bool = rhs_func(po, rhs_arg);

    if lhs_bool && rhs_bool {
        return true;
    }
    else {
        po.position = tmp_pos;
        return false;
    }
}

fn c_ordered_choice<T: Copy, U: Copy>(po: &mut ParserObject, pair: ((&dyn Fn(&mut ParserObject, T) -> bool,T), (&dyn Fn(&mut ParserObject, U) -> bool,U))) -> bool{
    /* True if one expression matches, then updates position, else false, no positional update */

    let tmp_pos = po.position;
    let (lhs, rhs) = pair;
    let (lhs_func, lhs_arg) = lhs;
    let (rhs_func, rhs_arg) = rhs;

    let lhs_bool: bool = lhs_func(po, lhs_arg);
    if lhs_bool {
        return true;
    }
    po.position = tmp_pos;

    let rhs_bool: bool = rhs_func(po, rhs_arg);
    if rhs_bool {
        return true;
    }
    po.position = tmp_pos;

    return false;
}

fn c_zero_or_more<T: Copy>(po: &mut ParserObject, pair: (&dyn Fn(&mut ParserObject, T) -> bool, T))-> bool {
    /* Always True, increments position each time the expression matches else continues without doing anything */

    let mut temp_position = po.position;
    let (func, arg) = pair; // unpack

    let mut bool = func(po, arg);

    loop {
        bool = func(po, arg);

        if bool {
            temp_position = po.position;
            continue;
        }
        else {
            po.position = temp_position;
            break;
        }
    }
    return true;
}

fn c_one_or_more<T: Copy>(po: &mut ParserObject, pair: (&dyn Fn(&mut ParserObject, T) -> bool, T)) -> bool {
    /* True if matches at least once, increments position each time the expression matches */

    let mut temp_position = po.position;
    let (func, arg) = pair; // unpack

    let mut bool = func(po, arg);

    if bool {
        temp_position = po.position;
    } else {
        po.position = temp_position;
        return false;
    }

    loop {
        bool = func(po, arg);
        if bool {
            temp_position = po.position;
            continue;
        } else {
            po.position = temp_position;
            break;
        }
    }
    return true;
}

fn c_and<T: Copy>(po: &mut ParserObject, pair: (&dyn Fn(&mut ParserObject, T) -> bool, T)) -> bool {
    /* True if the function results in True, never increments position */

    let temp_position = po.position;
    let (func, arg) = pair; // unpack
    let bool = func(po, arg);

    if bool {
        po.position = temp_position;
        return true;
    } else {
        po.position = temp_position;
        return false;
    }
}

fn c_not<T: Copy>(po: &mut ParserObject, pair: (&dyn Fn(&mut ParserObject, T) -> bool, T)) -> bool {
    /* True if the function results in False, never increments position */

    return !c_and(po, pair);
}

fn c_subexpression<T: Copy>(po: &mut ParserObject, pair: (&dyn Fn(&mut ParserObject, T) -> bool, T)) -> bool {
    /* Subexpression is any expression inside a pair of () brackets
    SUBEXPR essentially does nothing but allows for order of precedent
    more importantly order of precedence is very restricted because it made my life hard
    (mostly because I can't find a good definition of what order of precedence is in PEG) so use SUBEXPR
    to make more complicated rules */

    let (func, arg) = pair;
    let temp_position = po.position;
    let bool = func(po, arg);

    if bool {
        return true;
    } else {
        po.position = temp_position;
        return false;
    }
}


fn c_var_name<T: Copy>(po: &mut ParserObject, pair: (&dyn Fn(&mut ParserObject, T) -> bool, T)) -> bool{
    /* True if called function evaluates to true else false, Is used to call other functions*/

    let (func, arg) = pair;
    let temp_position = po.position;
    let bool = func(po, arg);

    if bool {
        return true;
    }
    else {
        po.position = temp_position;
        return false;
    }
}


fn Alphabet_Upper(po: &ParserObject) -> bool {
    /*
    <Alphabet_Upper> = "A"/"B"/"C"/"D"/"E"/"F"/"G"/"H"/"I"/"J"/"K"/"L"/"M"/"N"/"O"/"P"/"Q"/"R"/"S"/"T"/"U"/"V"/"W"/"X"/"Y"/"Z" ;
    
    We all love commments
    */
    return c_subexpression(&mut po, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_terminal, 65), (&c_terminal, 66)), (&c_terminal, 67)), (&c_terminal, 68)), (&c_terminal, 69)), (&c_terminal, 70)), (&c_terminal, 71)), (&c_terminal, 72)), (&c_terminal, 73)), (&c_terminal, 74)), (&c_terminal, 75)), (&c_terminal, 76)), (&c_terminal, 77)), (&c_terminal, 78)), (&c_terminal, 79)), (&c_terminal, 80)), (&c_terminal, 81)), (&c_terminal, 82)), (&c_terminal, 83)), (&c_terminal, 84)), (&c_terminal, 85)), (&c_terminal, 86)), (&c_terminal, 87)), (&c_terminal, 88)), (&c_terminal, 89)), (&c_terminal, 90)))
}
fn Alphabet_Lower(po: &ParserObject) -> bool {
    /*
    <Alphabet_Lower> = "a"/"b"/"c"/"d"/"e"/"f"/"g"/"h"/"i"/"j"/"k"/"l"/"m"/"n"/"o"/"p"/"q"/"r"/"s"/"t"/"u"/"v"/"w"/"x"/"y"/"z" ;
    */
    return c_subexpression(&mut po, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_terminal, 97), (&c_terminal, 98)), (&c_terminal, 99)), (&c_terminal, 100)), (&c_terminal, 101)), (&c_terminal, 102)), (&c_terminal, 103)), (&c_terminal, 104)), (&c_terminal, 105)), (&c_terminal, 106)), (&c_terminal, 107)), (&c_terminal, 108)), (&c_terminal, 109)), (&c_terminal, 110)), (&c_terminal, 111)), (&c_terminal, 112)), (&c_terminal, 113)), (&c_terminal, 114)), (&c_terminal, 115)), (&c_terminal, 116)), (&c_terminal, 117)), (&c_terminal, 118)), (&c_terminal, 119)), (&c_terminal, 120)), (&c_terminal, 121)), (&c_terminal, 122)))
}
fn Num(po: &ParserObject) -> bool {
    /*
    <Num> = "0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9" ;
    */
    return c_subexpression(&mut po, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_terminal, 48), (&c_terminal, 49)), (&c_terminal, 50)), (&c_terminal, 51)), (&c_terminal, 52)), (&c_terminal, 53)), (&c_terminal, 54)), (&c_terminal, 55)), (&c_terminal, 56)), (&c_terminal, 57)))
}
fn Spaces(po: &ParserObject) -> bool {
    /*
    <Spaces> = "\n"/"\t"/"\r"/" " ;
    */
    return c_subexpression(&mut po, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_terminal, 10), (&c_terminal, 9)), (&c_terminal, 13)), (&c_terminal, 32)))
}
fn Specials(po: &ParserObject) -> bool {
    /*
    <Specials> = "+"/"*"/"-"/"&"/"!"/"?"/"<"/">"/'"'/"("/")"/"_"/","/"/"/";"/"="/"\\"/"#"/":"/"|"/"."/"{"/"}"/"["/"]"/"%"/"'"/"^"/"~" ;
    */
    return c_subexpression(&mut po, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_terminal, 43), (&c_terminal, 42)), (&c_terminal, 45)), (&c_terminal, 38)), (&c_terminal, 33)), (&c_terminal, 63)), (&c_terminal, 60)), (&c_terminal, 62)), (&c_terminal, '34')), (&c_terminal, 40)), (&c_terminal, 41)), (&c_terminal, 95)), (&c_terminal, 44)), (&c_terminal, 47)), (&c_terminal, 59)), (&c_terminal, 61)), (&c_terminal, '92')), (&c_terminal, 35)), (&c_terminal, 58)), (&c_terminal, 124)), (&c_terminal, 46)), (&c_terminal, 123)), (&c_terminal, 125)), (&c_terminal, 91)), (&c_terminal, 93)), (&c_terminal, 37)), (&c_terminal, 39)), (&c_terminal, 94)), (&c_terminal, 126)))
}
fn ASCII(po: &ParserObject) -> bool {
    /*
    <ASCII> = <Alphabet_Lower>/<Alphabet_Upper>/<Num>/<Spaces>/<Specials> ;
    */
    return c_subexpression(&mut po, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_var_name, (&Alphabet_Lower, 0)), (&c_var_name, (&Alphabet_Upper, 0))), (&c_var_name, (&Num, 0))), (&c_var_name, (&Spaces, 0))), (&c_var_name, (&Specials, 0))))
}
fn Apostrophe(po: &ParserObject) -> bool {
    /*
    <Apostrophe> = '"' ;
    */
    return c_subexpression(&mut po, (&c_terminal, '34'))
}
fn Left_Angle_Bracket(po: &ParserObject) -> bool {
    /*
    <Left_Angle_Bracket> = "<" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 60))
}
fn Right_Angle_Bracket(po: &ParserObject) -> bool {
    /*
    <Right_Angle_Bracket> = ">" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 62))
}
fn Left_Bracket(po: &ParserObject) -> bool {
    /*
    <Left_Bracket> = "(" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 40))
}
fn Right_Bracket(po: &ParserObject) -> bool {
    /*
    <Right_Bracket> = ")" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 41))
}
fn Assignment(po: &ParserObject) -> bool {
    /*
    <Assignment> = "=" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 61))
}
fn End_Rule(po: &ParserObject) -> bool {
    /*
    <End_Rule> = ";" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 59))
}
fn Ampersand(po: &ParserObject) -> bool {
    /*
    <Ampersand> = "&" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 38))
}
fn Exclamation_Mark(po: &ParserObject) -> bool {
    /*
    <Exclamation_Mark> = "!" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 33))
}
fn Plus(po: &ParserObject) -> bool {
    /*
    <Plus> = "+" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 43))
}
fn Star(po: &ParserObject) -> bool {
    /*
    <Star> = "*" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 42))
}
fn Question_Mark(po: &ParserObject) -> bool {
    /*
    <Question_Mark> = "?" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 63))
}
fn Comma(po: &ParserObject) -> bool {
    /*
    <Comma> = "," ;
    */
    return c_subexpression(&mut po, (&c_terminal, 44))
}
fn Backslash(po: &ParserObject) -> bool {
    /*
    <Backslash> = "/" ;
    */
    return c_subexpression(&mut po, (&c_terminal, 47))
}
fn Var_Name(po: &ParserObject) -> bool {
    /*
    <Var_Name> = <Left_Angle_Bracket>, (<Alphabet_Lower>/<Alphabet_Upper>), (<Alphabet_Lower>/<Alphabet_Upper>/"_")*, <Right_Angle_Bracket> ;
    
    Not whitespace dependent, feel free to use multiple lines for readability
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_sequence, (&c_var_name, (&Left_Angle_Bracket, 0)), (&c_subexpression, (&c_ordered_choice, (&c_var_name, (&Alphabet_Lower, 0)), (&c_var_name, (&Alphabet_Upper, 0))))), (&c_zero_or_more, (&c_subexpression, (&c_ordered_choice, (&c_ordered_choice, (&c_var_name, (&Alphabet_Lower, 0)), (&c_var_name, (&Alphabet_Upper, 0))), (&c_terminal, 95))))), (&c_var_name, (&Right_Angle_Bracket, 0))))
}
fn Subexpression(po: &ParserObject) -> bool {
    /*
    <Subexpression> = <Left_Bracket>, <RHS>, <Right_Bracket> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_var_name, (&Left_Bracket, 0)), (&c_var_name, (&RHS, 0))), (&c_var_name, (&Right_Bracket, 0))))
}
fn Epsilon(po: &ParserObject) -> bool {
    /*
    <Epsilon> = <Apostrophe>, <Apostrophe> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_var_name, (&Apostrophe, 0)), (&c_var_name, (&Apostrophe, 0))))
}
fn Terminal(po: &ParserObject) -> bool {
    /*
    <Terminal> = (<Apostrophe>, <ASCII>, <Apostrophe>)/(<Apostrophe>, "\\", ("n"/"r"/"t"), <Apostrophe>)/<Epsilon> ;
    */
    return c_subexpression(&mut po, (&c_ordered_choice, (&c_ordered_choice, (&c_subexpression, (&c_sequence, (&c_sequence, (&c_var_name, (&Apostrophe, 0)), (&c_var_name, (&ASCII, 0))), (&c_var_name, (&Apostrophe, 0)))), (&c_subexpression, (&c_sequence, (&c_sequence, (&c_sequence, (&c_var_name, (&Apostrophe, 0)), (&c_terminal, '92')), (&c_subexpression, (&c_ordered_choice, (&c_ordered_choice, (&c_terminal, 110), (&c_terminal, 114)), (&c_terminal, 116)))), (&c_var_name, (&Apostrophe, 0))))), (&c_var_name, (&Epsilon, 0))))
}
fn Nucleus(po: &ParserObject) -> bool {
    /*
    <Nucleus> = (<Subexpression>/<Terminal>/<Var_Name>), <Whitespace> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_subexpression, (&c_ordered_choice, (&c_ordered_choice, (&c_var_name, (&Subexpression, 0)), (&c_var_name, (&Terminal, 0))), (&c_var_name, (&Var_Name, 0)))), (&c_var_name, (&Whitespace, 0))))
}
fn Atom(po: &ParserObject) -> bool {
    /*
    <Atom> = (<And_Predicate>/<Not_Predicate>/<One_Or_More>/<Zero_Or_More>/<Optional>/<Nucleus>), <Whitespace> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_subexpression, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_ordered_choice, (&c_var_name, (&And_Predicate, 0)), (&c_var_name, (&Not_Predicate, 0))), (&c_var_name, (&One_Or_More, 0))), (&c_var_name, (&Zero_Or_More, 0))), (&c_var_name, (&Optional, 0))), (&c_var_name, (&Nucleus, 0)))), (&c_var_name, (&Whitespace, 0))))
}
fn And_Predicate(po: &ParserObject) -> bool {
    /*
    <And_Predicate> = <Ampersand>, <Nucleus> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_var_name, (&Ampersand, 0)), (&c_var_name, (&Nucleus, 0))))
}
fn Not_Predicate(po: &ParserObject) -> bool {
    /*
    <Not_Predicate> = <Exclamation_Mark>, <Nucleus> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_var_name, (&Exclamation_Mark, 0)), (&c_var_name, (&Nucleus, 0))))
}
fn Sequence(po: &ParserObject) -> bool {
    /*
    <Sequence> = <Atom>, <Whitespace>, <Comma>, <Whitespace>, <Atom>, (<Comma>, <Whitespace>, <Atom>)* ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_var_name, (&Atom, 0)), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Comma, 0))), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Atom, 0))), (&c_zero_or_more, (&c_subexpression, (&c_sequence, (&c_sequence, (&c_var_name, (&Comma, 0)), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Atom, 0)))))))
}
fn Ordered_Choice(po: &ParserObject) -> bool {
    /*
    <Ordered_Choice> = <Atom>, <Whitespace>, <Backslash>, <Whitespace>, <Atom>, (<Backslash>, <Whitespace>, <Atom>)* ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_var_name, (&Atom, 0)), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Backslash, 0))), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Atom, 0))), (&c_zero_or_more, (&c_subexpression, (&c_sequence, (&c_sequence, (&c_var_name, (&Backslash, 0)), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Atom, 0)))))))
}
fn One_Or_More(po: &ParserObject) -> bool {
    /*
    <One_Or_More> = <Nucleus>, <Whitespace>, <Plus> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_var_name, (&Nucleus, 0)), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Plus, 0))))
}
fn Zero_Or_More(po: &ParserObject) -> bool {
    /*
    <Zero_Or_More> = <Nucleus>, <Whitespace>, <Star> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_var_name, (&Nucleus, 0)), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Star, 0))))
}
fn Optional(po: &ParserObject) -> bool {
    /*
    <Optional> = <Nucleus>, <Whitespace>, <Question_Mark> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_var_name, (&Nucleus, 0)), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Question_Mark, 0))))
}
fn Whitespace(po: &ParserObject) -> bool {
    /*
    <Whitespace> = (" "/"\n")* ;
    */
    return c_subexpression(&mut po, (&c_zero_or_more, (&c_subexpression, (&c_ordered_choice, (&c_terminal, 32), (&c_terminal, 10)))))
}
fn RHS(po: &ParserObject) -> bool {
    /*
    <RHS> = <Sequence>/<Ordered_Choice>/<Atom> ;
    */
    return c_subexpression(&mut po, (&c_ordered_choice, (&c_ordered_choice, (&c_var_name, (&Sequence, 0)), (&c_var_name, (&Ordered_Choice, 0))), (&c_var_name, (&Atom, 0))))
}
fn LHS(po: &ParserObject) -> bool {
    /*
    <LHS> = <Var_Name>, (<Whitespace>, <Semantic_Instructions>, <Whitespace>)? ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_var_name, (&Var_Name, 0)), (&c_optional, (&c_subexpression, (&c_sequence, (&c_sequence, (&c_var_name, (&Whitespace, 0)), (&c_var_name, (&Semantic_Instructions, 0))), (&c_var_name, (&Whitespace, 0)))))))
}
fn Rule(po: &ParserObject) -> bool {
    /*
    <Rule> = <LHS>, <Whitespace>, <Assignment>, <Whitespace>, <RHS>, <Whitespace>, <End_Rule>, <Whitespace>, <Comment>* ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_var_name, (&LHS, 0)), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&Assignment, 0))), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&RHS, 0))), (&c_var_name, (&Whitespace, 0))), (&c_var_name, (&End_Rule, 0))), (&c_var_name, (&Whitespace, 0))), (&c_zero_or_more, (&c_var_name, (&Comment, 0)))))
}
fn Grammar(po: &ParserObject) -> bool {
    /*
    <Grammar> = <Rule>+, <Whitespace> ;
    
    Double up dem comments
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_one_or_more, (&c_var_name, (&Rule, 0))), (&c_var_name, (&Whitespace, 0))))
}
fn Comment(po: &ParserObject) -> bool {
    /*
    <Comment> = <Whitespace>, "#", (!"#", <ASCII>)*, "#", <Whitespace> ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_var_name, (&Whitespace, 0)), (&c_terminal, 35)), (&c_zero_or_more, (&c_subexpression, (&c_sequence, (&c_not, (&c_terminal, 35)), (&c_var_name, (&ASCII, 0)))))), (&c_terminal, 35)), (&c_var_name, (&Whitespace, 0))))
}
fn Semantic_Instructions(po: &ParserObject) -> bool {
    /*
    <Semantic_Instructions> = <Delete>/<Passthrough>/<Collect> ;
    */
    return c_subexpression(&mut po, (&c_ordered_choice, (&c_ordered_choice, (&c_var_name, (&Delete, 0)), (&c_var_name, (&Passthrough, 0))), (&c_var_name, (&Collect, 0))))
}
fn Delete(po: &ParserObject) -> bool {
    /*
    <Delete> = "D", "E", "L", "E", "T", "E" ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_terminal, 68), (&c_terminal, 69)), (&c_terminal, 76)), (&c_terminal, 69)), (&c_terminal, 84)), (&c_terminal, 69)))
}
fn Passthrough(po: &ParserObject) -> bool {
    /*
    <Passthrough> = "P", "A", "S", "S", "T", "H", "R", "O", "U", "G", "H" ;
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_terminal, 80), (&c_terminal, 65)), (&c_terminal, 83)), (&c_terminal, 83)), (&c_terminal, 84)), (&c_terminal, 72)), (&c_terminal, 82)), (&c_terminal, 79)), (&c_terminal, 85)), (&c_terminal, 71)), (&c_terminal, 72)))
}
fn Collect(po: &ParserObject) -> bool {
    /*
    <Collect> = "C", "O", "L", "L", "E", "C", "T" ;
    
    Comment
    */
    return c_subexpression(&mut po, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_sequence, (&c_terminal, 67), (&c_terminal, 79)), (&c_terminal, 76)), (&c_terminal, 76)), (&c_terminal, 69)), (&c_terminal, 67)), (&c_terminal, 84)))
}