import time

from src.intpy import deterministic


class Test:
    @deterministic
    def func(self, data):
        a = 1 + 1
        time.sleep(2)
        return [data]

    @deterministic
    def func2(self):
        return 1234


@deterministic
def fib(n):
    if n < 2:
        return n

    return fib(n-1) + fib(n-2)


@deterministic
def quicksort(list):
    if len(list) <= 1:
        return list

    pivot = list[0]
    equal = [x for x in list if x == pivot]
    greater = [x for x in list if x > pivot]
    lesser = [x for x in list if x < pivot]

    return quicksort(lesser) + equal + quicksort(greater)


@deterministic
def pow(n, x):
    if x == 0:
        return 1

    return n*pow(n, x-1)


if __name__ == "__main__":
    print(fib(100))
    # test = Test()
    # print(test.func(1))
    # print(test.func2())
    # # print(func2())

    # print(quicksort([1, 2, 5, 2, 1, 0, 199, 2, 3]))
    # print(pow(2, 7))
    # print(fib(5))
