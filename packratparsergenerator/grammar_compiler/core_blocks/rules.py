from enum import IntEnum


class Rules(IntEnum):
    _ROOT = 0
    _TERMINAL = 1
    _SEQUENCE = 2
    _ORDERED_CHOICE = 3
    _NOT_PREDICATE = 4
    _AND_PREDICATE = 5
    _OPTIONAL = 6
    _ZERO_OR_MORE = 7
    _ONE_OR_MORE = 8
    _SUBEXPRESSION = 10
    _VAR_NAME = 11
    _test = 12
