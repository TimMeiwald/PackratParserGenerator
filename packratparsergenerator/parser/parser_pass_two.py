from collections import deque
from packratparsergenerator.parser.rules import Rules


class Parser_Pass_Two():

    def __init__(self):
        self.delete_nodes = (Rules.Apostrophe, Rules.Left_Angle_Bracket, Rules.Right_Angle_Bracket, Rules.Left_Bracket, Rules.Right_Bracket, Rules.Assignment, Rules.End_Rule, Rules.Ampersand, Rules.Exclamation_Mark, Rules.Plus, Rules.Star, Rules.Question_Mark, Rules.Comma, Rules.Backslash, Rules.Whitespace, )
        self.passthrough_nodes = (Rules.Alphabet_Upper, Rules.Alphabet_Lower, Rules.Num, Rules.Spaces, Rules.Specials, Rules.ASCII, Rules.Nucleus, Rules.Atom, Rules.RHS, Rules.Semantic_Instructions)
        self.collect_nodes = (Rules.Var_Name, Rules.Comment, Rules.Delete, Rules.Passthrough, Rules.Collect, )
        # Anyone making modifications be aware everything after line 10 is
        # automatically added to
        self.tokens = deque()
        # generated parsers while everything before it isn't(so I can add the
        # right stuff based on grammar)

    def token_generator(self, node):
        self.tokens.append(node)
        for child in node.children:
            child.parent = node
            self.token_generator(child)

    def delete_kernel(self, node):
        if (node.type in self.delete_nodes):
            node.children = deque()
            if(node.parent is not None):
                node.parent.children.remove(node)
            del node
        else:
            return node

    def passthrough_kernel(self, node):
        if (node.type in self.passthrough_nodes):
            if(node.parent is not None):
                index = node.parent.children.index(node)
                for child in node.children:
                    node.parent.children.insert(index, child)
                node.parent.children.remove(node)
            del node
        else:
            return node

    def collect_kernel(self, node):
        if (node.type in self.collect_nodes):
            for child in node.children:
                if (child.type != Rules._TERMINAL):
                    raise ValueError(
                        f"Cannot collect if there are non terminals in the nodes childrens. Node_Type: {node.type.name}, Child_Type: {child.type.name}")
            node.content = ""
            for child in node.children:
                node.content += child.content
            node.children = deque()
            return node
        else:
            return node

    def __parse(self, nodes):
        new_deq = deque()
        for index in range(0, len(nodes)):
            node = nodes.pop()
            node = self.delete_kernel(node)
            if (node is not None):
                node = self.passthrough_kernel(node)
                node.children = node.children.reverse()
            if (node is not None):
                node = self.collect_kernel(node)
            if (node is not None):
                new_deq.append(node)
        return new_deq

    def parse(self, node):
        self.token_generator(node)
        nodes = deque(self.tokens)
        nodes = self.__parse(nodes)
        return nodes
