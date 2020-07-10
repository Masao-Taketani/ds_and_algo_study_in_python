def sort(data):

    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
        # change positions between min_idx and where the sort is started
        data[i], data[min_idx] = data[min_idx], data[i]

    #print(data)
