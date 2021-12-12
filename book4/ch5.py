from utils.graphs import Dijkstra
from utils.test import execute_dijkstra_test


def execute_dijkstra(name_list, weights_dict):
    execute_dijkstra_test()

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
    #dijk = Dijkstra(name_list, weights_dict)
    #dijk.find_shortest_path()
    #print('final status:', dijk.current_status)
    #print('shortest paths;', dijk.shortest_path)
