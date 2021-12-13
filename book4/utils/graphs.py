from utils.ds import NamedNode, Heap, Queue, Stack
import copy


class Graph:
    def __init__(self, ds, start_letter='a'):
        self.ds = ds()
        self.seen = set()
        self.start_letter = start_letter

    def find_path(self, adjacent_dict):
        path_list = []
        self.ds.push(self.start_letter) if isinstance(self.ds, Stack) else self.ds.enqueue(self.start_letter)
        while(len(self.ds) > 0):
            if isinstance(self.ds, Stack):
                v = self.ds.pop()
            else:
                if not self.ds.check_circular_array_empty():
                    v = self.ds.dequeue()
                else:
                    break
            path_list.append(v)
            adj_v = adjacent_dict[v]
            for av in adj_v:
                 self.ds.push(av) if isinstance(self.ds, Stack) else self.ds.enqueue(av)
        return path_list


class BFS(Graph):
    def __init__(self, start_letter='a'):
        super(BFS, self).__init__(Queue, start_letter=start_letter)


class DFS(Graph):
    def __init__(self, start_letter='a'):
        super(DFS, self).__init__(Stack, start_letter=start_letter)


class Dijkstra:
    def __init__(self, name_list, weights_dict):
        self.max_len = len(name_list)
        self.weights_dict = weights_dict
        self.current_status = {name_list[0]: 0}
        self.shortest_path_dict = {name_list[0]: [name_list[0]]}
        for name in name_list[1:]:
            self.current_status[name] = float('inf')
            self.shortest_path_dict[name] = []

        self.heap = Heap([NamedNode(name_list[0], 0)], use_node=True)
        self.seen = set()

    def find_shortest_path(self):
        while(len(self.heap)):
            min_node = self.heap.deletemin_node()
            if min_node.name in self.seen:
                continue
            else:
                self.seen.add(min_node.name)
                to_dict = self.weights_dict[min_node.name]
                if to_dict == {}:
                    break
                for name, weight in to_dict.items():
                    self.heap.insert_node(NamedNode(name, weight))
                    comp_val = self.current_status[min_node.name] + weight
                    if self.current_status[name] > comp_val:
                        self.current_status[name] = comp_val
                        self.shortest_path_dict[name] = copy.deepcopy(self.shortest_path_dict[min_node.name])
                        self.shortest_path_dict[name].append(name)