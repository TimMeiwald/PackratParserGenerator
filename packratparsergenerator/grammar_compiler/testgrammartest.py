from Generated_Output.parser import Grammar_Parser, Parser
from Generated_Output.parser import Parser_Pass_Two
a = Grammar_Parser()


b = a.parse("1234", a.int)
print(b[0:1])
b[2].pretty_print()



