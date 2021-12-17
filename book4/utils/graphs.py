from typing import SupportsBytes
from utils.ds import NamedNode, EdgeNode, Heap, Queue, Stack
from utils.utils import swap
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


class Prim:

    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.seen = set()
    
    def find_min_spanning_tree(self, root_name):
        spanning_tree = []
        total_cost = 0
        v_len = len(self.V)
        self.seen.add(root_name)
        while(len(self.seen) != v_len):
            min_idx = None
            min_cost = float('inf')
            min_edge = None
            i = 0
            for e in self.E:
                renew_count = 0
                for node_name in e[0]:
                    if node_name in self.seen:
                        renew_count += 1
                if renew_count == 1 and min_cost > e[1]:
                    min_cost = e[1]
                    min_idx = i
                    min_edge = e[0]
                elif renew_count == 2:
                    continue
                i += 1
            if min_cost == float('inf'):
                continue
            else:
                spanning_tree.append(min_edge)
                total_cost += min_cost
                self._swap_and_delete_ith_elem(self.E, min_idx)
                for node_name in min_edge:
                    if node_name not in self.seen:
                        self.seen.add(node_name)
        return spanning_tree, total_cost

    def _swap_and_delete_ith_elem(self, li, i):
        last_idx = len(li) - 1
        swap(li, last_idx, i)
        li.pop()


class Kruscal:

    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.sub_trees = []
        for v in self.V:
            self.sub_trees.append(set(v))
        self._construct_heap()
    
    def find_min_spanning_tree(self):
        spanning_tree = []
        total_cost = 0
        while(len(self.heap.data)>0):
            min_node = self.heap.deletemin_node()
            renew = self._set_sub_trees(min_node.edge)
            if renew:
                spanning_tree.append(min_node.edge)
                total_cost += min_node.val
        return spanning_tree, total_cost

    def _construct_heap(self):
        new_E = []
        for e in self.E:
            new_E.append(EdgeNode(*e))
        self.heap = Heap(new_E, use_node=True)

    def _set_sub_trees(self, edge):
        renew = False
        for e in edge:
            for s in self.sub_trees:
                if e in s:
                    if self._is_subset(edge, s):
                        return
        renew = True
        connected_set = set()
        deletes = []
        for s in self.sub_trees:
            for e in edge:
                if e in s:
                    connected_set.update(s)
                    deletes.append(s)
        for d in deletes:
            self.sub_trees.remove(d)
        self.sub_trees.append(connected_set)
        return renew
                        
    def _is_subset(self, edge, s):
        count = 0
        for e in edge:
            if e in s:
                count += 1
        if count == 2:
            return True
        else:
            return False