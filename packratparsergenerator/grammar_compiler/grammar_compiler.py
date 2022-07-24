

from packratparsergenerator.parser.grammar import parse
from packratparsergenerator.parser.core_parser import Rules, Node, Parser
from os import getcwd
from os.path import join


class Grammar_Compiler():

    def __init__(self):
        self.node = Node(Rules._ROOT)

    def tree_walker(self, node: Node, type, func):
        self.node = Node(Rules._ROOT)
        self.node.children.append(node)
        self.__tree_walker(self.node, type, func)
        if(len(self.node.children) != 0):
            return self.node
        else:
            return Node(Rules._ROOT, "ALL CONTENT REMOVED DUE TO RATIONALIZATION")
        
    def __tree_walker(self, node: Node, type, func):
        changes_made = False
        for child in node.children:
            self.__tree_walker(child, type, func)
            if(child.content == type): # 2 is Sequence node, 7, 8 zero and one or more
                changes_made, node_to_remove, node_to_add = func(child)
        if(changes_made == True):
            if(node_to_remove != None):
                index = node.children.index(node_to_remove)
                node.children.remove(node_to_remove)
                if(node_to_add != None):
                    node_to_add.reverse()
                    for child in node_to_add:
                        node.children.insert(index, child)
            self.__tree_walker(node, type, func)

    def passthrough(self, node):
        """Collapses a given node type, by appending it's children to it's parent and making the childrens parent
        it's parent, then deletes itself"""
        for child in node.children:
            child.parent = node.parent
        node_to_remove = node
        node_to_add = node.children
        return True, node_to_remove, node_to_add

    def delete(self, node):
        "Deletes node entirely"
        node_to_remove = node
        return True, node_to_remove, None
    
    def collect(self, node):
        """Collects all the terminal values of a given node
        Fails if non terminals exist."""
        for child in node.children:
            if(child.type.value == Rules._TERMINAL):
                return False, None, None
        node.content = ""
        for child in node.children:
            node.content += child.content
        node.children = []
        return False, None, None

    def compile(self, node):
        node = self.tree_walker(node, "Whitespace", self.delete)
        node = self.tree_walker(node.children[0], "Apostrophe", self.delete)
        node = self.tree_walker(node.children[0], "Left_Angle_Bracket", self.delete)
        node = self.tree_walker(node.children[0], "Right_Angle_Bracket", self.delete)
        node = self.tree_walker(node.children[0], "Left_Bracket", self.delete)
        node = self.tree_walker(node.children[0], "Right_Bracket", self.delete)
        node = self.tree_walker(node.children[0], "Plus", self.delete)
        node = self.tree_walker(node.children[0], "Star", self.delete)
        node = self.tree_walker(node.children[0], "Question_Mark", self.delete)
        node = self.tree_walker(node.children[0], "Backslash", self.delete)
        node = self.tree_walker(node.children[0], "Comma", self.delete)
        node = self.tree_walker(node.children[0], "End_Rule", self.delete)
        node = self.tree_walker(node.children[0], "Assignment", self.delete)
        node = self.tree_walker(node.children[0], "Alphabet_Upper", self.passthrough)
        node = self.tree_walker(node.children[0], "Alphabet_Lower", self.passthrough)
        node = self.tree_walker(node.children[0], "ASCII", self.passthrough)
        node = self.tree_walker(node.children[0], "Atom", self.passthrough)
        node = self.tree_walker(node.children[0], "Nucleus", self.passthrough)
        node = self.tree_walker(node.children[0], "LHS", self.passthrough)
        node = self.tree_walker(node.children[0], "RHS", self.passthrough)
        node = self.tree_walker(node.children[0], "RHS", self.passthrough)
        node = self.tree_walker(node.children[0], "Var_Name", self.collect)
        
        return node
        
  
        
if __name__ == "__main__":
    from time import time
    path = join(getcwd(),"packratparsergenerator", "parser", "Grammar.txt")
    print(path)
    printer = Parser()
    ret = parse(path)
    x = Grammar_Compiler()
    start_time = time()
    node = x.compile(ret)
    end_time = time()
    printer.pretty_print(node)
    print(f"Time taken is {end_time-start_time}")