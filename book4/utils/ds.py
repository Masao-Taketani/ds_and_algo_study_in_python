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
    def __init__(self, data=[]):
        super(Heap, self).__init__(data)
        self.last_idx = None

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
        else:
            self.last_idx -= 1
        
        p_idx = 0
        while(self.last_idx / 2 > p_idx):
            left_idx = 2 * p_idx + 1
            right_idx = left_idx + 1 
            if self.data[p_idx] > self.data[left_idx]:
                if self.data[left_idx] > self.data[right_idx]:
                    swap(self.data, p_idx, right_idx)
                    p_idx = right_idx
                else:
                    swap(self.data, p_idx, left_idx)
                    p_idx = right_idx
            elif self.data[p_idx] > self.data[right_idx]:
                swap(self.data, p_idx, right_idx)
                p_idx = right_idx
            else:
                break
        return minval


class Node:

    def __init__(self, val, **kwargs):
        self.val = val
        for k, v in kwargs.items():
            self.__dict__[k] = v

    def check_empty(self):
        assert self.val is not None, EMPTY_MESSAGE


class BST(Node):
    """Implement Binary Search Tree"""
    def __init__(self, val=None, **kwargs):
        super(BST, self).__init__(val, **kwargs)

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

        def delete_and_fix_tree(parent):
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
                delete_and_fix_tree(self)
            else:
                self.right.delete(val)
        elif self.right is None:
            if self.val <= val:
                print_no_val(val)
            else:
                self.left.delete(val)
        else:
            # both left and right have a node

            if self.val == val:
                delete_and_fix_tree(self)

            elif self.val > val:
                self.left.delete(val)
            else:
                self.right.delete(val)


def swap(lis, idx1, idx2):
    tmp = lis[idx1]
    lis[idx1] = lis[idx2]
    lis[idx2] = tmp