from typing import Callable
from packratparsergenerator.parser.core_parser import Node, Rules
from functools import partial
from collections import deque

class Rationalizer():
    """Class eliminates the superfluous nodes that result from parsing
    Leaving only terminals and vars
    
    This means that the user can do whatever they want with their AST
    without needing to know the details of how PEG parsing works"""
    def __init__(self):
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

    def tree_walker(self, node: Node):
        self.node = Node(Rules._ROOT)
        self.node.children.append(node)
        self.__tree_walker(self.node)
        if(len(self.node.children) != 0):
            return self.node
        else:
            return Node(Rules._ROOT, "ALL CONTENT REMOVED DUE TO RATIONALIZATION")
        

    def __tree_walker(self, node: Node):
        changes_made = False
        for child in node.children:
            self.__tree_walker(child)
            if(child.type.value in [2,7,8]): # 2 is Sequence node, 7, 8 zero and one or more
                changes_made, node_to_remove, node_to_add = self.passthrough(child)
        if(changes_made == True):
            if(node_to_remove != None):
                index = node.children.index(node_to_remove)
                node.children.remove(node_to_remove)
                if(node_to_add != None):
                    node_to_add.reverse()
                    for child in node_to_add:
                        node.children.insert(index, child)
            self.__tree_walker(node)

    def passthrough(self, node):
        """Collapses a given node type, by appending it's children to it's parent and making the childrens parent
        it's parent, then deletes itself"""
        for child in node.children:
            child.parent = node.parent
        node_to_remove = node
        node_to_add = node.children
        return True, node_to_remove, node_to_add

    def rationalize(self, node):
        #node = self.deep_copy_tree(node) # Don't know if this is even needed, seems to work without
        node = self.tree_walker(node)
        return node
        
  