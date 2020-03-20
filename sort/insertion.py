def sort(data):
    # check if each i is smaller than the temporary sorted values
    for i in range(1, len(data)):
        tmp = data[i]
        j = i - 1
        while (j >= 0) and (data[j] > tmp):
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = tmp

    print(data)
