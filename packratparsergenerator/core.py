from packratparsergenerator.cache import Cache
from functools import wraps


def cache(func):
    name = func.__name__

    def kernel(*args):
        obj = args[0]
        args = args[1:]
        position = obj.position
        try:
            s = obj.cache.get(name, position, args)
            print("USED CACHE", position, s)
            return s
        except KeyError:
            print("NO CACHE", position)
            ans = func(obj, *args)
            obj.cache.set(name, position, args, ans)
            return ans

    return kernel


class Core:
    """Core PEG Class"""

    def __init__(self):
        self.position = 0
        self.src = None
        self.cache = None

    def _set_src(self, src: str):
        self.position = 0
        self.src = src
        self.cache = Cache()

    def _token(self):
        if self.position >= len(self.src):
            return ""
        return self.src[self.position]

    @cache
    def _TERMINAL(self, arg: str):
        print(self.position)
        if arg == self._token():
            self.position += 1
            return True
        else:
            return False

    @cache
    def _SEQUENCE(self, args):
        """True if all expressions match, then updates position, else false, no positional update"""
        LHS_func, LHS_arg = args[0]
        RHS_func, RHS_arg = args[1]
        tmp_pos = self.position
        bool = LHS_func(LHS_arg)
        if bool:
            bool = RHS_func(RHS_arg)
            if bool:
                return True
        self.position = tmp_pos
        return False

    @cache
    def _ORDERED_CHOICE(self, args):
        """True if one expression matches, then updates position, else false, no positional update"""
        LHS_func, LHS_arg = args[0]
        RHS_func, RHS_arg = args[1]
        tmp_pos = self.position
        bool = LHS_func(LHS_arg)
        if bool:
            return True
        self.position = tmp_pos
        bool = RHS_func(RHS_arg)
        if bool:
            return True
        self.position = tmp_pos
        return False

    @cache
    def _ZERO_OR_MORE(self, args):
        """Always True, increments position each time the expression matches else continues without doing anything"""
        temp_position = self.position
        func, arg = args
        while True:
            bool = func(arg)
            if bool:
                temp_position = self.position
                continue
            else:
                self.position = temp_position
                break
        return True

    @cache
    def _ONE_OR_MORE(self, args):
        """True if matches at least once, increments position each time the expression matches"""
        temp_position = self.position
        func, arg = args
        bool = func(arg)
        if bool:
            temp_position = self.position
        else:
            self.position = temp_position
            return False
        while True:
            bool = func(arg)
            if bool:
                temp_position = self.position
                continue
            else:
                self.position = temp_position
                break
        return True

    @cache
    def _OPTIONAL(self, args):
        """True if matches, False if not. Increments position on a match"""
        func, arg = args
        temp_position = self.position
        bool = func(arg)
        if bool:
            return True
        else:
            self.position = temp_position
            return False

    @cache
    def _AND_PREDICATE(self, args):
        """True if the function results in True, never increments position"""
        func, arg = args
        temp_position = self.position
        bool = func(arg)
        if bool:
            self.position = temp_position
            return True
        else:
            self.position = temp_position
            return False

    @cache
    def _NOT_PREDICATE(self, args):
        """True if the function results in False, never increments position"""
        bool = self._AND_PREDICATE(args)
        return not bool
