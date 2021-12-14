from utils.graphs import Prim
from utils.test import execute_prim_test

if __name__ == '__main__':
    V = [chr(i) for i in range(ord('a'), ord('a')+6)]
    E = [[{'a', 'b'}, 8], [{'a', 'c'}, 3], [{'a', 'd'}, 1], 
         [{'b', 'c'}, 9], [{'c', 'd'}, 4], [{'b', 'e'}, 2],
         [{'c', 'e'}, 7], [{'c', 'f'}, 6], [{'d', 'f'}, 5],
         [{'e', 'f'}, 10]]
    start_v = 'a'
    ans_list = [[{'a', 'c'}, {'a', 'd'}, {'d', 'f'}, {'c', 'e'}, {'b', 'e'}], 18]
    prim = Prim(V, E)
    execute_prim_test(prim.find_min_spanning_tree, ans_list, start_v)