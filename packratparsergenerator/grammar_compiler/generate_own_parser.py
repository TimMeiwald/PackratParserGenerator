if __name__ == "__main__":
    from packratparsergenerator.packratparsergenerator import PackratParserGenerator
    pgen = PackratParserGenerator()
    pgen.set_dest_filepath(
        "packratparsergenerator\\Generated_Output\\rust_parser.rs",
        override=True, relative_path=True)
    pgen.set_src_filepath(
        "packratparsergenerator\\parser\\Grammar.txt",
        relative_path=True,
        override=True)
    pgen.generate()


