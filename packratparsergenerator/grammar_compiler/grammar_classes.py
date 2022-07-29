from packratparsergenerator.parser.core_parser import Rules, Parser
from packratparsergenerator.parser.grammar_parser import Grammar_Parser
from collections import deque
"""Essentially two main types of nodes, those with a single child
and those with multiple which are Sequence and Ordered_Choice
While _ZERO_OR_MORE can result in multiple nodes that's only on parse
the rule Zero_Or_More will only ever have one child since it's the command to
parse it's argument once or more. Ofc that child could be a subexpression with a child that's a 
sequence but it doesn't need to worry about that"""

class Core_Compiler():

    def __init__(self, node):
        if(node == None):
            raise TypeError("Inputted node is None, maybe the rule failed when you expected success")
        self.node = node
        self.function_string = ""
    
    def create(self):
        if(len(self.node.children) == 1):
            return self.single_node()
        elif(len(self.node.children) == 0):
            return self.tuple_representation()
        else:
            return self.multi_node()
    
    def single_node(self):
        new = Core_Compiler(self.node.children[0])
        arg = new.create()
        self.function_string = f"(self.{self.node.content}, {arg})"
        return self.function_string

    
    def multi_node(self):
        args = deque()
        for child in self.node.children:
            new = Core_Compiler(child)
            arg = new.create()
            args.append(arg)
        for index in range(0, len(args)-1):
            if(index == 0):
                self.function_string = f"self._SEQUENCE, ({args[index]}, {args[index+1]})"
            else:
                self.function_string = f"self._SEQUENCE, ({self.function_string}, {args[index+1]})"
        self.function_string = "(" + self.function_string + ")"
        return self.function_string

    def tuple_representation(self):
        if(self.node.content not in ['"']):
            self.function_string = f'(self.{self.node.type}, "{self.node.content}")'
        else:
            self.function_string = f"(self.{self.node.type}, '{self.node.content}')"
        return self.function_string

if __name__ == "__main__":
    parser = Grammar_Parser()
    parser._set_src('"A"')
    node = parser.caller(0, parser.Terminal)
    parser.pretty_print(node)

    x = Core_Compiler(node)
    y = x.create()
    print(y)
    


    
