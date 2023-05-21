# A solution to the problem: https://open.kattis.com/problems/guessthedatastructure

''' General Solution:
    We simulate a queue, a stack and a priority queue and check for consistency.
'''
from collections import deque
import sys

for line in sys.stdin:
    operations = int(line)
    queue = deque([])
    stack = []
    priority_queue = []
    is_queue, is_stack, is_prio = True, True, True

    for _ in range(operations):
        op, data = list(map(int,input().split()))
        if op == 1:
            if is_queue:
                queue.append(data)
            if is_stack:
                stack.append(data)
            if is_prio:
                priority_queue.append(data)
                priority_queue.sort()
        elif op == 2:
            if len(queue) == 0:
                is_prio, is_stack, is_queue = False, False,False
            else:
                if is_queue and not queue.popleft() == data:
                    is_queue = False

                if is_stack and not stack.pop() == data:
                    is_stack = False

                if is_prio and not priority_queue.pop() == data:
                    is_prio = False

    if(int(is_prio) + int(is_stack) + int(is_queue) > 1):
        print("not sure")
    elif is_prio:
        print("priority queue")
    elif is_queue:
        print("queue")
    elif is_stack:
        print("stack")
    else:
        print("impossible")
