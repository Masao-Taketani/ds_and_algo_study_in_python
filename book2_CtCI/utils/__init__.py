from copy import deepcopy

ERROR_MGS = "An error occurred for case "

def check_true(method, args):
    result = check_instance_and_return_result(method, args)
    assert result == True, ERROR_MGS + "{}".format(args)


def check_all_true_cases(method, true_cases):
    for t in true_cases:
        check_true(method, t)
    print_success()


def check_false(method, args):
    result = check_instance_and_return_result(method, args)
    assert result == False, ERROR_MGS + "{}".format(args)


def check_all_false_cases(method, false_cases):
    for f in false_cases:
        check_false(method, f)
    print_success()


def check_equal(method, args, ans):
    result = check_instance_and_return_result(method, args)
    assert result == ans, ERROR_MGS + "{}. " \
                          "Expected {} Obtained {}".format(args, ans, result)


def check_all_equal_cases(method, test_cases):
    for inp, ans in test_cases:
        check_equal(method, inp, ans)
    print_success()


def print_success():
    print("passed the tests.")


def check_instance_and_return_result(method, args):
    """
    this function is used to differentiate the process
    when the args are single input such as int or str
    and multiple inputs such as list or tuples.
    """
    # check if args is instance of `int`, `str` or 'list'.
    # otherwise treat it as a tuple.
    if isinstance(args, (int, str, list)):
        args = deepcopy(args)
        result = method(args)
    else:
        result = method(*args)
    return result
