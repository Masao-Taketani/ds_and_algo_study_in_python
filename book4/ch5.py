from utils.graphs import Dijkstra


if __name__ == '__main__':
    name_list = ['s', 'a', 'b', 'c']
    weights_dict = {'s': {'a': 2, 'b': 6},
                    'a': {'b': 3},
                    'b': {'c': 2},
                    'c': {}}
    dijk = Dijkstra(name_list, weights_dict)
    dijk.find_shortest_path()
    print('final status:', dijk.current_status)