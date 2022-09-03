from packratparsergenerator.Generated_Output.parser import Grammar_Parser as Gen_Grammar_Parser
from packratparsergenerator.Generated_Output.parser import Parser_Pass_Two as Gen_Parser_Pass_Two
from packratparsergenerator.parser.grammar_parser import Grammar_Parser as Grammar_Parser
from packratparsergenerator.parser.parser_pass_two import Parser_Pass_Two
from os import getcwd
from os.path import join
from time import time


def og_parser(src):  # Not a proper test yet so renamed to prevent pytest from running it
    parser = Grammar_Parser()
    parser._set_src(src)
    time_start = time()
    # var_name, Needed to ensure correct handling of deques
    position, bool, node = parser._VAR_NAME(0, (parser.Grammar, None))
    time_end = time()
    print(f"{Grammar_Parser} time to parse is {time_end - time_start}")
    assert (len(src), True) == (position, True), "Parsing has failed"
    assert bool, "Parsing has failed"
    parsing = Parser_Pass_Two()
    parsing.parse(node)
    node.pretty_print()
    return node


def new_parser(src):  # Not a proper test yet so renamed to prevent pytest from running it
    parser = Gen_Grammar_Parser()
    parser._set_src(src)
    time_start = time()
    # var_name, Needed to ensure correct handling of deques
    position, bool, node = parser._VAR_NAME(0, (parser.Grammar, None))
    time_end = time()
    print(f"{Gen_Grammar_Parser} time to parse is {time_end - time_start}")
    assert (len(src), True) == (position, True), "Parsing has failed"
    assert bool, "Parsing has failed"
    parsing = Gen_Parser_Pass_Two()
    parsing.parse(node)
    node.pretty_print()
    return node


if __name__ == "__main__":
    # Tests the old parser grammar since the old parser does not have the new
    # rules yet necessarily.
    path = join(getcwd(), "packratparsergenerator", "parser", "Grammar.txt")
    with open(path, "r") as fp:
        src = fp.read()
    print(f"Length of File is : {len(src)}")
    #src = '<Rule> = "A";'
    old_parser = og_parser(src)
    new_parser = new_parser(src)
    if (new_parser == old_parser):
        print("Output of New Parser is Identical to Output of Old parser for given source input")
    else:
        print("DOHHH: Your New Parser does not have the same output as old parser, Is this expected? E.g Rule change? or Not")
