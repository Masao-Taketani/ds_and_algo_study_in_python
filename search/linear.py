def search(data, value):

    for idx in range(len(data)):
        if data[idx] == value:
            return idx
            break
    return None
