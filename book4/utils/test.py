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

    def check_heap(self, ans_list, *args):
        _ = self.calculate(*args)
        heap, _ = args
        if len(ans_list) != len(heap):
            print_error(self.test_name)
        for ans, out in zip(ans_list, heap.data):
            if ans != out:
                print_error(self.test_name)
        print_pass(self.test_name)

    def check_bst(self, ans_dict, *args):
        out_dict = self.calculate(*args)
        bst, _ = args
        for k, v in ans_dict.items():
            try:
                if out_dict[k] == v:
                    out_dict.pop(k)
            except KeyError:
                print_error(self.test_name)
        print_pass(self.test_name) if out_dict == {} else print_error(self.test_name)

    def check_hash(self, ans_dict, *args):
        out_dict = self.calculate(*args)
        hash, _ = args
        for k, v in ans_dict.items():
            try:
                if out_dict[k] == v:
                    out_dict.pop(k)
            except KeyError:
                print_error(self.test_name)
        print_pass(self.test_name) if out_dict == {} else print_error(self.test_name)


def print_pass(func_name):
    print(f'[PASS]{func_name}')

def print_error(func_name):
    print(f'[ERROR]{func_name}')
    raise Exception

def execute_val_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_val(ans, *args)

def execute_stack_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_stack(ans, *args)

def execute_queue_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_queue(ans, *args)

def execute_heap_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_heap(ans, *args)

def execute_bst_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_bst(ans, *args)

def execute_hash_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_hash(ans, *args)