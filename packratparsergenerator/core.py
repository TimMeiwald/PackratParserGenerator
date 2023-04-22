from packratparsergenerator.cache import Cache
from functools import wraps


def handle_direct_left_recursion(name, obj, func, *args):
    """Loop that keeps trying the function until the position doesn't change"""
    position = obj.position # Start of looping
    loop_position = obj.position
    
    while True:
        obj.cache.set(name, loop_position, args, (True, loop_position)) 
        bool = func(obj, *args)
        if(obj.position > loop_position):
            obj.cache.set(name, loop_position, args, (True, loop_position))
            loop_position = obj.position
            obj.cache.set(name, position, args, (bool, loop_position))
            continue
        else:
            break
    bool, pos = obj.cache.get(name, position, args)
    obj.position = pos
    return bool, pos

def direct_left_recursion(func):
    "Handles direct left recursion"
    name = func.__name__
    @wraps(func)
    def kernel(*args):
        obj = args[0]
        args = args[1:]
        position = obj.position
        try:
            bool, pos = obj.cache.get(name, position, args)
            if bool:
                obj.position = pos
            if(func.__name__ in ["And_Predicate", "Not_Predicate", "Optional", "Ordered_Choice", "Sequence", "Var_Name","_TERMINAL", "many_A"] and bool == True):
                print(f"k: Token: {position}, {func.__name__} -> '{obj.src[position:obj.position]}'")
            return bool
        except KeyError:
            bool, pos = handle_direct_left_recursion(name, obj, func, *args)
            obj.cache.set(name, pos, args, (bool, obj.position))
            if(func.__name__ in ["And_Predicate", "Not_Predicate", "Optional", "Ordered_Choice", "Sequence", "Var_Name", "_TERMINAL", "many_A"] and bool == True):
                print(f"nk: Token: {position}, {func.__name__} -> '{obj.src[position:obj.position]}'")
            return bool
    return kernel






def cache(func):
    """Handles regular PEG"""
    name = func.__name__
    @wraps(func)
    def kernel(*args):
        obj = args[0]
        args = args[1:]
        position = obj.position
        try:
            bool, pos = obj.cache.get(name, position, args)
            bool, pos = obj.cache.get(name, position, args)
            if bool:
                obj.position = pos
            if(func.__name__ in ["And_Predicate", "Not_Predicate", "Optional", "Ordered_Choice", "Sequence", "Var_Name","_TERMINAL", "many_A"] and bool == True):
                print(f"k: Token: {position}, {func.__name__} -> '{obj.src[position:obj.position]}'")
            return bool
        except KeyError:
            bool = func(obj, *args)
            obj.cache.set(name, position, args, (bool, obj.position))
            if(func.__name__ in ["And_Predicate", "Not_Predicate", "Optional", "Ordered_Choice", "Sequence", "Var_Name", "_TERMINAL", "many_A"] and bool == True):
                print(f"nk: Token: {position}, {func.__name__} -> '{obj.src[position:obj.position]}'")
            return bool

    return kernel





class Core:
    """Core PEG Class
    
    It seems that caching everything just slows things down
    caching at higher levels is much more valuable. So have disabled caching 
    at the intrinsic level."""

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
        if arg == self._token():
            self.position += 1
            return True
        else:
            return False

    #@cache
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

    #@cache
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

    #@cache
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

    #@cache
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

    #@cache
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

    #@cache
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

    #@cache
    def _NOT_PREDICATE(self, args):
        """True if the function results in False, never increments position"""
        bool = self._AND_PREDICATE(args)
        return not bool

    #@cache
    def _SUBEXPRESSION(self, args):
        """Subexpression is any expression inside a pair of () brackets
        SUBEXPR essentially does nothing but allows for order of precedent
        more importantly order of precedence is very restricted because it made my life hard
        (mostly because I can't find a good definition of what order of precedence is in PEG) so use SUBEXPR
        to make more complicated rules"""
        func, arg = args
        temp_position = self.position
        bool = func(arg)
        if bool:
            return True
        else:
            self.position = temp_position
            return False

    #@cache
    def _VAR_NAME(self, args):
        """True if called function evaluates to true else false, Is used to call other functions."""
        # where func is a grammar rule
        temp_position = self.position
        func, args = args
        bool = func(args)
        if bool:
            return True
        else:
            self.position = temp_position
            return False
