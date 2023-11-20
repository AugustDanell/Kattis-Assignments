

def getPalindromeDist(name):
    counter = 0
    for i in range(len(name)//2):
        backwardIndex = len(name) -1 -i
        if name[i] == "_" or name[backwardIndex] == "_":
            continue
        if not (name[i] == name[backwardIndex]):
            counter += 1

    return counter

if __name__ == "__main__":
    name = input()
    bestAns = float('inf')
    shifts = 0
    while shifts < bestAns:
        augmentedName = name + "_"*shifts
        localAns = getPalindromeDist(augmentedName) + shifts
        if localAns < bestAns:
            bestAns = localAns
        shifts += 1

    print(bestAns)