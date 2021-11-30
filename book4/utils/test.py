import sys


class TestCase:
    def __init__(self, func):
        self.func = func
        self.test_name = self.get_test_name(func)

    def get_test_name(self, func):
        func_name = func.__name__
        test_name = 'test_' + func_name
        return test_name

    def calculate(self, *args):
        return self.func(*args)

    def check_val(self, ans, *val):
        val = self.calculate(*val)
        #print("val:", val)
        if val == ans:
            print(f'[PASS]{self.test_name}')
        else:
            print(f'[ERROR]{self.test_name}')
            raise Exception


def execute_test(func, ans, *args):
    ins = TestCase(func)
    ins.check_val(ans, *args)