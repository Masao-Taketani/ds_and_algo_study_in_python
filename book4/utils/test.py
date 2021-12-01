class TestCase:
    def __init__(self, func):
        self.func = func
        self.test_name = self.get_test_name(func)

    def get_test_name(self, func):
        func_name = func.__name__
        test_name = 'Test for ' + func_name
        return test_name

    def calculate(self, *args):
        return self.func(*args)

    def check_val(self, ans, *val):
        val = self.calculate(*val)
        if val == ans:
            print_pass(self.test_name)
        else:
            print_error(self.test_name)

    def check_stack(self, ans_list, *args):
        _ = self.calculate(*args)
        stack, _ = args
        if len(ans_list) != len(stack):
            print_error(self.test_name)
        for ans, out in zip(ans_list, stack.data):
            if ans != out:
                print_error(self.test_name)
        print_pass(self.test_name)

    def check_queue(self, ans_list, *args):
        _ = self.calculate(*args)
        queue, _ = args
        modified_queue = []
        for elem in queue.data:
            if elem != float('inf'):
                modified_queue.append(elem)
        if len(ans_list) != len(modified_queue):
            print_error(self.test_name)
        for ans, out in zip(ans_list, modified_queue):
            if ans != out:
                print_error(self.test_name)
        print_pass(self.test_name)


def print_pass(func_name):
    print(f'[PASS]{func_name}')

def print_error(func_name):
    print(f'[ERROR]{func_name}')
    raise Exception

def execute_val_test(func, ans, *args):
    ins = TestCase(func)
    ins.check_val(ans, *args)

def execute_stack_test(func, ans, *args):
    ins = TestCase(func)
    ins.check_stack(ans, *args)

def execute_queue_test(func, ans, *args):
    ins = TestCase(func)
    ins.check_queue(ans, *args)