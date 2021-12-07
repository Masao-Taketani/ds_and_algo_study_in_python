from utils.test import *
from utils.sorts import bubble_sort, quick_sort, marge_sort, HeapSort
from utils import print_ex, print_passing_all


if __name__ == '__main__':
    bbsort_test_data = [4, 5, 2, 6, 3]
    bbsort_ans = [2, 3, 4, 5, 6]
    execute_sort_test(bubble_sort, bbsort_ans, bbsort_test_data)

    qcsort_test_data = [5, 6, 3, 9, 2, 8, 4, 7]
    qc_length = len(qcsort_test_data)
    qcsort_ans = list(range(2, 10))
    execute_sort_test(quick_sort, qcsort_ans, qcsort_test_data, 0, qc_length-1)
    
    mgsort_test_data = [5, 7, 9, 4, 6, 8, 3, 2]
    mgsort_ans = list(range(2, 10))
    execute_sort_test(marge_sort, mgsort_ans, mgsort_test_data)

    hpsort = HeapSort([12, 23, 24, 45, 18, 11, 34])
    print(hpsort.data)