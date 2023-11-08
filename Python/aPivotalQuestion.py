# Problem Description: https://open.kattis.com/problems/apivotalquestion

'''
      General Solution:
      The problem is to find every possible pivot number in a list.
      1. Find candidates in going from left to right.
      2. Eliminate candidates by going right to left.
      3. Print them in the correct order. 
'''

if __name__ == "__main__":
    # 1. Basic input:
    data = list(map(int,input().split()))
    size = data[0]
    numbers = data[1:]
    largestOcc = 0
    pivotCands = {}

    # 2. Find candidates for being pivots from left to right:
    for i in range(size):
        element = numbers[i]
        if element > largestOcc:
            largestOcc = element
            pivotCands[element] = True

    # 3. Find eliminate candidates from right to left:
    truePivots = {}
    smallestOcc = float('inf')
    for i in range(size-1, -1, -1):
        element = numbers[i]
        if element < smallestOcc:
            smallestOcc = element
            if element in pivotCands:
                truePivots[element] = True
                smallestOcc = element

    # 4. If the list is composed of m > 100, print the 100 first values. Else print all:
    elements = list(map(str, truePivots.keys()))[::-1]
    if len(elements) <= 100:
        print(len(truePivots), " ".join(elements))
    else:
        trimmedElements = []
        for i in range(100):
            trimmedElements.append(elements[i])
        print(len(truePivots), " ".join(trimmedElements))
