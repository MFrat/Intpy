from test import Interceptor


class Test(Interceptor):

    def func(self, data):
        return "func1"

    def func2(self):
        return 'func2'

if __name__ == "__main__":
    test = Test()
    print(test.func(5))
    print(test.func2())
