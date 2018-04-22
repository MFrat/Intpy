from functools import wraps
import time

from .data_access import get_cache_data, create_entry
from .logger.log import debug


def get_cache(func, args):
    return get_cache_data(func.__name__, args)


def cache_exists(cache):
    return cache is not None


def cache_data(func, fun_args, fun_return, elapsed_time):
    debug("starting caching data for {0}".format(func.__name__))
    create_entry(func.__name__, fun_args, fun_return, elapsed_time)


def execute_func(f, self, *method_args, **method_kwargs):
    start = time.clock()
    result_value = f(self, *method_args, **method_kwargs)
    end = time.clock()

    elapsed_time = end - start

    debug("{0} took {1} to run".format(f.__name__, elapsed_time))

    return result_value, elapsed_time


def deterministic(f):
    @wraps(f)
    def wrapper(self, *method_args, **method_kwargs):
        debug("calling {0}".format(f.__name__))
        c = get_cache(f, method_args)
        if not cache_exists(c):
            debug("cache miss for {0}".format(f.__name__))
            return_value, elapsed_time = execute_func(f, self, *method_args, **method_kwargs)
            cache_data(f, method_args, return_value, elapsed_time)
            return return_value
        else:
            debug("cache hit for {0}".format(f.__name__))
            return c

    return wrapper
