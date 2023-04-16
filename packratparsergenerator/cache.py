import pprint


class Cache:
    def __init__(self):
        self._cache = {}

    def set(self, func, position, args, bool):
        self._cache[func, position, args] = bool

    def get(self, func, position, args):
        return self._cache[func, position, args]

    def __repr__(self):
        return pprint.pformat(self._cache)
