if __name__ == "__main__":
    from grammar_parser import Grammar_Parser
    parser = Grammar_Parser()
    from os import getcwd
    from os.path import join
    path = join(getcwd(), "src", "Grammar.txt")
    with open(path, "r") as fp:
        src = fp.read()
    print(f"Length of File is : {len(src)}")
    parser._set_src(src)

    #tup = (parser.Grammar, None)
    #position, bool, node = parser._VAR_NAME(0, tup)
    #parser.pretty_print(node)
    #print(position, bool)
    #print(len(src))
    position = 0
    position_two, bool_two = -1,-1
    while(True):
        tup = (parser.Rule, None)
        position, bool, node = parser._VAR_NAME(position, tup)
        print(position, bool)
        parser.pretty_print(node)
        if((position, bool) == (position_two, bool_two)):
            break
        position_two, bool_two = position, bool
    print(src[position:])