#[derive(Debug)]
#[derive(PartialEq)]
struct ParserObject{
    position: u32,
    source: String,
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


fn c_ordered_choice<T, U>(po: &mut ParserObject, pair: ((Box<fn(&mut ParserObject, T) -> bool>,T), (Box<fn(&mut ParserObject, U) -> bool>,U))) -> bool{
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



fn c_subexpression<T>(po: &mut ParserObject, pair: (Box<fn(&mut ParserObject, T) -> bool>, T)) -> bool {
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
    return self._SUBEXPRESSION(position, 

























)
}
fn alphabet_lower(po: &mut ParserObject) -> bool {
    /*
    <Alphabet_Lower> = "a"/"b"/"c"/"d"/"e"/"f"/"g"/"h"/"i"/"j"/"k"/"l"/"m"/"n"/"o"/"p"/"q"/"r"/"s"/"t"/"u"/"v"/"w"/"x"/"y"/"z" ;
    */
    return self._SUBEXPRESSION(position, 

























)
}
fn num(po: &mut ParserObject) -> bool {
    /*
    <Num> = "0"/"1"/"2"/"3"/"4"/"5"/"6"/"7"/"8"/"9" ;
    */
    return self._SUBEXPRESSION(position, 









)
}
fn spaces(po: &mut ParserObject) -> bool {
    /*
    <Spaces> = "\n"/"\t"/"\r"/" " ;
    */
    return self._SUBEXPRESSION(position, 



)
}
fn specials(po: &mut ParserObject) -> bool {
    /*
    <Specials> = "+"/"*"/"-"/"&"/"!"/"?"/"<"/">"/'"'/"("/")"/"_"/","/"/"/";"/"="/"\\"/"#"/":"/"|"/"."/"{"/"}"/"["/"]"/"%"/"'"/"^"/"~" ;
    */
    return self._SUBEXPRESSION(position, 




























)
}
fn ascii(po: &mut ParserObject) -> bool {
    /*
    <ASCII> = <Alphabet_Lower>/<Alphabet_Upper>/<Num>/<Spaces>/<Specials> ;
    */
    return self._SUBEXPRESSION(position, 
        let temp_position = po.position;
        let bool = Alphabet_Lower(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Alphabet_Upper(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Num(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Spaces(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Specials(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
)
}
fn apostrophe(po: &mut ParserObject) -> bool {
    /*
    <Apostrophe> = '"' ;
    */
    return self._SUBEXPRESSION(position, )
}
fn left_angle_bracket(po: &mut ParserObject) -> bool {
    /*
    <Left_Angle_Bracket> = "<" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn right_angle_bracket(po: &mut ParserObject) -> bool {
    /*
    <Right_Angle_Bracket> = ">" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn left_bracket(po: &mut ParserObject) -> bool {
    /*
    <Left_Bracket> = "(" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn right_bracket(po: &mut ParserObject) -> bool {
    /*
    <Right_Bracket> = ")" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn assignment(po: &mut ParserObject) -> bool {
    /*
    <Assignment> = "=" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn end_rule(po: &mut ParserObject) -> bool {
    /*
    <End_Rule> = ";" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn ampersand(po: &mut ParserObject) -> bool {
    /*
    <Ampersand> = "&" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn exclamation_mark(po: &mut ParserObject) -> bool {
    /*
    <Exclamation_Mark> = "!" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn plus(po: &mut ParserObject) -> bool {
    /*
    <Plus> = "+" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn star(po: &mut ParserObject) -> bool {
    /*
    <Star> = "*" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn question_mark(po: &mut ParserObject) -> bool {
    /*
    <Question_Mark> = "?" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn comma(po: &mut ParserObject) -> bool {
    /*
    <Comma> = "," ;
    */
    return self._SUBEXPRESSION(position, )
}
fn backslash(po: &mut ParserObject) -> bool {
    /*
    <Backslash> = "/" ;
    */
    return self._SUBEXPRESSION(position, )
}
fn var_name(po: &mut ParserObject) -> bool {
    /*
    <Var_Name> = <Left_Angle_Bracket>, (<Alphabet_Lower>/<Alphabet_Upper>), (<Alphabet_Lower>/<Alphabet_Upper>/"_")*, <Right_Angle_Bracket> ;
    
    Not whitespace dependent, feel free to use multiple lines for readability
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Left_Angle_Bracket(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }let temp_position = po.position;
        let temp_position = po.position;
        let bool = Alphabet_Lower(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Alphabet_Upper(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
if bool {
            return true;
        } else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Right_Angle_Bracket(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn subexpression(po: &mut ParserObject) -> bool {
    /*
    <Subexpression> = <Left_Bracket>, <RHS>, <Right_Bracket> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Left_Bracket(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = RHS(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Right_Bracket(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn epsilon(po: &mut ParserObject) -> bool {
    /*
    <Epsilon> = <Apostrophe>, <Apostrophe> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Apostrophe(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Apostrophe(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn terminal(po: &mut ParserObject) -> bool {
    /*
    <Terminal> = (<Apostrophe>, <ASCII>, <Apostrophe>)/(<Apostrophe>, "\\", ("n"/"r"/"t"), <Apostrophe>)/<Epsilon> ;
    */
    return self._SUBEXPRESSION(position, let temp_position = po.position;
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Apostrophe(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = ASCII(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Apostrophe(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }}if bool {
            return true;
        } else {
            po.position = temp_position;
            return false;
        }
let temp_position = po.position;
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Apostrophe(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }let temp_position = po.position;


if bool {
            return true;
        } else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Apostrophe(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }}if bool {
            return true;
        } else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Epsilon(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
)
}
fn nucleus(po: &mut ParserObject) -> bool {
    /*
    <Nucleus> = (<Subexpression>/<Terminal>/<Var_Name>), <Whitespace> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;let temp_position = po.position;
        let temp_position = po.position;
        let bool = Subexpression(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Terminal(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Var_Name(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
if bool {
            return true;
        } else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn atom(po: &mut ParserObject) -> bool {
    /*
    <Atom> = (<And_Predicate>/<Not_Predicate>/<One_Or_More>/<Zero_Or_More>/<Optional>/<Nucleus>), <Whitespace> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;let temp_position = po.position;
        let temp_position = po.position;
        let bool = And_Predicate(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Not_Predicate(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = One_Or_More(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Zero_Or_More(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Optional(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Nucleus(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
if bool {
            return true;
        } else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn and_predicate(po: &mut ParserObject) -> bool {
    /*
    <And_Predicate> = <Ampersand>, <Nucleus> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Ampersand(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Nucleus(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn not_predicate(po: &mut ParserObject) -> bool {
    /*
    <Not_Predicate> = <Exclamation_Mark>, <Nucleus> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Exclamation_Mark(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Nucleus(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn sequence(po: &mut ParserObject) -> bool {
    /*
    <Sequence> = <Atom>, <Whitespace>, <Comma>, <Whitespace>, <Atom>, (<Comma>, <Whitespace>, <Atom>)* ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Atom(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Comma(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Atom(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn ordered_choice(po: &mut ParserObject) -> bool {
    /*
    <Ordered_Choice> = <Atom>, <Whitespace>, <Backslash>, <Whitespace>, <Atom>, (<Backslash>, <Whitespace>, <Atom>)* ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Atom(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Backslash(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Atom(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn one_or_more(po: &mut ParserObject) -> bool {
    /*
    <One_Or_More> = <Nucleus>, <Whitespace>, <Plus> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Nucleus(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Plus(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn zero_or_more(po: &mut ParserObject) -> bool {
    /*
    <Zero_Or_More> = <Nucleus>, <Whitespace>, <Star> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Nucleus(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Star(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn optional(po: &mut ParserObject) -> bool {
    /*
    <Optional> = <Nucleus>, <Whitespace>, <Question_Mark> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Nucleus(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Question_Mark(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn whitespace(po: &mut ParserObject) -> bool {
    /*
    <Whitespace> = (" "/"\n")* ;
    */
    return self._SUBEXPRESSION(position, )
}
fn rhs(po: &mut ParserObject) -> bool {
    /*
    <RHS> = <Sequence>/<Ordered_Choice>/<Atom> ;
    */
    return self._SUBEXPRESSION(position, 
        let temp_position = po.position;
        let bool = Sequence(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Ordered_Choice(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Atom(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
)
}
fn lhs(po: &mut ParserObject) -> bool {
    /*
    <LHS> = <Var_Name>, (<Whitespace>, <Semantic_Instructions>, <Whitespace>)? ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Var_Name(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn rule(po: &mut ParserObject) -> bool {
    /*
    <Rule> = <LHS>, <Whitespace>, <Assignment>, <Whitespace>, <RHS>, <Whitespace>, <End_Rule>, <Whitespace>, <Comment>* ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = LHS(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Assignment(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = RHS(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = End_Rule(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn grammar(po: &mut ParserObject) -> bool {
    /*
    <Grammar> = <Rule>+, <Whitespace> ;
    
    Double up dem comments
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn comment(po: &mut ParserObject) -> bool {
    /*
    <Comment> = <Whitespace>, "#", (!"#", <ASCII>)*, "#", <Whitespace> ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
        let temp_position = po.position;
        let bool = Whitespace(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn semantic_instructions(po: &mut ParserObject) -> bool {
    /*
    <Semantic_Instructions> = <Delete>/<Passthrough>/<Collect> ;
    */
    return self._SUBEXPRESSION(position, 
        let temp_position = po.position;
        let bool = Delete(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Passthrough(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }

        let temp_position = po.position;
        let bool = Collect(po);

        if bool {
            return true;
        }
        else {
            po.position = temp_position;
            return false;
        }
)
}
fn delete(po: &mut ParserObject) -> bool {
    /*
    <Delete> = "D", "E", "L", "E", "T", "E" ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn passthrough(po: &mut ParserObject) -> bool {
    /*
    <Passthrough> = "P", "A", "S", "S", "T", "H", "R", "O", "U", "G", "H" ;
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}
fn collect(po: &mut ParserObject) -> bool {
    /*
    <Collect> = "C", "O", "L", "L", "E", "C", "T" ;
    
    Comment
    */
    return self._SUBEXPRESSION(position, 
        let tmp_pos = po.position;
        let (lhs, rhs) = pair;

        if lhs_bool && rhs_bool {{
            return true;
        }}
        else {{
            po.position = tmp_pos;
            return false;
        }})
}