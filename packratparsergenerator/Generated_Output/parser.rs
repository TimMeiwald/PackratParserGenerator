
    #[derive(Copy, Clone)]
    struct Alphabet_Upper;
    impl Resolvable for Alphabet_Upper {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return alphabet_upper(position, source); 
        }
    }
    
    fn alphabet_upper(position: u32, source: &str) -> (bool, u32) {
    return OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:Terminal{arg:"A".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"B".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"C".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"D".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"E".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"F".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"G".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"H".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"I".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"J".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"K".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"L".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"M".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"N".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"O".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"P".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"Q".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"R".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"S".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"T".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"U".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"V".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"W".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"X".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"Y".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"Z".to_string().as_bytes()[0]}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Alphabet_Lower;
    impl Resolvable for Alphabet_Lower {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return alphabet_lower(position, source); 
        }
    }
    
    fn alphabet_lower(position: u32, source: &str) -> (bool, u32) {
    return OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:Terminal{arg:"a".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"b".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"c".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"d".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"e".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"f".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"g".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"h".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"i".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"j".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"k".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"l".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"m".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"n".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"o".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"p".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"q".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"r".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"s".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"t".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"u".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"v".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"w".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"x".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"y".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"z".to_string().as_bytes()[0]}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Num;
    impl Resolvable for Num {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return num(position, source); 
        }
    }
    
    fn num(position: u32, source: &str) -> (bool, u32) {
    return OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:Terminal{arg:"0".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"1".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"2".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"3".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"4".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"5".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"6".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"7".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"8".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"9".to_string().as_bytes()[0]}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Spaces;
    impl Resolvable for Spaces {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return spaces(position, source); 
        }
    }
    
    fn spaces(position: u32, source: &str) -> (bool, u32) {
    return OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:Terminal{arg:"\n".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"\t".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"\r".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:" ".to_string().as_bytes()[0]}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Specials;
    impl Resolvable for Specials {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return specials(position, source); 
        }
    }
    
    fn specials(position: u32, source: &str) -> (bool, u32) {
    return OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:Terminal{arg:"+".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"*".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"-".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"&".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"!".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"?".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"<".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:">".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:'"'.to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"(".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:")".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"_".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:",".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"/".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:";".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"=".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:'\\'.to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"#".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:":".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"|".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:".".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"{".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"}".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"[".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"]".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"%".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"'".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"^".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"~".to_string().as_bytes()[0]}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Ascii;
    impl Resolvable for Ascii {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return ascii(position, source); 
        }
    }
    
    fn ascii(position: u32, source: &str) -> (bool, u32) {
    return OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:VarName{arg:Alphabet_Lower}, arg_rhs:VarName{arg:Alphabet_Upper}}, arg_rhs:VarName{arg:Num}}, arg_rhs:VarName{arg:Spaces}}, arg_rhs:VarName{arg:Specials}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Apostrophe;
    impl Resolvable for Apostrophe {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return apostrophe(position, source); 
        }
    }
    
    fn apostrophe(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:'"'.to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Left_Angle_Bracket;
    impl Resolvable for Left_Angle_Bracket {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return left_angle_bracket(position, source); 
        }
    }
    
    fn left_angle_bracket(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:"<".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Right_Angle_Bracket;
    impl Resolvable for Right_Angle_Bracket {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return right_angle_bracket(position, source); 
        }
    }
    
    fn right_angle_bracket(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:">".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Left_Bracket;
    impl Resolvable for Left_Bracket {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return left_bracket(position, source); 
        }
    }
    
    fn left_bracket(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:"(".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Right_Bracket;
    impl Resolvable for Right_Bracket {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return right_bracket(position, source); 
        }
    }
    
    fn right_bracket(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:")".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Assignment;
    impl Resolvable for Assignment {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return assignment(position, source); 
        }
    }
    
    fn assignment(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:"=".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct End_Rule;
    impl Resolvable for End_Rule {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return end_rule(position, source); 
        }
    }
    
    fn end_rule(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:";".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Ampersand;
    impl Resolvable for Ampersand {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return ampersand(position, source); 
        }
    }
    
    fn ampersand(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:"&".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Exclamation_Mark;
    impl Resolvable for Exclamation_Mark {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return exclamation_mark(position, source); 
        }
    }
    
    fn exclamation_mark(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:"!".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Plus;
    impl Resolvable for Plus {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return plus(position, source); 
        }
    }
    
    fn plus(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:"+".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Star;
    impl Resolvable for Star {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return star(position, source); 
        }
    }
    
    fn star(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:"*".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Question_Mark;
    impl Resolvable for Question_Mark {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return question_mark(position, source); 
        }
    }
    
    fn question_mark(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:"?".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Comma;
    impl Resolvable for Comma {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return comma(position, source); 
        }
    }
    
    fn comma(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:",".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Backslash;
    impl Resolvable for Backslash {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return backslash(position, source); 
        }
    }
    
    fn backslash(position: u32, source: &str) -> (bool, u32) {
    return Terminal{arg:"/".to_string().as_bytes()[0]}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Var_Name;
    impl Resolvable for Var_Name {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return var_name(position, source); 
        }
    }
    
    fn var_name(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Left_Angle_Bracket}, arg_rhs:Subexpression{arg:OrderedChoice{arg_lhs:VarName{arg:Alphabet_Lower}, arg_rhs:VarName{arg:Alphabet_Upper}}}}, arg_rhs:ZeroOrMore{arg: Subexpression{arg:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:VarName{arg:Alphabet_Lower}, arg_rhs:VarName{arg:Alphabet_Upper}}, arg_rhs:Terminal{arg:"_".to_string().as_bytes()[0]}}}}}, arg_rhs:VarName{arg:Right_Angle_Bracket}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Subexpression;
    impl Resolvable for Subexpression {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return subexpression(position, source); 
        }
    }
    
    fn subexpression(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Left_Bracket}, arg_rhs:VarName{arg:RHS}}, arg_rhs:VarName{arg:Right_Bracket}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Epsilon;
    impl Resolvable for Epsilon {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return epsilon(position, source); 
        }
    }
    
    fn epsilon(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:VarName{arg:Apostrophe}, arg_rhs:VarName{arg:Apostrophe}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Lterminal;
    impl Resolvable for Lterminal {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return lterminal(position, source); 
        }
    }
    
    fn lterminal(position: u32, source: &str) -> (bool, u32) {
    return OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:Subexpression{arg:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Apostrophe}, arg_rhs:VarName{arg:ASCII}}, arg_rhs:VarName{arg:Apostrophe}}}, arg_rhs:Subexpression{arg:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Apostrophe}, arg_rhs:Terminal{arg:'\\'.to_string().as_bytes()[0]}}, arg_rhs:Subexpression{arg:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:Terminal{arg:"n".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"r".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"t".to_string().as_bytes()[0]}}}}, arg_rhs:VarName{arg:Apostrophe}}}}, arg_rhs:VarName{arg:Epsilon}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Nucleus;
    impl Resolvable for Nucleus {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return nucleus(position, source); 
        }
    }
    
    fn nucleus(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Subexpression{arg:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:VarName{arg:Subexpression}, arg_rhs:VarName{arg:LTerminal}}, arg_rhs:VarName{arg:Var_Name}}}, arg_rhs:VarName{arg:Whitespace}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Atom;
    impl Resolvable for Atom {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return atom(position, source); 
        }
    }
    
    fn atom(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Subexpression{arg:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:VarName{arg:And_Predicate}, arg_rhs:VarName{arg:Not_Predicate}}, arg_rhs:VarName{arg:One_Or_More}}, arg_rhs:VarName{arg:Zero_Or_More}}, arg_rhs:VarName{arg:Optional}}, arg_rhs:VarName{arg:Nucleus}}}, arg_rhs:VarName{arg:Whitespace}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct And_Predicate;
    impl Resolvable for And_Predicate {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return and_predicate(position, source); 
        }
    }
    
    fn and_predicate(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:VarName{arg:Ampersand}, arg_rhs:VarName{arg:Nucleus}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Not_Predicate;
    impl Resolvable for Not_Predicate {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return not_predicate(position, source); 
        }
    }
    
    fn not_predicate(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:VarName{arg:Exclamation_Mark}, arg_rhs:VarName{arg:Nucleus}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Sequence;
    impl Resolvable for Sequence {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return sequence(position, source); 
        }
    }
    
    fn sequence(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Atom}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Comma}}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Atom}}, arg_rhs:ZeroOrMore{arg: Subexpression{arg:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Comma}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Atom}}}}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Ordered_Choice;
    impl Resolvable for Ordered_Choice {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return ordered_choice(position, source); 
        }
    }
    
    fn ordered_choice(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Atom}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Backslash}}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Atom}}, arg_rhs:ZeroOrMore{arg: Subexpression{arg:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Backslash}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Atom}}}}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct One_Or_More;
    impl Resolvable for One_Or_More {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return one_or_more(position, source); 
        }
    }
    
    fn one_or_more(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Nucleus}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Plus}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Zero_Or_More;
    impl Resolvable for Zero_Or_More {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return zero_or_more(position, source); 
        }
    }
    
    fn zero_or_more(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Nucleus}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Star}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Optional;
    impl Resolvable for Optional {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return optional(position, source); 
        }
    }
    
    fn optional(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Nucleus}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Question_Mark}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Whitespace;
    impl Resolvable for Whitespace {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return whitespace(position, source); 
        }
    }
    
    fn whitespace(position: u32, source: &str) -> (bool, u32) {
    return ZeroOrMore{arg: Subexpression{arg:OrderedChoice{arg_lhs:Terminal{arg:" ".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"\n".to_string().as_bytes()[0]}}}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Rhs;
    impl Resolvable for Rhs {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return rhs(position, source); 
        }
    }
    
    fn rhs(position: u32, source: &str) -> (bool, u32) {
    return OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:VarName{arg:Sequence}, arg_rhs:VarName{arg:Ordered_Choice}}, arg_rhs:VarName{arg:Atom}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Lhs;
    impl Resolvable for Lhs {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return lhs(position, source); 
        }
    }
    
    fn lhs(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:VarName{arg:Var_Name}, arg_rhs:Optional{arg: Subexpression{arg:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Whitespace}, arg_rhs:VarName{arg:Semantic_Instructions}}, arg_rhs:VarName{arg:Whitespace}}}}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Rule;
    impl Resolvable for Rule {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return rule(position, source); 
        }
    }
    
    fn rule(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:LHS}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:Assignment}}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:RHS}}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:VarName{arg:End_Rule}}, arg_rhs:VarName{arg:Whitespace}}, arg_rhs:ZeroOrMore{arg: VarName{arg:Comment}}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Grammar;
    impl Resolvable for Grammar {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return grammar(position, source); 
        }
    }
    
    fn grammar(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:OneOrMore{arg: VarName{arg:Rule}}, arg_rhs:VarName{arg:Whitespace}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Comment;
    impl Resolvable for Comment {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return comment(position, source); 
        }
    }
    
    fn comment(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:VarName{arg:Whitespace}, arg_rhs:Terminal{arg:"#".to_string().as_bytes()[0]}}, arg_rhs:ZeroOrMore{arg: Subexpression{arg:Sequence{arg_lhs:NotPredicate{arg: Terminal{arg:"#".to_string().as_bytes()[0]}}, arg_rhs:VarName{arg:ASCII}}}}}, arg_rhs:Terminal{arg:"#".to_string().as_bytes()[0]}}, arg_rhs:VarName{arg:Whitespace}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Semantic_Instructions;
    impl Resolvable for Semantic_Instructions {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return semantic_instructions(position, source); 
        }
    }
    
    fn semantic_instructions(position: u32, source: &str) -> (bool, u32) {
    return OrderedChoice{arg_lhs:OrderedChoice{arg_lhs:VarName{arg:Delete}, arg_rhs:VarName{arg:Passthrough}}, arg_rhs:VarName{arg:Collect}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Delete;
    impl Resolvable for Delete {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return delete(position, source); 
        }
    }
    
    fn delete(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Terminal{arg:"D".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"E".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"L".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"E".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"T".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"E".to_string().as_bytes()[0]}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Passthrough;
    impl Resolvable for Passthrough {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return passthrough(position, source); 
        }
    }
    
    fn passthrough(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Terminal{arg:"P".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"A".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"S".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"S".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"T".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"H".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"R".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"O".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"U".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"G".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"H".to_string().as_bytes()[0]}}.resolve(position, source);}

    #[derive(Copy, Clone)]
    struct Collect;
    impl Resolvable for Collect {
    fn resolve(&self, position: u32, source: &str) -> (bool, u32) {
        return collect(position, source); 
        }
    }
    
    fn collect(position: u32, source: &str) -> (bool, u32) {
    return Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Sequence{arg_lhs:Terminal{arg:"C".to_string().as_bytes()[0]}, arg_rhs:Terminal{arg:"O".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"L".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"L".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"E".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"C".to_string().as_bytes()[0]}}, arg_rhs:Terminal{arg:"T".to_string().as_bytes()[0]}}.resolve(position, source);}
