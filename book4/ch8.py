from utils.dp import LCS
from utils.test import execute_lcs_test


if __name__ == '__main__':
    s1, s2 = 'abcbdab', 'bdcaba'
    ans_list = (4, [['b', 'c', 'b', 'a'], ['b', 'c', 'a', 'b'], ['b', 'd', 'a', 'b']])
    lcs = LCS(s1, s2)
    execute_lcs_test(lcs.execute, ans_list)