def sort(data):
    # isolate all elements
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = sort(data[:mid])
    right = sort(data[mid:])
    # merge isolated elements
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while (i < len(left)) and (j < len(right)):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result.extend(left[i:])
    else:
        result.extend(right[j:])
    return result
