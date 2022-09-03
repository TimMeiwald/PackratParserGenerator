from packratparsergenerator.parser.core_parser import Parser
from packratparsergenerator.parser.rules import Rules
from packratparsergenerator.parser.grammar_parser import Grammar_Parser


class Comment_Maker():

    def __init__(self, node):
        if (node is None):
            raise TypeError(
                "Inputted node is None, maybe the rule failed when you expected success")
        self.comment = self.create_comment(node)

    def create_comment(self, node):
        c_string = self.selector(node)
        return c_string

    def selector(self, node):
        if (node.type == Rules.Sequence):
            return self.c_sequence(node)
        elif (node.type == Rules.Ordered_Choice):
            return self.c_ordered_choice(node)
        elif (node.type == Rules.One_Or_More):
            return self.c_one_or_more(node)
        elif (node.type == Rules.Zero_Or_More):
            return self.c_zero_or_more(node)
        elif (node.type == Rules.Optional):
            return self.c_optional(node)
        elif (node.type == Rules.And_Predicate):
            return self.c_and_predicate(node)
        elif (node.type == Rules.Not_Predicate):
            return self.c_not_predicate(node)
        elif (node.type == Rules.Subexpression):
            return self.c_subexpression(node)
        elif (node.type == Rules.Rule):
            return self.c_rule(node)
        elif (node.type == Rules.LHS):
            return self.c_lhs(node)
        elif (node.type == Rules.Terminal):
            return self.c_terminal(node)
        elif (node.type == Rules._TERMINAL):
            return self.c_TERMINAL(node)
        elif (node.type == Rules.Var_Name):
            return self.c_var_name(node)
        elif (node.type == Rules.Comment):
            raise Exception("Comment")
        else:
            raise Exception(
                f"Unidentified node of type: {node.type.name}, content: {node.content}")

    def c_sequence(self, node):
        c_string = ""
        for child in node.children:
            child_str = self.selector(child)
            c_string += child_str + ", "
        c_string = c_string[:-2]  # removes last comma and space
        return c_string

    def c_ordered_choice(self, node):
        c_string = ""
        for child in node.children:
            child_str = self.selector(child)
            c_string += child_str + "/"
        c_string = c_string[:-1]  # removes last comma and space
        return c_string

    def c_subexpression(self, node):
        try:
            c_string = "("
            child = node.children[0]
            child_str = self.selector(child)
            c_string += child_str + ")"
        except IndexError:
            c_string = self.c_var_name(node)
        return c_string

    def c_var_name(self, node):
        c_string = "<"
        c_string += node.content
        c_string += ">"
        return c_string

    def c_rule(self, node):
        try:
            c_string = ""
            c_string += self.selector(node.children[0])
            c_string += self.selector(node.children[1])
            c_string += " ;"
        except IndexError:
            c_string = self.c_var_name(node)
        return c_string

    def c_lhs(self, node):
        try:
            c_string = self.selector(node.children[0])
            c_string += " = "
        except IndexError:
            c_string = self.c_var_name(node)
        return c_string

    def c_and_predicate(self, node):
        c_string = "&" + self.selector(node.children[0])
        return c_string

    def c_not_predicate(self, node):
        c_string = "!" + self.selector(node.children[0])
        return c_string

    def c_optional(self, node):
        c_string = self.selector(node.children[0]) + "?"
        return c_string

    def c_one_or_more(self, node):
        c_string = self.selector(node.children[0]) + "+"
        return c_string

    def c_zero_or_more(self, node):
        c_string = self.selector(node.children[0]) + "*"
        return c_string

    def c_terminal(self, node):
        node = node.children[0]
        c_string = self.c_TERMINAL(node)
        return c_string

    def c_TERMINAL(self, node):
        if (node.content == '"'):
            c_string = f"'{node.content}'"
        elif (node.content == "\\"):
            c_string = f'"\\\\"'
        else:
            c_string = f'"{node.content}"'

        return c_string
