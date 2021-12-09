from utils.test import *
from utils.sorts import bubble_sort, quick_sort, marge_sort, HeapSort
from utils import print_ex, print_passing_all
import random
import copy


def execute_heap_sort(hpsort, test_data):
    # construct heap
    for elem in test_data:
        hpsort.insert(elem)
    # inplace sort
    hpsort.implace_sort()
    hpsort.data = hpsort.data[::-1]

def execute_sort_for_bunch_data(func, ans_set, dataset, sort_type=None):
    last_data_idx = len(ans_set) - 1
    for i, (ans, data) in enumerate(zip(ans_set, dataset)):
        show_pass = True if i == last_data_idx else False
        if sort_type=='quick':
            execute_sort_test(func, ans, data, 0, len(data) - 1, show_pass=show_pass)
        elif sort_type=='heap':
            hpsort = HeapSort([])
            execute_sort_test(func, ans, hpsort, data, show_pass=show_pass)
        else:
            execute_sort_test(func, ans, data, show_pass=show_pass)

def create_new_data(dataset):
    for data in dataset:
        random.shuffle(data)

def create_copy_of_test_data(data, how_many=4):
    mul_test_data = []
    for _ in range(how_many):
        mul_test_data.append(copy.deepcopy(data))
    return mul_test_data


if __name__ == '__main__':
    #bbsort_test_data = [4, 5, 2, 6, 3]
    #bbsort_ans = [2, 3, 4, 5, 6]
    #execute_sort_test(bubble_sort, bbsort_ans, bbsort_test_data)
    #
    #qcsort_test_data = [6, 3, 5, 2, 4]
    #qc_length = len(qcsort_test_data)
    ##qcsort_ans = list(range(2, 10))
    #qcsort_ans = [2, 3, 4, 5, 6]
    #execute_sort_test(quick_sort, qcsort_ans, qcsort_test_data, 0, qc_length-1, show_pass=True)
    #
    #mgsort_test_data = [5, 7, 9, 4, 6, 8, 3, 2]
    #mgsort_ans = list(range(2, 10))
    #execute_sort_test(marge_sort, mgsort_ans, mgsort_test_data)
    #
    #hpsort_test = [12, 23, 24, 45, 18, 11, 34]
    #hpsort = HeapSort([])
    #hpsort_ans = [11, 12, 18, 23, 24, 34, 45]
    #execute_sort_test(execute_heap_sort, hpsort_ans, hpsort, hpsort_test)
    #print(hpsort.data)
    #hpsort.implace_sort()
    #print(hpsort.data[::-1])

    test_dataset = [[4, 5, 2, 6, 3],
                    [5, 6, 3, 9, 2, 8, 4, 7], 
                    [5, 7, 9, 4, 6, 8, 3, 2], 
                    [12, 23, 24, 45, 18, 11, 34]]
    ans_set = [[2, 3, 4, 5, 6],
               list(range(2, 10)),
               list(range(2, 10)),
               [11, 12, 18, 23, 24, 34, 45]]
    execute_sort_for_bunch_data(bubble_sort, ans_set, test_dataset)
    create_new_data(test_dataset)
    execute_sort_for_bunch_data(quick_sort, ans_set, test_dataset, sort_type='quick')
    create_new_data(test_dataset)
    execute_sort_for_bunch_data(marge_sort, ans_set, test_dataset)
    create_new_data(test_dataset)
    execute_sort_for_bunch_data(execute_heap_sort, ans_set, test_dataset, sort_type='heap')

    print_ex()

    test_data = [[18, 35, 76, 23, 49, 42, 31, 12]]
    ans = [[12, 18, 23, 31, 35, 42, 49, 76]]
    mul_test_data = create_copy_of_test_data(test_data)
    execute_sort_for_bunch_data(bubble_sort, ans, mul_test_data[0])
    execute_sort_for_bunch_data(quick_sort, ans, mul_test_data[1], sort_type='quick')
    execute_sort_for_bunch_data(marge_sort, ans, mul_test_data[2])
    execute_sort_for_bunch_data(execute_heap_sort, ans, mul_test_data[3], sort_type='heap')

    print_passing_all()