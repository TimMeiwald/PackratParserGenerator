from Generated_Output.grammar_parser import Grammar_Parser
from os import getcwd
from os.path import join
from packratparsergenerator.parser.parser_pass_two import Parser_Pass_Two
if __name__ == "__main__":
    path = join(getcwd(), "packratparsergenerator", "parser", "Grammar.txt")
    with open(path, "r") as fp:
        src = fp.read()
    print(f"Length of File is : {len(src)}")
    parser = Grammar_Parser()
    parser._set_src(src)
    position, bool, node = parser._VAR_NAME(0, (parser.Grammar, None))
    print(position, bool)
    assert (len(src), True) == (position, True), "Parsing has failed"
    #node.pretty_print()
    print(node)
    parsing = Parser_Pass_Two()
    parsing.parse(node)

    node.pretty_print()