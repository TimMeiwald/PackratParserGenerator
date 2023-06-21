from packratparsergenerator.parser.core_parser import Rules, Parser
from packratparsergenerator.parser.grammar_parser import Grammar_Parser


class Parser_Call_Maker():

    def __init__(self, node):
        if (node is None):
            raise TypeError(
                "Inputted node is None, maybe the rule failed when you expected success")
        self.parse_string = self.create_parse_string(node)

    def create_parse_string(self, node):
        p_string = self.selector(node)
        return p_string

    def selector(self, node):
        if (node.type == Rules.Sequence):
            return self.p_sequence(node)
        elif (node.type == Rules.Ordered_Choice):
            return self.p_ordered_choice(node)
        elif (node.type == Rules.One_Or_More):
            return self.p_one_or_more(node)
        elif (node.type == Rules.Zero_Or_More):
            return self.p_zero_or_more(node)
        elif (node.type == Rules.Optional):
            return self.p_optional(node)
        elif (node.type == Rules.And_Predicate):
            return self.p_and_predicate(node)
        elif (node.type == Rules.Not_Predicate):
            return self.p_not_predicate(node)
        elif (node.type == Rules.Subexpression):
            return self.p_subexpression(node)
        elif (node.type == Rules.Rule):
            return self.p_rule(node)
        elif (node.type == Rules.LHS):
            return self.p_lhs(node)
        elif (node.type == Rules.Terminal):
            return self.p_terminal(node)
        elif (node.type == Rules._TERMINAL):
            return self.p_TERMINAL(node)
        elif (node.type == Rules.Var_Name):
            return self.p_var_name(node)
        elif(node.type == Rules.Epsilon):
            return self.p_epsilon(node)
        else:
            raise Exception(
                f"Unidentified node of type: {node.type.name}, content: {node.content}")

    def p_epsilon(self, node):
        return "Terminal{arg:'""'.to_string().as_bytes()[0]}"

    def p_sequence(self, node):
        p_string = ""
        for index in range(0, len(node.children) - 1):
            if (index == 0):
                p_string = "Sequence{arg_lhs:" + self.selector(
                    node.children[index]) + ", arg_rhs:" + self.selector(node.children[index + 1]) + "}"
            else:
                p_string = "Sequence{arg_lhs:"  + p_string + ", arg_rhs:" + \
                    self.selector(node.children[index + 1]) + "}"
        return p_string

    def p_ordered_choice(self, node):
        p_string = ""
        for index in range(0, len(node.children) - 1):
            if (index == 0):
                p_string = "OrderedChoice{arg_lhs:" + self.selector(
                    node.children[index]) + ", arg_rhs:" + self.selector(node.children[index + 1]) + "}"
            else:
                p_string = "OrderedChoice{arg_lhs:" + p_string + \
                    ", arg_rhs:" + self.selector(node.children[index + 1]) + "}"
        return p_string

    def p_subexpression(self, node):
        try:
            child = node.children[0]
            child_str = self.selector(child)
            p_string = "Subexpression{arg:" + child_str + "}"
        except IndexError:
            p_string = self.p_var_name(node)
        return p_string

    def p_var_name(self, node):
        p_string = "VarName{arg:" + node.content + "}"
        return p_string

    def p_rule(self, node):
        try:
            p_string = self.selector(node.children[1])
            p_string = p_string + ".resolve(position, source)"
        except IndexError:
            p_string = self.p_var_name(node)
        return p_string

    def p_lhs(self, node):
        try:
            p_string = self.selector(node.children[0])
        except IndexError:
            p_string = self.p_var_name(node)
        return p_string

    def p_and_predicate(self, node):
        p_string = "AndPredicate{arg: " + \
            self.selector(node.children[0]) + "}"
        return p_string

    def p_not_predicate(self, node):
        p_string = "NotPredicate{arg: " + \
            self.selector(node.children[0]) + "}"
        return p_string

    def p_optional(self, node):
        p_string = "Optional{arg: " + self.selector(node.children[0]) + "}"
        return p_string

    def p_one_or_more(self, node):
        p_string = "OneOrMore{arg: " + \
            self.selector(node.children[0]) + "}"
        return p_string

    def p_zero_or_more(self, node):
        p_string = "ZeroOrMore{arg: " + \
            self.selector(node.children[0]) + "}"
        return p_string

    def p_terminal(self, node):
        #p_string = "(self.Terminal, " + self.selector(node.children[0]) + ")"
        p_string = self.selector(node.children[0])
        return p_string

    def p_TERMINAL(self, node):
        if (node.content == '"'):
            p_string = "Terminal{arg:'" + node.content + "'.to_string().as_bytes()[0]}"
        elif (node.content == "\\"):
            p_string = "Terminal{arg:'" + "\\\\" + "'.to_string().as_bytes()[0]}"
        else:
            if (node.content is None):
                p_string = "Terminal{arg:" + '"' + \
                    "\033[31mERROR: NONE\033[0m" + '"' + ".to_string().as_bytes()[0]}"
            else:
                p_string = "Terminal{arg:" + '"' + node.content + '"' + ".to_string().as_bytes()[0]}"
        return p_string
