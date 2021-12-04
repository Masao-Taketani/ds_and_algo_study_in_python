from utils.test import *
from utils.ds import Heap, BST, Hash
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
        result_dict = bst.convert_bst_to_dict()
        print(result_dict)
    return result_dict

def execute_hash(hs, test_data):
    for elem in test_data:
        if '_' in elem:
            val = elem.split('_')[1]
            hs.delete(val)
        else:
            hs.insert(elem)
        result_dict = hs.convert_hash_to_dict()
        print(result_dict)
    return result_dict


if __name__ == '__main__': 
    heap_test_data = [31, 21, 48, 9, 'delete', 26, 13, 'delete']
    heap_ans = [21, 26, 48, 31]
    heap = Heap([])
    execute_heap_test(execute_heap, heap_ans, heap, heap_test_data)
    bst_test_data = [34, 51, 72, 17, 66, 'delete_51', 'delete_34']
    bst_ans = {0: 66, 1: 17, 2: 72}
    bst = BST(None, left=None, right=None)
    execute_bst_test(execute_bst, bst_ans, bst, bst_test_data)
    hash_test_data = ['dog', 'bird', 'cat', 'delete_dog', 'rat']
    hash_ans = {3: ['rat', 'cat'], 4: ['bird']}
    def hash_func(string):
        return len(string)
    hs = Hash(5, hash_func, None)
    execute_hash_test(execute_hash, hash_ans, hs, hash_test_data)

    print_ex()

    heap_test_data = [12, 24, 8, 16, 'delete', 14, 'delete']
    heap_ans = [14, 16, 24]
    heap_ex = Heap([])
    execute_heap_test(execute_heap, heap_ans, heap_ex, heap_test_data)
    bst_test_data = [12, 24, 8, 16, 6, 'delete_8', 'delete_12']
    bst_ans = {0: 16, 1: 6, 2: 24}
    bst_ex = BST(None, left=None, right=None)
    execute_bst_test(execute_bst, bst_ans, bst_ex, bst_test_data)
    hash_test_data = ['うま', 'かめ', 'へび', 'きつね', 'delete_かめ']
    hash_ans = {2: ['へび', 'うま'], 3: ['きつね']}
    hs_ex = Hash(5, hash_func, None)
    execute_hash_test(execute_hash, hash_ans, hs_ex, hash_test_data)

    print_passing_all()