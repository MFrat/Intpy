import inspect
from functools import wraps


def interceptor(f):
    def cached(cached_data=None):
        return "cached data: {0}".format(cached_data)

    def get_cache(func):
        return "cached data" if func.__name__ == "func2" else None

    @wraps(f)
    def wrapper(self, *method_args, **method_kwargs):
        c = get_cache(f)
        return cached(cached_data=c) if c is not None else f(self, *method_args, **method_kwargs)

    return wrapper


class Test:
    @interceptor
    def func(self, data):
        return "func1 {0}".format(data)

    @interceptor
    def func2(self):
        return 'func2'

if __name__ == "__main__":
    test = Test()
    print(test.func(2))
    print(test.func2())
