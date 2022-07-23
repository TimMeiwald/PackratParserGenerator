from typing import Callable
from core_parser import Node, Rules
from functools import partial
from collections import deque

class Rationalizer():

    def __init__(self, dict, inverse_dict):
        self.dict = dict
        self.inverse_dict = inverse_dict
        self.node = Node(Rules._ROOT)

    def deep_copy_tree(self, node: Node, top_level = True, parent = None):
        """This makes a deep copy of the AST. 
        This matters because the caching means that sometimes stuff shares the same nodes
        and then causes circular loops. 
        It is at least also O(N) and only needs to be done once
        regardless of how many passes of the treewalker you do"""
        # Makes copy of node
        new_node = Node(node.type, node.content)
        new_node.parent = parent

        # Makes copy of children
        for child in node.children:
            new_child = self.deep_copy_tree(child, False, new_node)
            new_node.children.append(new_child)
        if(top_level == True):
            print("Tree has been deep copied")
        return new_node

    def tree_walker(self, node: Node, type: Rules | int ,func: Callable):
        self.node = Node(Rules._ROOT)
        self.node.children.append(node)
        self.__tree_walker(self.node, type, func)
        return self.node.children[0]
        


    def __tree_walker(self, node: Node, type: Rules | int ,func: Callable):
        changes_made = False
        for child in node.children:
            self.__tree_walker(child, type, func)
            if(child.type.value == type.value):
                changes_made, node_to_remove, node_to_add = func(type, child)
        if(changes_made == True):
            for child in node_to_add:
                node.children.append(child)
            node.children.remove(node_to_remove)
            self.__tree_walker(node, type, func)

    def test(self, type, node):
        # Return True to have the function be reapplied to the same function
        # e.g To deal with newly appended Node.
        print(f"Node type: {node.type}")
        if(node.type.value == type.value):
            return False #Since no changes made causes a RecursionError as always sequence availdable
        else:
            return False

    def passthrough(self, type, node):
        """Collapses a given node type, by appending it's children to it's parent and making the childrens parent
        it's parent, then deletes itself"""
        if(node.type.value == type.value):
            #print(f"Node: {node.type}, Parent:{node.parent.type}")
            #print(len(node.parent.children))
            for child in node.children:
                child.parent = node.parent
            node_to_remove = node
            node_to_add = node.children
            return True, node_to_remove, node_to_add
        else:
            return False, None, None
    
    def var_collector(self, type, node, var_type):


if __name__ == "__main__":
    from grammar_parser import Grammar_Parser
    from os import getcwd
    from os.path import join
    parser = Grammar_Parser()
    path = join(getcwd(), "src", "Grammar.txt")
    with open(path, "r") as fp:
        src = fp.read()
    print(f"Length of File is : {len(src)}")
    #src = '<hey> = "A";'
    
    parser._set_src(src)
    position, bool, node = parser.Grammar(0)
    dict, inverse_dict = parser._rules_dict, parser._rules_dict_inverse
    rationalizer = Rationalizer(dict, inverse_dict)

    node = rationalizer.deep_copy_tree(node) 
    node = rationalizer.tree_walker(node, Rules._SEQUENCE, rationalizer.passthrough)
    node = rationalizer.tree_walker(node, Rules._ORDERED_CHOICE, rationalizer.passthrough)
    node = rationalizer.tree_walker(node, Rules._OPTIONAL, rationalizer.passthrough)
    node = rationalizer.tree_walker(node, Rules._SUBEXPRESSION, rationalizer.passthrough)
    node = rationalizer.tree_walker(node, Rules._ONE_OR_MORE, rationalizer.passthrough)
    node = rationalizer.tree_walker(node, Rules._ZERO_OR_MORE, rationalizer.passthrough)
    
    var_collecter = partial(rationalizer.var_collecter, var_type=)
    parser.pretty_print(node)
