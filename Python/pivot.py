def is_pivot2(i,x):
    if(i+1 == x):
        return True
    return False

''' is_pivot 
    A pivot element should be such that all elements to the left are less and all elements to te right greater.
    1. We look if the previous element is consequitive, meaning that whatever it was it still is.
    2. We look if the current element is lesser than the highest so far, if so, the current is NOT pivot.
    3. We look that all elements from the current to the end are greater than the current, if not, current is not pivot.
'''
def is_pivot(x,l,prev_elem, prev_pivot):
    global highest_so_far
    start_elem = l[x]
    if(start_elem > highest_so_far):
        highest_so_far = start_elem

    if(start_elem-prev_elem == 1):
        return prev_pivot

    elif start_elem < highest_so_far:
        return False

    else:
        for i in range(x,len(l)):
            if(start_elem > l[i]):
                return False

    return True

elements = int(input())
l = list(map(int,input().split()))
s = 0
prev_pivot = True
prev_elem = 0
highest_so_far = 0

for i in range(len(l)):
    if(is_pivot(i, l, prev_elem, prev_pivot)):
        s += 1
        prev_pivot = True
    else:
        prev_pivot = False
    prev_elem = l[i]

print(s)
