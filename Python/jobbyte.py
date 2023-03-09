# Kattis Assignment: https://open.kattis.com/problems/jobbyte

# Swaps like a selection sort but with a dictionary for faster avg lookup:
def selectionSortSwap(l = []):
    swaps = 0
    helpMap = {}
    index = 0
    while index < len(l):
        if helpMap.__contains__(index + 1) and helpMap.__contains__(l[helpMap[index + 1]]):
            #print(helpMap, l, index)
            swapIndex = helpMap[index + 1]
            if swapIndex == index:
                index += 1
                continue

            l[index], l[swapIndex] = l[swapIndex], l[index]
            helpMap[index + 1], helpMap[l[swapIndex]] = helpMap[l[swapIndex]], helpMap[index + 1]
            swaps += 1

        elif not l[index] == index + 1:
            for i in range(index+1, len(l)):
                if l[i] == index + 1:
                    # Update cache
                    helpMap[l[i]] = index
                    helpMap[l[index]] = i


                    l[i], l[index] = l[index], l[i]

                    swaps += 1
                    break
                else:
                    helpMap[l[i]] = i

        index += 1
    return swaps

n = int(input())
print(selectionSortSwap(list(map(int,input().split()))))
