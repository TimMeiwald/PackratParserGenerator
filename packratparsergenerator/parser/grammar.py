from packratparsergenerator.parser.core_parser import Parser
from packratparsergenerator.parser.grammar_parser import Grammar_Parser
from packratparsergenerator.parser.parser_pass_two import Parser_Pass_Two
from time import time

def parse(*,src_filepath=None ,src=None):
    if(src_filepath != None):
        with open(src_filepath, "r") as fp:
            src = fp.read()
    elif(src != None):
        src = src
    else:
        raise Exception("must provide a valid input")
    start_time = time()
    parser = Grammar_Parser()
    parser._set_src(src)
    tup = (parser.Grammar, None)
    position, bool, node = parser._VAR_NAME(0, tup) 
    pass_two = Parser_Pass_Two()
    pass_two.parse(node)
    end_time = time()
    print(f"Time to Parse: {end_time-start_time}")
    print(type(node))
    return node
