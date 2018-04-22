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


if __name__ == "__main__":
    test = Test()
    print(test.func("asdasd"))
    print(test.func2())
