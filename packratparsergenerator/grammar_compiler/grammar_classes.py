from packratparsergenerator.parser.core_parser import Rules, Parser
"""Essentially two main types of nodes, those with a single child
and those with multiple which are Sequence and Ordered_Choice
While _ZERO_OR_MORE can result in multiple nodes that's only on parse
the rule Zero_Or_More will only ever have one child since it's the command to
parse it's argument once or more. Ofc that child could be a subexpression with a child that's a 
sequence but it doesn't need to worry about that"""

class Unary_Node():
    """All nodes not Sequence or Ordered_Choice"""

    def __init__(self, node, type):
        assert node.type.value == type, f"Got: {type}, Expected: {node.type.value}"
        self.type = type
        self.node = node

    def call(self):
        if(len(self.node.children) != 0):
            self.child = self.node.children[0]
            if(self.child.content in ["Sequence", "Ordered_Choice"]):
                self.arg = Binary_Node(self.child, self.child.type.value)
            else:
                self.arg = Unary_Node(self.child, self.child.type.value)
        else:
            return self.tuple_representation(self.child.content)

    def tuple_representation(self, arg):
        representation = f"(self.{self.type}, {arg})"
        return representation
    
    def call_representation(self, arg):
        "Should only be called at top level"
        representation = f"self.{self.type}(position, {arg})"
        return representation
    

class Binary_Node():
    """Nodes Sequence or Ordered_Choice"""
    def __init__(self, node, type):
        assert node.content == type
        self.type = type
        self.node = node
        self.children = node.children
        if(self.child_content in ["Sequence", "Ordered_Choice"]):
            raise TypeError("A binary node's child should never be a binary_node")
        else:
            self.arg = Unary_Node(self.child, self.child_content)
    
    def create(self):
        for i in range(0, len(self.children)-1):
            self.tuple_representation(self.children[i], self.children[i+1]) #Might be wrongway around inspect output

    def tuple_representation(self, arg1, arg2):
        representation = f"(self.{self.type}, ({arg1}, {arg2}))"
        return representation
    
    def call_representation(self, arg1, arg2):
        "Should only be called at top level"
        representation = f"self.{self.type}(position, ({arg1}, {arg2}))"
        return representation


if __name__ == "__main__":
    parser = Parser()
    parser._set_src("ABC")
    tup1 = (parser._TERMINAL, "A")
    ret = parser._VAR_NAME(0, tup1)
    parser.pretty_print(ret[2])

    x = Unary_Node(ret[2], Rules._VAR.value)
    y = x.call()