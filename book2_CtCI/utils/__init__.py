def check_true(method, args):
    result = method(args)
    assert result == True, "An error occurred for case {}".format(args)

def check_all_true_cases(method, true_cases):
    for t in true_cases:
        check_true(method, t)
    print_success()

def check_false(method, args):
    result = method(args)
    assert result == False, "An error occurred for case {}".format(args)

def check_all_false_cases(method, false_cases):
    for f in false_cases:
        check_false(method, f)
    print_success()

def print_success():
    print("passed the tests.")
