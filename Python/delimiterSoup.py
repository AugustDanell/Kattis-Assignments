from collections import deque
stack = deque()
length = int(input())
inp = input()
error = False
inp = list(inp)

for i in range(length):
    if(inp[i] == '(' or inp[i] == '{' or inp[i] == '['):
        stack.append(inp[i])

    elif (inp[i] == ')' or inp[i] == '}' or inp[i] == ']'):
        if(len(stack) == 0):
            error = True
            print("%s %d" % (inp[i], i))
            break

        x = stack.pop()
        if(not(ord(x) == (ord(inp[i]) - 1)) and not(ord(x) == (ord(inp[i])-2))):
            error = True
            print("%s %d"%(inp[i], i))

    if(error):
        break

if(not error):
    print("ok so far")
