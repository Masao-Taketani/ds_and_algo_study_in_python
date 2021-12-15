import sys


def print_pass(func_name):
    print(f'[PASS]{func_name}')

def print_length_error(func_name, len_ans, len_out):
    print(f'[ERROR]{func_name} length expected: {len_ans}, got: {len_out}', file=sys.stderr)
    sys.exit(1)

def print_result_error(func_name, expected, got):
    print(f'[ERROR]{func_name} result expected: {expected}, got: {got}', file=sys.stderr)
    sys.exit(1)


class TestCase:
    def __init__(self, func, specified_name=None):
        self.func = func
        self.test_name = self.get_test_name(func) if specified_name is None else specified_name

    def get_test_name(self, func):
        func_name = func.__name__
        test_name = 'Test for ' + func_name
        return test_name

    def calculate(self, *args):
        return self.func(*args)

    def check_val(self, ans, val):
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

    def check_dict(self, ans_dict, out_dict, show_pass=True):
        for k, v in ans_dict.items():
            try:
                if out_dict[k] == v:
                    out_dict.pop(k)
            except KeyError:
                print('[KeyError]{self.func_name}')
        if show_pass:
            print_pass(self.test_name) if out_dict == {} else print_result_error(self.test_name, {}, out_dict)

    def check_sets_list(self, ans_sets_list, out_sets_list, show_pass=True):
        for out_set in out_sets_list:
            if out_set in ans_sets_list:
                continue
            else:
                print_result_error(self.test_name, ans_sets_list, out_sets_list)
        if show_pass:
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

    def check_ds_dict(self, ans_dict, *args):
        out_dict = self.calculate(*args)
        self.check_dict(ans_dict, out_dict)

    def check_sort_list(self, ans_list, *args, show_pass=True):
        out_list = self.calculate(*args)
        if out_list is None:
            out_list, _, _ = args
        self.check_list(ans_list, out_list, show_pass=show_pass)

# for ch2
def execute_val_test(func, ans, *args):
    tc = TestCase(func)
    val = tc.calculate(*args)
    tc.check_val(ans, val)

def execute_stack_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_instance_data(ans, *args)

def execute_queue_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_queue(ans, *args)

# for ch3
def execute_heap_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_instance_data(ans, *args)

def execute_bst_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_ds_dict(ans, *args)

def execute_hash_test(func, ans, *args):
    tc = TestCase(func)
    tc.check_ds_dict(ans, *args)

# for ch4
def execute_sort_test(func, ans, *args, show_pass=False):
    tc = TestCase(func)
    tc.check_instance_data(ans, *args, show_pass=show_pass) if len(args) == 2 else tc.check_sort_list(ans, *args, show_pass=show_pass)

# for ch5
def execute_dijkstra_test(func, ans_dict, ans_list, instance):
    tc = TestCase(func, 'Dijkstra')
    _ = tc.calculate()
    for key in instance.current_status.keys():
        continue
    tc.check_dict(ans_dict, instance.current_status, show_pass=False)
    tc.check_list(ans_list, instance.shortest_path_dict[key], show_pass=True)

def execute_bfs_dfs_test(func, ans_list, *args, specified_name):
    tc = TestCase(func, specified_name)
    out_list = tc.calculate(*args)
    tc.check_list(ans_list, out_list)

# for ch6
def execute_prim_test(func, ans_list, *args):
    tc = TestCase(func, "Prim's Algorithm")
    out_tuple = tc.calculate(*args)
    check_prim_or_kruscal(tc, ans_list, out_tuple)

def execute_kruscal_test(func, ans_list):
    tc = TestCase(func, "Kruscal's Algorithm")
    out_tuple = tc.calculate()
    check_prim_or_kruscal(tc, ans_list, out_tuple)

def check_prim_or_kruscal(tc, ans_list, out_tuple):
    out_sets_list, out_total_cost = out_tuple
    ans_sets_list, min_total_cost = ans_list
    tc.check_sets_list(ans_sets_list, out_sets_list, show_pass=False)
    tc.check_val(min_total_cost, out_total_cost)