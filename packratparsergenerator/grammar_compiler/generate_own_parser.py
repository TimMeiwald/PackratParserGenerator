if __name__ == "__main__":
    from packratparsergenerator.packratparsergenerator import PackratParserGenerator
    pgen = PackratParserGenerator()
    pgen.set_dest_filepath("C:\\Users\\timme\\Desktop\\MyPythonPackages\\PackratParserGenerator\\Generated_Output\\parser.py", override=True)
    pgen.set_src_filepath("packratparsergenerator\\parser\\Grammar.txt", relative_path=True, override=True)
    pgen.generate()

