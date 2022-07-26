

from collections import deque
from packratparsergenerator.parser.core_parser import Rules



class Parser_Pass_Two():

    def __init__(self):
        self.delete_nodes = ("Whitespace", "Apostrophe", "Left_Angle_Bracket", "Right_Angle_Bracket", "Left_Bracket", 
        "Right_Bracket", "Plus", "Star", "Question_Mark", "Backslash", "Comma", "End_Rule", "Assignment")
        self.passthrough_nodes = ("ASCII", "Alphabet_Upper", "Alphabet_Lower", "Atom", "Nucleus", "RHS", "Specials")
        self.collect_nodes = ("Var_Name")

    def token_generator(self, node):
        yield node
        for child in node.children:
            child.parent = node
            yield from self.token_generator(child)

    def delete_kernel(self, node):
        if(node.content in self.delete_nodes):
            node.children = deque()
            node.parent.children.remove(node)
            del node
        else:
            return node

    def passthrough_kernel(self, node):
        if(node.content in self.passthrough_nodes):
            index = node.parent.children.index(node)
            for child in node.children:
                node.parent.children.insert(index, child)
            node.parent.children.remove(node)
            del node
        else:
            return node

    def collect_kernel(self, node):
        if(node.content in self.collect_nodes and node.type is Rules._VAR): #Not sure why or is needed
            for child in node.children:
                if(child.type != Rules._TERMINAL):
                    raise ValueError(f"Cannot collect if there are non terminals in the nodes childrens. Node_Type: {node.type}, Child_Type: {child.type}")
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
            if(node != None):
                node = self.passthrough_kernel(node)
            if(node != None):
                node = self.collect_kernel(node)
            if(node != None):
                new_deq.append(node)
        return new_deq


    def parse(self, node):
        nodes = deque(self.token_generator(node))
        nodes = self.__parse(nodes)
        return nodes

