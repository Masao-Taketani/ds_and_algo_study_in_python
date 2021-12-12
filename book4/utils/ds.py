from utils.utils import swap

EMPTY_MESSAGE = 'Empty. There is no data.'

class Base:

    def __init__(self, data=[]):
        self.data = data

    def __len__(self):
        return len(self.data)

    def check_empty(self):
        assert len(self) != 0, EMPTY_MESSAGE


class Stack(Base):

    def __init__(self, data=[]):
        super(Stack, self).__init__(data)

    def push(self, val):
        self.data.append(val)
    
    def pop(self):
        self.check_empty()
        val = self.data.pop()
        return val


class Queue(Base):

    def __init__(self, data=[], max_elem=8, init_val=float('inf')):
        super(Queue, self).__init__(data)
        self.first_idx, self.last_idx = None, None
        self.max_elem = max_elem
        self.init_val = init_val
        if len(data) == 0:
            for i in range(max_elem):
                data.append(init_val)
        else:
            self.last_idx = len(data) - 1
        self.data = data
    
    def increment_idx(self, idx):
        idx += 1
        idx = self.check_max_idx(idx)
        return idx

    def check_max_idx(self, idx):
        if idx >= self.max_elem:
            idx = 0
        return idx

    def enqueue(self, val):
        if self.check_circular_array_empty():
            self.first_idx = 0
            self.last_idx = 0
        else:
            self.last_idx = self.increment_idx(self.last_idx)
            if self.first_idx == self.last_idx:
                self.first_idx = self.increment_idx(self.first_idx)
        self.data[self.last_idx] = val

    def check_circular_array_empty(self):
        is_empty = True
        while is_empty:
            for elem in self.data:
                if elem != self.init_val:
                    is_empty = False
                    break
            break
        return is_empty

    def dequeue(self):
        is_empty = self.check_circular_array_empty()
        if is_empty:
            print(EMPTY_MESSAGE)
            raise Exception
        val = self.data[self.first_idx]
        self.data[self.first_idx] = self.init_val
        self.first_idx = self.increment_idx(self.first_idx)
        return val


class Heap(Base):
    """Implement min heap"""
    def __init__(self, data=[], use_node=False):
        super(Heap, self).__init__(data)
        if len(self.data) > 0:
            self.construct_heap_node() if use_node else self.construct_heap()
        else:
            self.last_idx = None

    def construct_heap(self, right_idx=None):
        if right_idx is None: 
            self.last_idx = len(self.data) - 1
            right_idx = self.last_idx
        length = right_idx + 1
        for i in range(length // 2 - 1, -1, -1):
            r_idx = 2 * i + 2
            l_idx = 2 * i + 1
            if r_idx > right_idx:
                min_idx = l_idx
            elif self.data[l_idx] >= self.data[r_idx]:
                min_idx = r_idx
            else:
                min_idx = l_idx
            
            if self.data[i] > self.data[min_idx]:
                swap(self.data, i, min_idx)

    def insert(self, val):
        self.data.append(val)
        if self.last_idx is None:
            self.last_idx = 0
        else:
            self.last_idx += 1
        
        i = self.last_idx
        while(i > 0):
            p_idx = (i - 1) // 2
            if self.data[p_idx] > self.data[i]:
                swap(self.data, p_idx, i)
                i = p_idx
            else:
                break
    
    def deletemin(self):
        self.check_empty()
        minval = self.data[0]
        last_val = self.data[self.last_idx]
        self.data[0] = last_val
        self.data.pop()
        if len(self.data) == 0:
            self.last_idx = None
            return minval
        else:
            self.last_idx -= 1
        
        p_idx = 0
        while(self.last_idx / 2 > p_idx):
            left_idx = 2 * p_idx + 1
            right_idx = left_idx + 1 

            if right_idx > self.last_idx:
                if self.data[p_idx] > self.data[left_idx]:
                    swap(self.data, p_idx, left_idx)
                    p_idx = left_idx
                else:
                    break  

            if self.data[p_idx] > self.data[left_idx]:
                if self.data[left_idx] > self.data[right_idx]:
                    swap(self.data, p_idx, right_idx)
                    p_idx = right_idx
                else:
                    swap(self.data, p_idx, left_idx)
                    p_idx = left_idx
            elif self.data[p_idx] > self.data[right_idx]:
                swap(self.data, p_idx, right_idx)
                p_idx = right_idx
            else:
                break
        return minval

    def construct_heap_node(self, right_idx=None):
        if right_idx is None:
            self.last_idx = len(self.data) - 1
            right_idx = self.last_idx
        length = right_idx + 1
        for i in range(length // 2 - 1, -1, -1):
            r_idx = 2 * i + 2
            l_idx = 2 * i + 1
            if r_idx > right_idx:
                min_idx = l_idx
            elif self.data[l_idx] >= self.data[r_idx]:
                min_idx = r_idx
            else:
                min_idx = l_idx
            
            if self.data[i] > self.data[min_idx]:
                swap(self.data, i, min_idx)

    def insert_node(self, node):
        self.data.append(node)
        if self.last_idx is None:
            self.last_idx = 0
        else:
            self.last_idx += 1
        
        i = self.last_idx
        while(i > 0):
            p_idx = (i - 1) // 2
            if self.data[p_idx].val > self.data[i].val:
                swap(self.data, p_idx, i)
                i = p_idx
            else:
                break
    
    def deletemin_node(self):
        self.check_empty()
        min_node = self.data[0]
        last_node = self.data[self.last_idx]
        self.data[0] = last_node
        self.data.pop()
        if len(self.data) == 0:
            self.last_idx = None
            return min_node
        else:
            self.last_idx -= 1
        
        p_idx = 0
        while(self.last_idx / 2 > p_idx):
            left_idx = 2 * p_idx + 1
            right_idx = left_idx + 1

            if right_idx > self.last_idx:
                if self.data[p_idx].val > self.data[left_idx].val:
                    swap(self.data, p_idx, left_idx)
                    p_idx = left_idx
                else:
                    break

            if self.data[p_idx].val > self.data[left_idx].val:
                if self.data[left_idx].val > self.data[right_idx].val:
                    swap(self.data, p_idx, right_idx)
                    p_idx = right_idx
                else:
                    swap(self.data, p_idx, left_idx)
                    p_idx = left_idx
            elif self.data[p_idx].val > self.data[right_idx].val:
                swap(self.data, p_idx, right_idx)
                p_idx = right_idx
            else:
                break

        return min_node


class Node:

    def __init__(self, val, **kwargs):
        self.val = val
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def check_empty(self):
        assert self.val is not None, EMPTY_MESSAGE


class NamedNode(Node):

    def __init__(self, name, val):
        super(NamedNode, self).__init__(val, name=name)


class BST(Node):
    """Implement Binary Search Tree"""
    def __init__(self, val=None, left=None, right=None):
        super(BST, self).__init__(val, left=left, right=right)

    def insert(self, val):
        if self.val is None:
            self.val = val
        elif val < self.val:
            if self.left is None:
                self.left = BST(val, left=None, right=None)
            else:
                self.left.insert(val)
        else:
            if self.right is None:
                self.right = BST(val, left=None, right=None)
            else:
                self.right.insert(val)

    def delete(self, val):
        self.check_empty()
        def print_no_val(val):
            print(f'there is no {val} in this tree')
        
        def deletemin(node):
            if node.left is None:
                minval = node.val
                return minval, node.right
            else:
                minval, node.left = deletemin(node.left)
                return minval, node

        def deletemax(node):
            if node.right is None:
                maxval = node.val
                return maxval, node.left
            else:
                maxval, node.right = deletemax(node.right)
                return maxval, node

        def delete_and_fix_left_tree(parent):
                maxval, node = deletemax(parent.left)
                parent.val = maxval
                parent.left = node

        def delete_and_fix_right_tree(parent):
                minval, node = deletemin(parent.right)
                parent.val = minval
                parent.right = node
            
        if self.left is None and self.right is None:
            if self.val == val:
                self.val = None
            else:
                print_no_val(val)
        elif self.left is None:
            if self.val > val:
                print_no_val(val)
            elif self.val == val:
                delete_and_fix_right_tree(self)
            else:
                self.right.delete(val)
        elif self.right is None:
            if self.val == val:
                delete_and_fix_left_tree(self)
            else:
                self.left.delete(val)
        else:
            # both left and right have a node
            if self.val == val:
                delete_and_fix_right_tree(self)

            elif self.val > val:
                self.left.delete(val)
            else:
                self.right.delete(val)

    def convert_bst_to_dict(self):
        if self.val is None:
            return None
        else:
            def get_bst_dic(dic, idx, node):
                dic[idx] = node.val
                if node.left is not None:
                    get_bst_dic(dic, 2*idx+1, node.left)
                if node.right is not None:
                    get_bst_dic(dic, 2*idx+2, node.right)
            
            dic = {}
            get_bst_dic(dic, 0, self)
            return dic


class LinkedList(Node):

    def __init__(self, val=None, next=None):
        super(LinkedList, self).__init__(val, next=next)

    def insert(self, val):
        new_node = LinkedList(val, next=None)
        new_node.next = self
        self = new_node
        return self

    def delete(self, val):
        self.check_empty()
        if self.val == val:
            self = self.next
            pass
        prev = self
        next = prev.next
        while(True):
            if next is None:
                print(f'there is no {val} in this tree')
                break
            elif next.val == val:
                prev.next = next.next
                break
            else:
                prev = next
                next = next.next

    def collect_all_vals_in_list(self):
        l = []
        l.append(self.val)
        next = self.next
        while(True):
            if next is not None:
                l.append(next.val)
                next = next.next
            else:
                return l


class Hash:
    """Implement Separate Chaining Hash"""
    def __init__(self, num_bucket, hash_func, init_val=None):
        self.buckets = []
        self.hash_func = hash_func
        for _ in range(num_bucket):
            self.buckets.append(init_val)
    
    def insert(self, val):
        hash_val = self.hash_func(val)
        if self.buckets[hash_val] is None:
            self.buckets[hash_val] = LinkedList(val=val, next=None)
        else:
            self.buckets[hash_val] = self.buckets[hash_val].insert(val)

    def delete(self, val):
        self.check_empty()
        hash_val = self.hash_func(val)
        if self.buckets[hash_val] is None:
            print(f'there is no {val} in this tree')
            pass
        else:
            self.buckets[hash_val].delete(val)

    def check_empty(self):
        for elem in self.buckets:
            if elem is not None:
                return
        print(EMPTY_MESSAGE)
        raise Exception

    def convert_hash_to_dict(self):
        dic = {}
        for i, ll in enumerate(self.buckets):
            if ll is not None:
                l = ll.collect_all_vals_in_list()
                dic[i] = l
        return dic