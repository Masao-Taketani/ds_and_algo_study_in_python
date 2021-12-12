from utils.ds import NamedNode, Heap


class Dijkstra:
    def __init__(self, name_list, weights_dict):
        self.max_len = len(name_list)
        self.weights_dict = weights_dict
        self.current_status = {name_list[0]: 0}
        for name in name_list[1:]:
            self.current_status[name] = float('inf')

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