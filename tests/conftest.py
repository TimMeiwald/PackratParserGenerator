from argparse import PARSER
import pytest
from . import TEST_RUN_COUNT


@pytest.fixture(autouse=True)
def parser():
    parser = parser_dynamic_load(TEST_RUN_COUNT)
    print(parser)
    parser = parser()
    return parser


@pytest.fixture(autouse=True)
def gparser():
    parser = gparser_dynamic_load(TEST_RUN_COUNT)
    print(parser)
    parser = parser()
    return parser


def gparser_dynamic_load(test_run_count):
    if (test_run_count == 1):
        from Generated_Output.parser import Grammar_Parser
        return Grammar_Parser
    else:
        from packratparsergenerator.parser.grammar_parser import Grammar_Parser
        return Grammar_Parser


def parser_dynamic_load(test_run_count):
    if (test_run_count == 1):
        from Generated_Output.parser import Parser
        return Parser
    else:
        from packratparsergenerator.parser.core_parser import Parser
        return Parser


def pytest_unconfigure(config):
    global TEST_RUN_COUNT
    if (TEST_RUN_COUNT == 0):
        TEST_RUN_COUNT += 1
        print("\n\n")
        print(80 * "#")
        print("#", 32 * " ", "NEW PARSER", 32 * " ", "#")
        print(80 * "#")
        pytest.main()
    else:
        return 0
