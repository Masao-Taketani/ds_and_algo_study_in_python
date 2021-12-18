

def KMP(text, search_text, skip_table):
    i, j = 0, 0
    n, m = len(text), len(search_text)
    while(n-m > i):
        while(j<m and text[i+j]==search_text[j]):
            j += 1
        if j == m:
            return i
        i = i + skip_table[j]
        j = 0
    return False


if __name__ == '__main__':
    text = 'とくままくまくたたくまくまくたくまたま'
    search_text = 'くまくたくまた'
    skip_table = [1, 1, 3,  2, 5, 5, 4]
    print(KMP(text, search_text, skip_table))