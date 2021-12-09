from utils.utils import swap
from utils.ds import Heap


def bubble_sort(li):
    length = len(li)
    if length < 2:
        return li
    
    for i in range(length):
        for j in range(length - 1, i, -1):
            if li[j] < li[j-1]:
                swap(li, j, j-1)

    return li


def quick_sort(li, i, j):
    if i >= j or len(li) < 2:
        return

    def find_pivot(li, i, j):
        first = li[i]
        for val in li[i+1:j+1]:
            if first != val:
                if first > val:
                    return first
                else:
                    return val
        return None

    def partition(li, l, r, pivot):
        while(True):
            while(li[l] < pivot):
                l += 1
            while(li[r] >= pivot):
                r -= 1
            if l > r:
                return l
            swap(li, l, r)

    pivot = find_pivot(li, i, j)
    if pivot is None:
        return

    k = partition(li, i, j, pivot)
    quick_sort(li, i, k-1)
    quick_sort(li, k, j)


def marge_sort(li):
    length = len(li)
    if length < 2:
        return li

    def marge(left, right):
        result = []
        len_l, len_r = len(left), len(right)
        i, j = 0, 0
        while(True):
            if i < len_l and j < len_r and left[i] <= right[j] or j == len_r:
                result.append(left[i])
                i += 1
            elif i < len_l and j < len_r and right[j] < left[i] or i == len_l:
                result.append(right[j])
                j += 1

            if i == len_l and j == len_r:
                return result
    
    mid = length // 2
    left_li = marge_sort(li[:mid])
    right_li = marge_sort(li[mid:])
    return marge(left_li, right_li)


class HeapSort(Heap):

    def __init__(self, data=[]):
        super(Heap, self).__init__(data)
        if len(self.data) > 1:
            self.construct_heap()

    def insert(self, val):
        self.data.append(val)
        if len(self.data) > 1: self.construct_heap()

    def construct_heap(self, last_idx=None):
        if last_idx is None: last_idx = len(self.data) - 1
        length = last_idx + 1
        for i in range(length // 2 - 1, -1, -1):
            r_idx = 2 * i + 2
            l_idx = 2 * i + 1
            if r_idx > last_idx:
                min_idx = l_idx
            elif self.data[l_idx] >= self.data[r_idx]:
                min_idx = r_idx
            else:
                min_idx = l_idx
            
            if self.data[i] > self.data[min_idx]:
                swap(self.data, i, min_idx)

    def implace_sort(self):
        last_idx = len(self.data) - 1
        while(last_idx > 0):
            swap(self.data, 0, last_idx)
            last_idx -= 1
            self.construct_heap(last_idx)