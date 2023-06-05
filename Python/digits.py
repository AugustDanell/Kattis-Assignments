# 707th Kattis, A Solution to the problem: https://open.kattis.com/problems/digits
'''
    General Solution: Basic recursive function
    1. Read in the data.
    
    2. Feed the data into a recursive function with a specific case for "1".
    The specific case is because if X0 = 1, X1 = 1, we should stop the recursion.
    This does not need to be treated for other numbers.
    
    3. The Recursive Function:
    Well within the recursion we just recursively call until a base case is met.
    We pass in an accumulator and we return the accumulator when the line == prev.
    For each recursion we pass line as len(line).
''' 

def rec(line, prev, acc = 0):
    next = len(line)
    if prev == next:
        return acc+1
    else:
        acc += 1
        next_line = str(next)
        prev = next
        return rec(next_line, prev, acc)


while True:
    line = input()
    if line == "END":
        break
    else:
        if line == "1":
            print(rec(line, int(line)))
        else:
            print(rec(line, -1))
