from utils.test import *
from utils.ds import Stack, Queue
from utils import print_ex, print_passing_all

def execute_stack(stack, test_data):
    for elem in test_data:
        if elem == 'pop':
            stack.pop()
        else:
            stack.push(elem)
        print(stack.data)

def execute_stack(stack, test_data):
    for elem in test_data:
        stack.pop() if elem == 'pop' else stack.push(elem)
        print(stack.data)

def execute_queue(queue, test_data):
    for elem in test_data:
        queue.dequeue() if elem == 'deq' else queue.enqueue(elem)
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

    print_ex()
    A = [12, 23, 'pop', 34, 25, 'pop']
    A_ans = [12, 34]
    A_stack = Stack([])
    execute_stack_test(execute_stack, A_ans, A_stack, A)
    B = [12, 23, 'deq', 34, 25, 'deq']
    B_ans = [34, 25]
    B_queue = Queue([])
    execute_queue_test(execute_queue, B_ans, B_queue, B)

    print_passing_all()