import copy


class LCS:
    """Stands for longest common subsequence"""
    def __init__(self, s1, s2):
        self.s1, self.s2 = s1, s2
        self.l1, self.l2= len(s1), len(s2)
        self.lcs_table = []

    def execute(self):
        # init lcs
        for i in range(self.l1+1):
            tmp = []
            for j in range(self.l2+1):
                tmp.append(0)
            self.lcs_table.append(tmp)

        for i in range(1, self.l1+1):
            for j in range(1, self.l2+1):
                self.lcs_table[i][j] = 1 + self.lcs_table[i-1][j-1] if self.s1[i-1] == self.s2[j-1] else max(self.lcs_table[i][j-1], self.lcs_table[i-1][j])

        s_list = []
        lcs_list = self.find_lcs(s_list, self.l1, self.l2)
        for i in range(len(lcs_list)):
            lcs_list[i] = lcs_list[i][::-1]
        return self.lcs_table[self.l1][self.l2], lcs_list

    def find_lcs(self, s_list, i, j):
        s2 = None
        if self.lcs_table[i-1][j-1] == self.lcs_table[i-1][j] and self.lcs_table[i-1][j-1] == self.lcs_table[i][j-1]:
            s_list.append(self.s2[j-1])
            if self.lcs_table[i-1][j-1] == 0:
                return [s_list]
            s1 = self.find_lcs(s_list, i-1, j-1)
        else:
            if self.lcs_table[i-1][j] > self.lcs_table[i][j-1]:
                s1 = self.find_lcs(s_list, i-1, j)
            elif self.lcs_table[i-1][j] < self.lcs_table[i][j-1]:
                s1 = self.find_lcs(s_list, i, j-1)
            else:
                s_list_copy = copy.deepcopy(s_list)
                s1 = self.find_lcs(s_list, i-1, j)
                s2 = self.find_lcs(s_list_copy, i, j-1)

        if s2 is None:
            return s1
        else:
            return s1 + s2