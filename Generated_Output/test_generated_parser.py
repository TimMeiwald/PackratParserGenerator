from Generated_Output.grammar_parser import Grammar_Parser as Gen_Grammar_Parser
from packratparsergenerator.parser.grammar_parser import Grammar_Parser as Grammar_Parser
from os import getcwd
from os.path import join
from packratparsergenerator.parser.parser_pass_two import Parser_Pass_Two
from time import time

def ntest_generated_parser(parser_class, src): # Not a proper test yet so renamed to prevent pytest from running it
    parser = parser_class()
    parser._set_src(src)
    time_start = time()
    position, bool, node = parser._VAR_NAME(0, (parser.Grammar, None)) #var_name, Needed to ensure correct handling of deques
    time_end = time()
    print(f"{parser_class} time to parse is {time_end - time_start}")
    assert (len(src), True) == (position, True), "Parsing has failed"
    assert bool, "Parsing has failed"
    parsing = Parser_Pass_Two()
    parsing.parse(node)
    #node.pretty_print()
    return node


if __name__ == "__main__":
    path = join(getcwd(), "packratparsergenerator", "parser", "Grammar.txt")
    with open(path, "r") as fp:
        src = fp.read()
    print(f"Length of File is : {len(src)}")
    old_parser = test_generated_parser(Grammar_Parser, src)
    new_parser = test_generated_parser(Gen_Grammar_Parser, src)
    if(new_parser == old_parser):
        print("Output of New Parser is Identical to Output of Old parser for given source input")
    else:
        print("DOHHH: Your New Parser does not have the same output as old parser, Is this expected? E.g Rule change? or Not")