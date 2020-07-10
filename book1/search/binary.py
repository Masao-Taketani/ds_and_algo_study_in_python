def search(data, value):
    # it assumes data to be sorted.
    left_idx = 0
    right_idx = len(data) - 1

    while True:
        mid_idx = (left_idx + right_idx) // 2

        if data[mid_idx] == value:
            return mid_idx
            break
        elif data[mid_idx] > value:
            right_idx = mid_idx - 1
        else:
            left_idx = mid_idx + 1

        if left_idx == right_idx:
            return None
