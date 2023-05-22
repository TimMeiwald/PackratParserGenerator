
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

fn c_optional<T>(po: &mut ParserObject, pair: (Box<fn(&mut ParserObject, T) -> bool>, T)) -> bool {
    /* True if matches, False if not. Increments position on a match */

    // Fn(&u8), u8
    // Fn(&Fn), Fn
    let temp_position = po.position;
    let (func, arg) = pair;
    let bool: bool = func(po, arg);

    if bool == true {
        return true
    }
    else{
        po.position = temp_position;
        return true;
    }
}


fn c_ordered_choice<T: Copy, U: Copy>(po: &mut ParserObject, pair: ((Box<fn(&mut ParserObject, T) -> bool>,T), (Box<fn(&mut ParserObject, U) -> bool>,U))) -> bool{
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



fn c_subexpression<T: Copy>(po: &mut ParserObject, pair: (Box<fn(&mut ParserObject, T) -> bool>, T)) -> bool {
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


fn alphabet_upper(po: &mut ParserObject) -> bool {
    /*
    <Alphabet_Upper> = "A"/"B"/"C"/"D"/"E"/"F"/"G"/"H"/"I"/"J"/"K"/"L"/"M"/"N"/"O"/"P"/"Q"/"R"/"S"/"T"/"U"/"V"/"W"/"X"/"Y"/"Z" ;
    
    We all love commments
    */
    return c_subexpression(po, (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_terminal), 65), (Box::new(c_terminal), 66))), (Box::new(c_terminal), 67))), (Box::new(c_terminal), 68))), (Box::new(c_terminal), 69))), (Box::new(c_terminal), 70))), (Box::new(c_terminal), 71))), (Box::new(c_terminal), 72))), (Box::new(c_terminal), 73))), (Box::new(c_terminal), 74))), (Box::new(c_terminal), 75))), (Box::new(c_terminal), 76))), (Box::new(c_terminal), 77))), (Box::new(c_terminal), 78))), (Box::new(c_terminal), 79))), (Box::new(c_terminal), 80))), (Box::new(c_terminal), 81))), (Box::new(c_terminal), 82))), (Box::new(c_terminal), 83))), (Box::new(c_terminal), 84))), (Box::new(c_terminal), 85))), (Box::new(c_terminal), 86))), (Box::new(c_terminal), 87))), (Box::new(c_terminal), 88))), (Box::new(c_terminal), 89))), (Box::new(c_terminal), 90))));
}
fn alphabet_lower(po: &mut ParserObject) -> bool {
    /*
    <Alphabet_Lower> = "a"/"b"/"c"/"d"/"e"/"f"/"g"/"h"/"i"/"j"/"k"/"l"/"m"/"n"/"o"/"p"/"q"/"r"/"s"/"t"/"u"/"v"/"w"/"x"/"y"/"z" ;
    */
    return c_subexpression(po, (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_terminal), 97), (Box::new(c_terminal), 98))), (Box::new(c_terminal), 99))), (Box::new(c_terminal), 100))), (Box::new(c_terminal), 101))), (Box::new(c_terminal), 102))), (Box::new(c_terminal), 103))), (Box::new(c_terminal), 104))), (Box::new(c_terminal), 105))), (Box::new(c_terminal), 106))), (Box::new(c_terminal), 107))), (Box::new(c_terminal), 108))), (Box::new(c_terminal), 109))), (Box::new(c_terminal), 110))), (Box::new(c_terminal), 111))), (Box::new(c_terminal), 112))), (Box::new(c_terminal), 113))), (Box::new(c_terminal), 114))), (Box::new(c_terminal), 115))), (Box::new(c_terminal), 116))), (Box::new(c_terminal), 117))), (Box::new(c_terminal), 118))), (Box::new(c_terminal), 119))), (Box::new(c_terminal), 120))), (Box::new(c_terminal), 121))), (Box::new(c_terminal), 122))));
}
fn num(po: &mut ParserObject) -> bool {
    /*
    <Num> = "0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9" ;
    */
    return c_subexpression(po, (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_terminal), 48), (Box::new(c_terminal), 49))), (Box::new(c_terminal), 50))), (Box::new(c_terminal), 51))), (Box::new(c_terminal), 52))), (Box::new(c_terminal), 53))), (Box::new(c_terminal), 54))), (Box::new(c_terminal), 55))), (Box::new(c_terminal), 56))), (Box::new(c_terminal), 57))));
}
fn spaces(po: &mut ParserObject) -> bool {
    /*
    <Spaces> = "\n"/"\t"/"\r"/" " ;
    */
    return c_subexpression(po, (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_terminal), 10), (Box::new(c_terminal), 9))), (Box::new(c_terminal), 13))), (Box::new(c_terminal), 32))));
}
fn specials(po: &mut ParserObject) -> bool {
    /*
    <Specials> = "+"/"*"/"-"/"&"/"!"/"?"/"<"/">"/'"'/"("/")"/"_"/","/"/"/";"/"="/"\\"/"#"/":"/"|"/"."/"{"/"}"/"["/"]"/"%"/"'"/"^"/"~" ;
    */
    return c_subexpression(po, (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_terminal), 43), (Box::new(c_terminal), 42))), (Box::new(c_terminal), 45))), (Box::new(c_terminal), 38))), (Box::new(c_terminal), 33))), (Box::new(c_terminal), 63))), (Box::new(c_terminal), 60))), (Box::new(c_terminal), 62))), (Box::new(c_terminal), "34"))), (Box::new(c_terminal), 40))), (Box::new(c_terminal), 41))), (Box::new(c_terminal), 95))), (Box::new(c_terminal), 44))), (Box::new(c_terminal), 47))), (Box::new(c_terminal), 59))), (Box::new(c_terminal), 61))), (Box::new(c_terminal), 92))), (Box::new(c_terminal), 35))), (Box::new(c_terminal), 58))), (Box::new(c_terminal), 124))), (Box::new(c_terminal), 46))), (Box::new(c_terminal), 123))), (Box::new(c_terminal), 125))), (Box::new(c_terminal), 91))), (Box::new(c_terminal), 93))), (Box::new(c_terminal), 37))), (Box::new(c_terminal), 39))), (Box::new(c_terminal), 94))), (Box::new(c_terminal), 126))));
}
fn ascii(po: &mut ParserObject) -> bool {
    /*
    <ASCII> = <Alphabet_Lower>/<Alphabet_Upper>/<Num>/<Spaces>/<Specials> ;
    */
    return c_subexpression(po, (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_var_name), (&alphabet_lower, 0)), (Box::new(c_var_name), (&alphabet_upper, 0)))), (Box::new(c_var_name), (&num, 0)))), (Box::new(c_var_name), (&spaces, 0)))), (Box::new(c_var_name), (&specials, 0)))));
}
fn apostrophe(po: &mut ParserObject) -> bool {
    /*
    <Apostrophe> = '"' ;
    */
    return c_subexpression(po, (Box::new(c_terminal), "34"));
}
fn left_angle_bracket(po: &mut ParserObject) -> bool {
    /*
    <Left_Angle_Bracket> = "<" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 60));
}
fn right_angle_bracket(po: &mut ParserObject) -> bool {
    /*
    <Right_Angle_Bracket> = ">" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 62));
}
fn left_bracket(po: &mut ParserObject) -> bool {
    /*
    <Left_Bracket> = "(" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 40));
}
fn right_bracket(po: &mut ParserObject) -> bool {
    /*
    <Right_Bracket> = ")" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 41));
}
fn assignment(po: &mut ParserObject) -> bool {
    /*
    <Assignment> = "=" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 61));
}
fn end_rule(po: &mut ParserObject) -> bool {
    /*
    <End_Rule> = ";" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 59));
}
fn ampersand(po: &mut ParserObject) -> bool {
    /*
    <Ampersand> = "&" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 38));
}
fn exclamation_mark(po: &mut ParserObject) -> bool {
    /*
    <Exclamation_Mark> = "!" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 33));
}
fn plus(po: &mut ParserObject) -> bool {
    /*
    <Plus> = "+" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 43));
}
fn star(po: &mut ParserObject) -> bool {
    /*
    <Star> = "*" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 42));
}
fn question_mark(po: &mut ParserObject) -> bool {
    /*
    <Question_Mark> = "?" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 63));
}
fn comma(po: &mut ParserObject) -> bool {
    /*
    <Comma> = "," ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 44));
}
fn backslash(po: &mut ParserObject) -> bool {
    /*
    <Backslash> = "/" ;
    */
    return c_subexpression(po, (Box::new(c_terminal), 47));
}
fn var_name(po: &mut ParserObject) -> bool {
    /*
    <Var_Name> = <Left_Angle_Bracket>, (<Alphabet_Lower>/<Alphabet_Upper>), (<Alphabet_Lower>/<Alphabet_Upper>/"_")*, <Right_Angle_Bracket> ;
    
    Not whitespace dependent, feel free to use multiple lines for readability
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&left_angle_bracket, 0)), (Box::new(c_subexpression), (Box::new(c_ordered_choice), ((Box::new(c_var_name), (&alphabet_lower, 0)), (Box::new(c_var_name), (&alphabet_upper, 0))))))), (Box::new(c_zero_or_more), (Box::new(c_subexpression), (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_var_name), (&alphabet_lower, 0)), (Box::new(c_var_name), (&alphabet_upper, 0)))), (Box::new(c_terminal), 95))))))), (Box::new(c_var_name), (&right_angle_bracket, 0)))));
}
fn subexpression(po: &mut ParserObject) -> bool {
    /*
    <Subexpression> = <Left_Bracket>, <RHS>, <Right_Bracket> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&left_bracket, 0)), (Box::new(c_var_name), (&rhs, 0)))), (Box::new(c_var_name), (&right_bracket, 0)))));
}
fn epsilon(po: &mut ParserObject) -> bool {
    /*
    <Epsilon> = <Apostrophe>, <Apostrophe> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_var_name), (&apostrophe, 0)), (Box::new(c_var_name), (&apostrophe, 0)))));
}
fn terminal(po: &mut ParserObject) -> bool {
    /*
    <Terminal> = (<Apostrophe>, <ASCII>, <Apostrophe>)/(<Apostrophe>, "\\", ("n"/"r"/"t"), <Apostrophe>)/<Epsilon> ;
    */
    return c_subexpression(po, (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_subexpression), (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&apostrophe, 0)), (Box::new(c_var_name), (&ascii, 0)))), (Box::new(c_var_name), (&apostrophe, 0))))), (Box::new(c_subexpression), (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&apostrophe, 0)), (Box::new(c_terminal), 92))), (Box::new(c_subexpression), (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_terminal), 110), (Box::new(c_terminal), 114))), (Box::new(c_terminal), 116)))))), (Box::new(c_var_name), (&apostrophe, 0))))))), (Box::new(c_var_name), (&epsilon, 0)))));
}
fn nucleus(po: &mut ParserObject) -> bool {
    /*
    <Nucleus> = (<Subexpression>/<Terminal>/<Var_Name>), <Whitespace> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_subexpression), (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_var_name), (&subexpression, 0)), (Box::new(c_var_name), (&terminal, 0)))), (Box::new(c_var_name), (&var_name, 0))))), (Box::new(c_var_name), (&whitespace, 0)))));
}
fn atom(po: &mut ParserObject) -> bool {
    /*
    <Atom> = (<And_Predicate>/<Not_Predicate>/<One_Or_More>/<Zero_Or_More>/<Optional>/<Nucleus>), <Whitespace> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_subexpression), (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_var_name), (&and_predicate, 0)), (Box::new(c_var_name), (&not_predicate, 0)))), (Box::new(c_var_name), (&one_or_more, 0)))), (Box::new(c_var_name), (&zero_or_more, 0)))), (Box::new(c_var_name), (&optional, 0)))), (Box::new(c_var_name), (&nucleus, 0))))), (Box::new(c_var_name), (&whitespace, 0)))));
}
fn and_predicate(po: &mut ParserObject) -> bool {
    /*
    <And_Predicate> = <Ampersand>, <Nucleus> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_var_name), (&ampersand, 0)), (Box::new(c_var_name), (&nucleus, 0)))));
}
fn not_predicate(po: &mut ParserObject) -> bool {
    /*
    <Not_Predicate> = <Exclamation_Mark>, <Nucleus> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_var_name), (&exclamation_mark, 0)), (Box::new(c_var_name), (&nucleus, 0)))));
}
fn sequence(po: &mut ParserObject) -> bool {
    /*
    <Sequence> = <Atom>, <Whitespace>, <Comma>, <Whitespace>, <Atom>, (<Comma>, <Whitespace>, <Atom>)* ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&atom, 0)), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&comma, 0)))), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&atom, 0)))), (Box::new(c_zero_or_more), (Box::new(c_subexpression), (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&comma, 0)), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&atom, 0)))))))));
}
fn ordered_choice(po: &mut ParserObject) -> bool {
    /*
    <Ordered_Choice> = <Atom>, <Whitespace>, <Backslash>, <Whitespace>, <Atom>, (<Backslash>, <Whitespace>, <Atom>)* ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&atom, 0)), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&backslash, 0)))), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&atom, 0)))), (Box::new(c_zero_or_more), (Box::new(c_subexpression), (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&backslash, 0)), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&atom, 0)))))))));
}
fn one_or_more(po: &mut ParserObject) -> bool {
    /*
    <One_Or_More> = <Nucleus>, <Whitespace>, <Plus> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&nucleus, 0)), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&plus, 0)))));
}
fn zero_or_more(po: &mut ParserObject) -> bool {
    /*
    <Zero_Or_More> = <Nucleus>, <Whitespace>, <Star> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&nucleus, 0)), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&star, 0)))));
}
fn optional(po: &mut ParserObject) -> bool {
    /*
    <Optional> = <Nucleus>, <Whitespace>, <Question_Mark> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&nucleus, 0)), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&question_mark, 0)))));
}
fn whitespace(po: &mut ParserObject) -> bool {
    /*
    <Whitespace> = (" "/"\n")* ;
    */
    return c_subexpression(po, (Box::new(c_zero_or_more), (Box::new(c_subexpression), (Box::new(c_ordered_choice), ((Box::new(c_terminal), 32), (Box::new(c_terminal), 10))))));
}
fn rhs(po: &mut ParserObject) -> bool {
    /*
    <RHS> = <Sequence>/<Ordered_Choice>/<Atom> ;
    */
    return c_subexpression(po, (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_var_name), (&sequence, 0)), (Box::new(c_var_name), (&ordered_choice, 0)))), (Box::new(c_var_name), (&atom, 0)))));
}
fn lhs(po: &mut ParserObject) -> bool {
    /*
    <LHS> = <Var_Name>, (<Whitespace>, <Semantic_Instructions>, <Whitespace>)? ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_var_name), (&var_name, 0)), (Box::new(c_optional), (Box::new(c_subexpression), (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&whitespace, 0)), (Box::new(c_var_name), (&semantic_instructions, 0)))), (Box::new(c_var_name), (&whitespace, 0)))))))));
}
fn rule(po: &mut ParserObject) -> bool {
    /*
    <Rule> = <LHS>, <Whitespace>, <Assignment>, <Whitespace>, <RHS>, <Whitespace>, <End_Rule>, <Whitespace>, <Comment>* ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&lhs, 0)), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&assignment, 0)))), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&rhs, 0)))), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_var_name), (&end_rule, 0)))), (Box::new(c_var_name), (&whitespace, 0)))), (Box::new(c_zero_or_more), (Box::new(c_var_name), (&comment, 0))))));
}
fn grammar(po: &mut ParserObject) -> bool {
    /*
    <Grammar> = <Rule>+, <Whitespace> ;
    
    Double up dem comments
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_one_or_more), (Box::new(c_var_name), (&rule, 0))), (Box::new(c_var_name), (&whitespace, 0)))));
}
fn comment(po: &mut ParserObject) -> bool {
    /*
    <Comment> = <Whitespace>, "#", (!"#", <ASCII>)*, "#", <Whitespace> ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_var_name), (&whitespace, 0)), (Box::new(c_terminal), 35))), (Box::new(c_zero_or_more), (Box::new(c_subexpression), (Box::new(c_sequence), ((Box::new(c_not), (Box::new(c_terminal), 35)), (Box::new(c_var_name), (&ascii, 0)))))))), (Box::new(c_terminal), 35))), (Box::new(c_var_name), (&whitespace, 0)))));
}
fn semantic_instructions(po: &mut ParserObject) -> bool {
    /*
    <Semantic_Instructions> = <Delete>/<Passthrough>/<Collect> ;
    */
    return c_subexpression(po, (Box::new(c_ordered_choice), ((Box::new(c_ordered_choice), ((Box::new(c_var_name), (&delete, 0)), (Box::new(c_var_name), (&passthrough, 0)))), (Box::new(c_var_name), (&collect, 0)))));
}
fn delete(po: &mut ParserObject) -> bool {
    /*
    <Delete> = "D", "E", "L", "E", "T", "E" ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_terminal), 68), (Box::new(c_terminal), 69))), (Box::new(c_terminal), 76))), (Box::new(c_terminal), 69))), (Box::new(c_terminal), 84))), (Box::new(c_terminal), 69))));
}
fn passthrough(po: &mut ParserObject) -> bool {
    /*
    <Passthrough> = "P", "A", "S", "S", "T", "H", "R", "O", "U", "G", "H" ;
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_terminal), 80), (Box::new(c_terminal), 65))), (Box::new(c_terminal), 83))), (Box::new(c_terminal), 83))), (Box::new(c_terminal), 84))), (Box::new(c_terminal), 72))), (Box::new(c_terminal), 82))), (Box::new(c_terminal), 79))), (Box::new(c_terminal), 85))), (Box::new(c_terminal), 71))), (Box::new(c_terminal), 72))));
}
fn collect(po: &mut ParserObject) -> bool {
    /*
    <Collect> = "C", "O", "L", "L", "E", "C", "T" ;
    
    Comment
    */
    return c_subexpression(po, (Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_sequence), ((Box::new(c_terminal), 67), (Box::new(c_terminal), 79))), (Box::new(c_terminal), 76))), (Box::new(c_terminal), 76))), (Box::new(c_terminal), 69))), (Box::new(c_terminal), 67))), (Box::new(c_terminal), 84))));
}