# Problem: https://open.kattis.com/problems/janeeyre

if __name__ == "__main__":
    # 0. Initiate data:
    n,m,k = list(map(int, input().split()))
    constantStr = "Jane Eyre"

    # 1. Initiate the STARTING stack of books to read:
    toRead = 0
    for _ in range(n):
        data = input().split()
        name = " ".join(data[0:-1])[1:-1]
        length = int(data[-1])
        if(name < constantStr):
            toRead += length

    # 2. Read in books from FRIENDS that come before Jane Eyre in order of occurance:
    beforeJane = []
    for _ in range(m):
        data = input().split()
        inTime = int(data[0])
        name = " ".join(data[1:-1])[1:-1]
        length = int(data[-1])
        if(name < constantStr):
            beforeJane.append([inTime, length])

    # 3. Sort books that came before jane:
    sortedBeforeJane = sorted(beforeJane, key = lambda x: x[0], reverse=True)

    # 4. Add books that we are reading to the accumulating counter:
    while(len(sortedBeforeJane) > 0):
        nextBook = sortedBeforeJane.pop()
        if(nextBook[0] > toRead):
            break
        else:
            toRead += nextBook[1]

    # 5. Print the counter + time to read "Jane Eyre":
    print(toRead + k)

    '''
    Testcase:
    
    2 2 592
    "Pride and Prejuce" 432
    "Don Qi" 863
    863 "Great Go Go Go Gooo" 218
    1081 "Crime and Punishment" 527
    '''
