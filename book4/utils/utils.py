def swap(lis, idx1, idx2):
    if idx1 == idx2:
        return
    tmp = lis[idx1]
    lis[idx1] = lis[idx2]
    lis[idx2] = tmp