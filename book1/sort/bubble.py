def sort(data):
    for i in range(len(data)):
        # since bubble sort complete sorting from the back end,
        # it loops only for the non-sorted parts
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]

    #print(data)
