# 715th Kattis, A Solution To The Problem: https://open.kattis.com/problems/integerlists

''' General Solution: Deques
    This problem is a timeout kind of problem where we have to write more efficiently that of our code.
    We can use deques instead of lists, deques have a popleft() and pop() function, where we can pop out
    an item at both ends of the deque without having to care about re-factoring it. Using a deque the 
    problem becomes rather straight forward. We switch a reverse flag if we get a reverse operation.
    If we get a DROP operation we drop either at the front (popleft) or at the end (pop), depending
    on the reverse flag. If we get a drop operation when we have no items, we set the error flag to true,
    and break the loop so as to save time. 
'''

from collections import deque
testcases = int(input())
for _ in range(testcases):
    operations = list(input())
    n = int(input())
    operands = input().split(",")
    operands[0] = operands[0][1:]
    operands[-1] = operands[-1][:-1]

    reverse = False
    error = False

    if n == 0:
        operands = []
    else:
        operands = deque(map(int, operands))
        
    for op in operations:
        if op == "R":
            reverse = not reverse
        else:
            if len(operands) == 0:
                print("error")
                error = True
                break
            elif not reverse:
                operands.popleft()
            else:
                operands.pop()

    if not error:
        if reverse:
            operands.reverse()
        l = []
        for operand in operands:
            l.append(str(operand))

        print("[{0}]".format(",".join(l)))
