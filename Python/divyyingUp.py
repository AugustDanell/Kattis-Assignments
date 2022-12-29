# I wanted to write a solution in the smallest amount of rows possible.
if(type(input()) == str and sum(list(map(int,input().split())))%3 == 0):
    print("yes")
else:
    print("no")
