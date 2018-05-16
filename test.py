import time

from src.intpy import deterministic


class Test:
    @deterministic
    def func(self, data):
        time.sleep(2)
        return [data]

    @deterministic
    def func2(self):
        return 1234


@deterministic
def func2():
    return "data"


@deterministic
def fib(n):
    if n <= 1:
        return n

    return fib(n-1) + fib(n-2)


if __name__ == "__main__":
    # test = Test()
    # print(test.func(Teste(2)))
    # print(test.func(1))
    # print(test.func2())
    # # print(func2())

    print(fib(10))
