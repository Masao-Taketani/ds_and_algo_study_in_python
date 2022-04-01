def KMP(text, search_text, skip_table):
    i, j = 0, 0
    n, m = len(text), len(search_text)
    while(n-m >= i):
        while(j<m and text[i+j]==search_text[j]):
            j += 1
        if j == m:
            return i
        i = i + skip_table[j]
        j = j - skip_table[j]
        if j == -1: j += 1
    return None


def BM(text, search_text, skip_table1, skip_table2):
    i = 0
    n, m = len(text), len(search_text)
    while(n-m >= i):
        j = m - 1
        while(j >= 0 and text[i+j] == search_text[j]):
            j -= 1
        if j == -1:
            return i
        skip = skip_table1[text[i+j]] + j - m + 1 if text[i+j] in skip_table1 else skip_table1['others'] 
        i = i + max(skip, skip_table2[j])
    return None