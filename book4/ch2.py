from utils.test import *
from utils.ds import Stack, Queue

def execute_stack(stack, test_data):
    for elem in test_data:
        if elem == 'pop':
            stack.pop()
        else:
            stack.push(elem)
        print(stack.data)

def execute_stack(stack, test_data):
    for elem in test_data:
        if elem == 'pop':
            stack.pop()
        else:
            stack.push(elem)
        print(stack.data)

def execute_queue(queue, test_data):
    for elem in test_data:
        if elem == 'deq':
            queue.dequeue()
        else:
            queue.enqueue(elem)
        print(queue.data)

if __name__ == '__main__':
    stack_test_data = ['dog', 'cat', 'pig', 'pop', 'pop', 'rat']
    stack_ans = ['dog', 'rat']
    stack = Stack()
    execute_stack_test(execute_stack, stack_ans, stack, stack_test_data)
    queue_test_data = ['dog', 'cat', 'pig', 'deq', 'deq', 'rat']
    queue_ans = ['pig', 'rat']
    queue = Queue()
    execute_queue_test(execute_queue, queue_ans, queue, queue_test_data)