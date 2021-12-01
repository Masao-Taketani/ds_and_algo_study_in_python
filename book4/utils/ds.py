EMPTY_MESSAGE = 'Cannot be popped since there is no data.'

class Base:
    def __init__(self, data=[]):
        self.data = data

    def __len__(self):
        return len(self.data)

    def check_empty(self):
        assert len(self) != 0, EMPTY_MESSAGE


class Stack(Base):
    def push(self, val):
        self.data.append(val)
    
    def pop(self):
        self.check_empty()
        val = self.data.pop()
        return val


class Queue(Base):
    def __init__(self, data=[], max_elem=8, init_val=float('inf')):
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