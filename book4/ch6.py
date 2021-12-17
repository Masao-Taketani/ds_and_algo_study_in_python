from utils.graphs import Prim, Kruscal
from utils.test import execute_prim_test, execute_kruscal_test
import copy
from utils import print_ex, print_passing_all


def copy_V_and_E(V, E):
     return copy.deepcopy(V), copy.deepcopy(E)


if __name__ == '__main__':
     V = [chr(i) for i in range(ord('a'), ord('a')+6)]
     E = [[{'a', 'b'}, 8], [{'a', 'c'}, 3], [{'a', 'd'}, 1], 
         [{'b', 'c'}, 9], [{'c', 'd'}, 4], [{'b', 'e'}, 2],
         [{'c', 'e'}, 7], [{'c', 'f'}, 6], [{'d', 'f'}, 5],
         [{'e', 'f'}, 10]]
     V1, E1 = copy_V_and_E(V, E)
     start_v = 'a'
     ans_list = [[{'a', 'c'}, {'a', 'd'}, {'d', 'f'}, {'c', 'e'}, {'b', 'e'}], 18]
     prim = Prim(V1, E1)
     execute_prim_test(prim.find_min_spanning_tree, ans_list, start_v)
     V2, E2 = copy_V_and_E(V, E)
     kruscal = Kruscal(V2, E2)
     execute_kruscal_test(kruscal.find_min_spanning_tree, ans_list)

     print_ex()

     V = [chr(i) for i in range(ord('a'), ord('a')+6)]
     E = [[{'a', 'b'}, 5], [{'b', 'c'}, 7], [{'a', 'd'}, 1], 
         [{'a', 'e'}, 4], [{'d', 'e'}, 2], [{'b', 'e'}, 6],
         [{'c', 'e'}, 8], [{'c', 'f'}, 3], [{'e', 'f'}, 9]]
     V1, E1 = copy_V_and_E(V, E)
     start_v = 'a'
     ans_list = [[{'a', 'b'}, {'a', 'd'}, {'d', 'e'}, {'b', 'c'}, {'c', 'f'}], 18]
     prim = Prim(V1, E1)
     execute_prim_test(prim.find_min_spanning_tree, ans_list, start_v)
     V2, E2 = copy_V_and_E(V, E)
     kruscal = Kruscal(V2, E2)
     execute_kruscal_test(kruscal.find_min_spanning_tree, ans_list)