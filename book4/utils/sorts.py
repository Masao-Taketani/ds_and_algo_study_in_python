from utils.utils import swap

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
    if i >= j or len(li) < 1:
        return

    def find_pivot(li, i, j):
        first = li[i]
        for val in li[1:j+1]:
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
        return li
    k = partition(li, i, j, pivot)
    quick_sort(li, i, k-1)
    quick_sort(li, k, j)

    return li