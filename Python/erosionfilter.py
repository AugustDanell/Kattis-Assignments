n = int(input())
numbers = list(map(int,input().split()))
transformedList = []
breakpoint = 1e15
for i in range(len(numbers)):
    number = numbers[i]
    
    # Backward Checking:
    for j in range(i-1, 0-1, -1):
        weight = 2**(i-j)
        number += numbers[j]/weight
        if weight > breakpoint:
            break
    
    # Forward Checking:
    for j in range(i+1, n):
        weight = 2**(j-i)
        number += numbers[j]/weight
        if weight > breakpoint:
            break
    
    transformedList.append(str(number))
    
print(" ".join(transformedList))