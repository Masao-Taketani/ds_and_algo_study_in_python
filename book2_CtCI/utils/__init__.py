def check_true(method, args):
    result = check_instance_and_return_result(method, args)
    assert result == True, "An error occurred for case {}".format(args)


def check_all_true_cases(method, true_cases):
    for t in true_cases:
        check_true(method, t)
    print_success()


def check_false(method, args):
    result = check_instance_and_return_result(method, args)
    assert result == False, "An error occurred for case {}".format(args)


def check_all_false_cases(method, false_cases):
    for f in false_cases:
        check_false(method, f)
    print_success()


def print_success():
    print("passed the tests.")


def check_instance_and_return_result(method, args):
    """
    this function is used to differentiate the process
    when the args are single input such as int or str
    and multiple inputs such as list or tuples.
    """
    # check if t is instance of `int` or `str`
    if isinstance(args, (int, str)):
        result = method(args)
    else:
        result = method(*args)
    return result
