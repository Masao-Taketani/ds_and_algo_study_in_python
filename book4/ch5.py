from utils.graphs import Dijkstra, BFS, DFS
from utils.test import execute_dijkstra_test, execute_bfs_dfs_test
from utils import print_ex, print_passing_all


def execute_dijkstra_with_batch(ans_dicts_list, ans_lists_list, name_lists_list, weights_dicts_list):
    for ans_dict, and_list, name_list, weights_dict in zip(ans_dicts_list, ans_lists_list, name_lists_list, weights_dicts_list):
        dijk = Dijkstra(name_list, weights_dict)
        execute_dijkstra_test(dijk.find_shortest_path, ans_dict, and_list, dijk)


if __name__ == '__main__':
    name_lists_list = [['s', 'a', 'b', 'c'],
                       [chr(i) for i in range(ord('a'), ord('a')+8)]]
    weights_dicts_list = [{'s': {'a': 2, 'b': 6},
                           'a': {'b': 3},
                           'b': {'c': 2},
                           'c': {}},
                          {'a': {'b': 5, 'c': 4, 'd': 1},
                           'b': {'e': 2},
                           'c': {'e': 5, 'f': 6},
                           'd': {'c': 2},
                           'e': {'g': 1, 'h': 3},
                           'f': {'h': 2},
                           'g': {'h': 4},
                           'h': {}}]
    ans_dicts_list = [{'s': 0, 'a': 2, 'b': 5, 'c': 7},
                      {'a': 0, 'b': 5, 'c': 3, 'd': 1, 'e': 7, 'f': 9, 'g': 8, 'h': 10}]
    ans_lists_list = [['s', 'a', 'b', 'c'],
                       ['a', 'b', 'e', 'h']]
    execute_dijkstra_with_batch(ans_dicts_list, ans_lists_list, name_lists_list, weights_dicts_list)
    adjacent_dict = {'a': ['b', 'c'],
                     'b': ['d', 'e'],
                     'c': ['f'],
                     'd': [],
                     'e': [],
                     'f': ['g'],
                     'g': []}
    bfs_ans_list = [chr(i) for i in range(ord('a'), ord('a')+7)]
    dfs_ans_list = ['a', 'c', 'f', 'g', 'b', 'e', 'd']
    bfs = BFS()
    dfs = DFS()
    execute_bfs_dfs_test(bfs.find_path, bfs_ans_list, adjacent_dict, specified_name='BFS')
    execute_bfs_dfs_test(dfs.find_path, dfs_ans_list, adjacent_dict, specified_name='DFS')

    print_ex()
    
    name_lists_list = [['s', 'a', 'b', 'c']]
    weights_dicts_list = [{'s': {'a': 6, 'b': 1},
                           'a': {'c': 1},
                           'b': {'a': 2, 'c': 4},
                           'c': {}}]
    ans_dicts_list = [{'s': 0, 'a': 3, 'b': 1, 'c': 4}]
    ans_lists_list = [['s', 'b', 'a', 'c']]
    execute_dijkstra_with_batch(ans_dicts_list, ans_lists_list, name_lists_list, weights_dicts_list)

    print_passing_all()