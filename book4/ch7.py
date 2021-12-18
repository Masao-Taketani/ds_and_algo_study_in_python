from utils.test import execute_val_test
from utils import print_ex, print_passing_all
from utils.strings import KMP, BM


if __name__ == '__main__':
    text = 'とくままくまくたたくまくまくたくまたま'
    search_text = 'くまくたくまた'
    skip_table = [1, 1, 3, 2, 5, 5, 4]
    ans = 11
    execute_val_test(KMP, ans, text, search_text, skip_table)

    text = 'くくまくまふくまひくまひくまふくまひ'
    search_text = 'ひくまふくま'
    len_st = len(search_text)
    skip_table1 = {'ひ': 5, 'く': 1, 'ま': 0, 'ふ': 2, 'others': len_st}
    skip_table2 = [len_st, len_st, len_st, 3, len_st, 1]
    ans = 11
    execute_val_test(BM, ans, text, search_text, skip_table1, skip_table2)

    print_ex()

    text = 'さあささうささよささうささうささん'
    search_text = 'ささうささん'
    skip_table = [1, 2, 1, 4, 5, 3]
    ans = 11
    execute_val_test(KMP, ans, text, search_text, skip_table)

    text = 'はんなりののみすぎのみみたのみもみのみ'
    search_text = 'たのみもみのみ'
    len_st = len(search_text)
    skip_table1 = {'た': 6, 'の': 1, 'み': 0, 'も': 3, 'others': len_st}
    skip_table2 = [len_st, len_st, len_st, len_st, 4, 2, 1]
    ans = 12
    execute_val_test(BM, ans, text, search_text, skip_table1, skip_table2)

    print_passing_all()