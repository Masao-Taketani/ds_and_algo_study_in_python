def sort(data):
    if len(data) <= 1:
        return data
    # pick a pivot from the first element
    pivot = data[0]
    left, right, same = [], [], 1

    for d in data[1:]:
        if d < pivot:
            left.append(d)
        elif d > pivot:
            right.append(d)
        else:
            same += 1

    left = sort(left)
    right = sort(right)

    return left + [pivot] * same + right
