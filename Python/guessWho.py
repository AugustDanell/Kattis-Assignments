# Problem Description: https://open.kattis.com/problems/guesswho

if __name__ == "__main__":
    # 1. Read in data and add to a list:
    N, M, Q = list(map(int,input().split()))
    people = []
    for _ in range(N):
        people.append(list(input()))
    
    # 2. Create a mapping, index -> value from the queries.
    indexToVal = {}
    for _ in range(Q):
        index, val = input().split()
        index = int(index)-1
        indexToVal[index] = val
    
    # 3. Test which people pass.
    foundIndex = -1
    foundPpl = 0
    for i in range(len(people)):
        person = people[i]
        match = True
        for index in indexToVal:
            if not indexToVal[index] == person[index]:
                match = False
        if match:
            foundIndex = i + 1
            foundPpl += 1
    
    # 4. Print the result
    if foundPpl == 1:
        print("unique")
        print(foundIndex)
    else:
        print("ambiguous")
        print(foundPpl)
