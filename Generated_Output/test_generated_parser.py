from Generated_Output.grammar_parser import Grammar_Parser as Gen_Grammar_Parser
from packratparsergenerator.parser.grammar_parser import Grammar_Parser as Grammar_Parser
from os import getcwd
from os.path import join
from packratparsergenerator.parser.parser_pass_two import Parser_Pass_Two


def test_generated_parser(parser_class, src):
    parser = parser_class()
    parser._set_src(src)
    position, bool, node = parser._VAR_NAME(0, (parser.Grammar, None)) #var_name, Needed to ensure correct handling of deques
    assert (len(src), True) == (position, True), "Parsing has failed"
    assert bool, "Parsing has failed"
    parsing = Parser_Pass_Two()
    parsing.parse(node)
    node.pretty_print()
    return node


if __name__ == "__main__":
    """
    path = join(getcwd(), "packratparsergenerator", "parser", "Grammar.txt")
    with open(path, "r") as fp:
        src = fp.read()
    print(f"Length of File is : {len(src)}")
    parser = Gen_Grammar_Parser()
    parser._set_src(src)
    position, bool, node = parser._VAR_NAME(0, (parser.Grammar, None)) #var_name, Needed to ensure correct handling of deques
    print(position, bool)
    assert (len(src), True) == (position, True), "Parsing has failed"
    #node.pretty_print()
    print(node)
    parsing = Parser_Pass_Two()
    parsing.parse(node)

    node.pretty_print()
    """
    path = join(getcwd(), "packratparsergenerator", "parser", "Grammar.txt")
    with open(path, "r") as fp:
        src = fp.read()
    print(f"Length of File is : {len(src)}")
    old_parser = test_generated_parser(Grammar_Parser, src)
    new_parser = test_generated_parser(Gen_Grammar_Parser, src)
    if(new_parser == old_parser):
        print("VICTORY")
    else:
        print("DOHHH")