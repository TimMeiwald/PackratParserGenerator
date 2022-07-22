from typing import Callable
from core_parser import Node, Rules
from functools import partial
from collections import deque
class Rationalizer():

    def __init__(self, dict, inverse_dict):
        self.dict = dict
        self.inverse_dict = inverse_dict

    def deep_copy_tree(self, node: Node, top_level = False):
        """This makes a deep copy of the AST. 
        This matters because the caching means that sometimes stuff shares the same nodes
        and then causes circular loops. 
        It is at least also O(N) and only needs to be done once
        regardless of how many passes of the treewalker you do"""
        # Makes copy of node
        new_node = Node(node.type, node.content)
        new_node.parent = node.parent

        # Makes copy of children
        for child in node.children:
            new_child = self.deep_copy_tree(child)
            new_node.children.append(new_child)
        if(top_level == True):
            print("Tree has been deep copied")
        return new_node

    def tree_walker(self, node: Node, func : Callable):
        node = func(node)
        for child in node.children:
            self.tree_walker(child, func)
        return node

    def passthrough(self, node: Node, type: Rules | int):
        to_append_left = deque()
        to_del = deque()
        for child in node.children:
            print("ye")
            if(child.type.value == type.value):
                print("you")
                for subchild in child.children:
                    to_append_left.append(subchild)
                    subchild.parent = node
                to_del.append(child)
                print("Added to_del")
        for child in to_del:
            node.children.popleft()
        for subchild in to_append_left:
            node.children.appendleft(subchild)
        return node

    def test(self, node):
        print(f"Node type: {node.type}, Node parent: {node.parent}, Node children: {node.children}")


if __name__ == "__main__":
    from grammar_parser import Grammar_Parser
    from os import getcwd
    from os.path import join
    parser = Grammar_Parser()
    path = join(getcwd(), "src", "Grammar.txt")
    with open(path, "r") as fp:
        src = fp.read()
    print(f"Length of File is : {len(src)}")
    src = '<hey> = "A";'
    
    parser._set_src(src)
    position, bool, node = parser.Grammar(0)
    dict, inverse_dict = parser._rules_dict, parser._rules_dict_inverse
    rationalizer = Rationalizer(dict, inverse_dict)
    func1 = partial(rationalizer.passthrough, type = Rules._ORDERED_CHOICE)
    func2 = partial(rationalizer.passthrough, type = Rules._SEQUENCE)
    node = rationalizer.deep_copy_tree(node,True) # Needed because sometimes cached copies are used so multiple things have the same copies
    # This causes an infinite loop
    
    #parser.pretty_print(node)
    node = rationalizer.tree_walker(node, func1)
    node = rationalizer.tree_walker(node, func2)
    parser.pretty_print(node)