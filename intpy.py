from functools import wraps

from data_access import get_cache_data, create_entry

def get_cache(func, args):
    return get_cache_data(func.__name__, args)

def cache_exists(cache):
    return cache is not None

def cache_data(func, fun_args, fun_return):
    create_entry(func.__name__, fun_args, fun_return)

def deterministic():
    def fun(f):
        @wraps(f)
        def wrapper(self, *method_args, **method_kwargs):
            c = get_cache(f, method_args)
            if not cache_exists(c):
                return_value = f(self, *method_args, **method_kwargs)
                cache_data(f, method_args, return_value)
                return return_value
            else:
                return c
        return wrapper
    return fun