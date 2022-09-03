from packratparsergenerator.parser.grammar_parser import Grammar_Parser
from packratparsergenerator.parser.parser_pass_two import Parser_Pass_Two
from packratparsergenerator.grammar_compiler.grammar_compiler import Grammar_Compiler
from os import PathLike, getcwd
import os.path


class PackratParserGenerator():

    def __init__(self):
        self._src_filepath = None
        self._dest_filepath = None
        self._src = None

        self.parser = Grammar_Parser()
        self.parser_pass_two = Parser_Pass_Two()
        self.compiler = Grammar_Compiler()

    def generate(
            self,
            dryrun: bool = False,
            verbose: bool = True,
            pytest: bool = False):
        if (self._src is None):
            with open(self._src_filepath, "r") as fp:
                src = fp.read()
        elif (self._src_filepath is None):
            src = self._src
        else:
            raise ValueError(
                "You must provide either src or src_filepath via their respective methods set_src_filepath or set_src")
        print(f"src is \n{src}")
        # Parses
        self.parser._set_src(src)
        position, bool, node = self.parser.caller(0, self.parser.Grammar)
        if (verbose):
            print(f"Reached position: {position}")
            print(f"With Boolean result: {bool}")
            print("With Node before second_pass: \n")
            node.pretty_print()
            print("\n\n\n\n")
        if (position != len(src) or bool != True):
            raise Exception(
                f"Failed to Parse Grammar, Reached character: {position}")

        # Parser Pass Two
        self.parser_pass_two.parse(node)
        if (verbose):
            print("With Node after second_pass: \n")
            node.pretty_print()
            print("\n\n\n\n")

        if (dryrun):
            return None
        # Compiles
        ret_string = self.compiler.compile(node)
        if (verbose):
            print(ret_string, "\n")
        if (self._dest_filepath is None):
            raise ValueError(
                "You must set dest_filepath with it's method set_dest_filepath")
        else:
            with open(self._dest_filepath, "w") as fp:
                fp.write(ret_string)
        if (pytest):
            retcode = pytest.main()
        else:
            print("pytest is configured as off by default, set pytest path using associated set_pytest_path method\n and pass pytest=True as an argument to generate and automatically run pytest afterwards.")

    def set_src(self, src: str):
        if (self._src_filepath is not None):
            raise ValueError(
                "src_filepath and src cannot both be defined. Please only set src or src_filepath")
        self._src = src

    def set_src_filepath(
            self,
            src_filepath: str | PathLike,
            relative_path: bool = False,
            override: bool = False):
        if (self._src is not None):
            raise ValueError(
                "src_filepath and src cannot both be defined. Please only set src or src_filepath")
        if (os.path.exists(src_filepath) and override == False):
            raise FileExistsError(
                "This file already exists, please set override to true if you want it to overwrite the existing file.")
        if (relative_path):
            rel_path = getcwd()
            self._src_filepath = os.path.join(rel_path, src_filepath)
        else:
            self._src_filepath = src_filepath

    def set_dest_filepath(
            self,
            dest_filepath: str | PathLike,
            relative_path: bool = False,
            override: bool = False):
        if (os.path.exists(dest_filepath) and override == False):
            raise FileExistsError(
                "This file already exists, please set override to true if you want it to overwrite the existing file.")
        if (relative_path):
            rel_path = getcwd()
            self._dest_filepath = os.path.join(rel_path, dest_filepath)
        else:
            self._dest_filepath = dest_filepath
