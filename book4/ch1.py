from utils.test import *
from utils import print_ex, print_passing_all

def Euclid(m, n):
    """Return the greatest common divisor"""
    i = 1
    while True:
        print(f'{i}th', m, n)
        r = m % n
        if r == 0:
            return n
        m = n
        n = r
        i += 1

def LinearSearch(A, b):
    for elem in A:
        print('element', elem)
        if elem == b:
            return True
    return False

def BinarySearch(A, b):
    print("List A", A)
    len_a = len(A)
    if len_a == 0:
        return False
    elif len_a == 1:
        if A[0] == b:
            return True
        else:
            return False

    mid_idx = len_a // 2
    if A[mid_idx] == b:
        return True
    elif A[mid_idx] < b:
        A = A[mid_idx+1:]
        return BinarySearch(A, b)
    else:
        A = A[:mid_idx]
        return BinarySearch(A, b)        


if __name__ == '__main__':
    execute_val_test(Euclid, 71, 1633, 355)
    A = list(range(1, 15, 3))
    print("List A:", A)
    execute_val_test(LinearSearch, True, A, 7)
    execute_val_test(LinearSearch, False, A, 8)
    execute_val_test(BinarySearch, True, A, 7)
    execute_val_test(BinarySearch, False, A, 8)
    B = [13, 16, 23, 45, 54, 58, 76, 91]
    execute_val_test(BinarySearch, False, B, 73)

    print_ex()
    execute_val_test(Euclid, 137, 3425, 1233)
    C = [12, 15, 19, 36, 38, 45, 56, 88]
    execute_val_test(BinarySearch, False, C, 34)

    print_passing_all()