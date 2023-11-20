def canMerge(l):
    for i in range(len(l)-1):
        if l[i] == l[i+1]:
            return True
    return False

def contMerge(l):
    while(canMerge(l)):
        index = 0
        while(index < len(l)-1):
            if l[index] == l[index+1]:
                l.pop(index+1)
                l[index] *= 2
            else:
                index += 1
    return l

def scanAndRemove(l, removeNumber):
    index = 0
    while index < len(l):
        if l[index] == removeNumber:
            l.pop(index)
        else:
            index += 1

    return l, removeNumber*2

if __name__ == "__main__":
    N = int(input())
    numbers = list(map(int, input().split()))

    removeNumber = 1
    while len(numbers) > 1:
        numbers = contMerge(numbers)
        numbers, removeNumber = scanAndRemove(numbers, removeNumber)
        #print(numbers, removeNumber)

    print(numbers[0])