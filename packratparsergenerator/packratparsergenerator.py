from parser.grammar_parser import Grammar_Parser
from parser.parser_pass_two import Parser_Pass_Two
from grammar_compiler.grammar_compiler import Grammar_Compiler
from os import PathLike, getcwd
import os.path
from time import time

class Packrat_Parser_Generator():

    def __init__(self):
        self._src_filepath = None
        self._dest_filepath = None
        self._src = None

        self.parser = Grammar_Parser()
        self.parser_pass_two = Parser_Pass_Two()
        self.compiler = Grammar_Compiler()
        
    def generate(self, dryrun: bool = False, verbose: bool = True):
        if(self._src == None):
            with open(self._src_filepath, "r") as fp:
                src = fp.read()
        elif(self._src_filepath == None):
            src = self._src
        else:
            raise ValueError("You must provide either src or src_filepath via their respective methods set_src_filepath or set_src")
        
        # Parses
        self.parser._set_src(self._src)
        position, bool, node = self.parser.caller(0, self.parser.Grammar)
        if(verbose):
            print(f"Reached position: {position}")
            print(f"With Boolean result: {bool}")
            print("With Node before second_pass: \n")
            node.pretty_print()
            print("\n\n\n\n")
        if(position != len(src) or bool != True):
            raise Exception(f"Failed to Parse Grammar, Reached character: {position}")
        
        # Parser Pass Two
        node = self.parser_pass_two.parse(node)
        if(verbose):
            print("With Node after second_pass: \n")
            node.pretty_print()
            print("\n\n\n\n")

        if(dryrun):
            return None
        # Compiles
        if(self._dest_filepath == None):
            # TODO: Rework Grammar_Compiler to return string so that this class can choose what to do with it
            raise ValueError("You must set dest_filepath with it's method set_dest_filepath")
        self.compiler.compile(node, self._dest_filepath)
        if(print):
            with open(self._dest_filepath, "r") as fp:
                parser = fp.read()
                fp.print()

    def set_src(self, src: str):
        if(self._src_filepath != None):
            raise ValueError("src_filepath and src cannot both be defined. Please only set src or src_filepath")
        self._src = src

    def set_src_filepath(self, src_filepath: str | PathLike, relative_path: bool = False, override: bool = False):
        if(self._src != None):
            raise ValueError("src_filepath and src cannot both be defined. Please only set src or src_filepath")
        if(os.path.exists(src_filepath)):
            raise FileExistsError("This file already exists, please set override to true if you want it to overwrite the existing file.")
        if(relative_path):
            rel_path = getcwd()
            self._src_filepath = os.path.join(rel_path, src_filepath)
        else:
            self._src_filepath = src_filepath

    def set_dest_filepath(self, dest_filepath: str | PathLike, relative_path: bool = False, override: bool = False):
        if(self._src != None):
            raise ValueError("src_filepath and src cannot both be defined. Please only set src or src_filepath")
        if(os.path.exists(dest_filepath)):
            raise FileExistsError("This file already exists, please set override to true if you want it to overwrite the existing file.")
        if(relative_path):
            rel_path = getcwd()
            self._dest_filepath = os.path.join(rel_path, dest_filepath)
        else:
            self._dest_filepath = dest_filepath
