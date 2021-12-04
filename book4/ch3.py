from utils.test import *
from utils.ds import Heap, BST
from utils import print_ex, print_passing_all


def execute_heap(heap, test_data):
    for elem in test_data:
        heap.deletemin() if elem == 'delete' else heap.insert(elem)
        print(heap.data)

def execute_bst(bst, test_data):
    for elem in test_data:
        if isinstance(elem, str):
            val = elem.split('_')[1]
            bst.delete(int(val))
        else:
            bst.insert(elem)
        print(convert_bst_to_dict(bst))
    return convert_bst_to_dict(bst)


if __name__ == '__main__': 
    heap_test_data = [31, 21, 48, 9, 'delete', 26, 13, 'delete']
    heap_ans = [21, 26, 48, 31]
    heap = Heap()
    execute_heap_test(execute_heap, heap_ans, heap, heap_test_data)
    bst_test_data = [34, 51, 72, 17, 66, 'delete_51', 'delete_34']
    bst_ans = {0: 66, 1: 17, 2: 72}
    bst = BST(None, left=None, right=None)
    execute_bst_test(execute_bst, bst_ans, bst, bst_test_data)