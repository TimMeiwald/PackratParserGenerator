from packratparsergenerator.parser.grammar_parser import Grammar_Parser
from packratparsergenerator.parser.rationalizer import Rationalizer
from time import time

def parse(src_filepath):
    with open(src_filepath, "r") as fp:
        src = fp.read()
    start_time = time()
    parser = Grammar_Parser()
    parser._set_src(src)
    position, bool, node = parser.Grammar(0)
    end_time = time()
    print(f"Time to Parse: {end_time-start_time}")
    
    start2_time = time()
    rationalizer = Rationalizer()
    node = rationalizer.rationalize(node)
    print(f"Time to rationalize: {end2_time-start2_time}")
    end2_time = time()

    print(f"Total time to parse: {end2_time-start_time}")
    return node
