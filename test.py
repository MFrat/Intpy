import time
from functools import wraps
from intpy import deterministic


class Test:
    @deterministic()
    def func(self, data):
        time.sleep(2)
        return "func1 {0}".format(data)

    @deterministic()
    def func2(self):
        return 'func2'

if __name__ == "__main__":
    test = Test()
    print(test.func(123))