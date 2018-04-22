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
def load_data():
    return "data"


if __name__ == "__main__":
    test = Test()
    print(test.func({"key": 1}))
    print(test.func({"key": 1}))
    print(test.func2())

    print(load_data())
