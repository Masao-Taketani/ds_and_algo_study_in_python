import sys


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
            print_result_error(self.test_name, ans, val)

    def check_list(self, ans_list, out_list, show_pass=True):
        if len(ans_list) != len(out_list):
            print_length_error(self.test_name, len(ans_list), len(out_list))
        for ans, out in zip(ans_list, out_list):
            if ans != out:
                print_result_error(self.test_name, ans_list, out_list)
        if show_pass==True:
            print_pass(self.test_name)

    def check_instance_data(self, ans_list, *args, show_pass=True):
        _ = self.calculate(*args)
        instance, _ = args
        self.check_list(ans_list, instance.data, show_pass=show_pass)

    def check_queue(self, ans_list, *args):
        _ = self.calculate(*args)
        queue, _ = args
        modified_queue = []
        for elem in queue.data:
            if elem != float('inf'):
                modified_queue.append(elem)
        self.check_list(ans_list, modified_queue)

    def check_dict(self, ans_dict, *args):
        out_dict = self.calculate(*args)
        for k, v in ans_dict.items():
            try:
                if out_dict[k] == v:
                    out_dict.pop(k)
            except KeyError:
                print('[KeyError]{self.func_name}')
            print_pass(self.test_name) if out_dict == {} else print_result_error(self.test_name, {}, out_dict)

    def check_sort_list(self, ans_list, *args, show_pass=True):
        out_list = self.calculate(*args)
        if out_list is None:
            out_list, _, _ = args
        self.check_list(ans_list, out_list, show_pass=show_pass)


def print_pass(func_name):
    print(f'[PASS]{func_name}')

def print_length_error(func_name, len_ans, len_out):
    print(f'[ERROR]{func_name} length expected: {len_ans}, got: {len_out}', file=sys.stderr)
    sys.exit(1)

def print_result_error(func_name, expected, got):
    print(f'[ERROR]{func_name} result expected: {expected}, got: {got}', file=sys.stderr)
    sys.exit(1)

# execute test for ch2
def execute_val_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_val(ans, *args)

def execute_stack_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_instance_data(ans, *args)

def execute_queue_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_queue(ans, *args)

# execute test for ch3
def execute_heap_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_instance_data(ans, *args)

def execute_bst_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_dict(ans, *args)

def execute_hash_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_dict(ans, *args)

# execute test for ch4
def execute_sort_test(func, ans, *args, show_pass=False):
    tc = TestCase(func)
    tc.check_instance_data(ans, *args, show_pass=show_pass) if len(args) == 2 else tc.check_sort_list(ans, *args, show_pass=show_pass)