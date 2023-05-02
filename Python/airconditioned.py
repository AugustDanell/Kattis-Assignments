# A solution to the problem: https://open.kattis.com/problems/airconditioned
'''
    Greedy Algorithm Approach:
    1. Sort the minions by (min,max), with emphasis on max, ascendingly.
    2. Take the lowest max greedily and fill.
    3. For every time every new minion comes see if it squeezed in, if not, take a new max.
'''

if __name__ == "__main__":
    n = int(input())
    minions = []
    for i in range(n):
        a,b = list(map(int,input().split()))
        minions.append([a,b])

    f = lambda x: x[0] + x[1]*1000
    minions = sorted(minions, key = f)

    count = 0
    end = -1

    for minion in minions:
        if minion[0] > end:
            end = minion[1]
            count+= 1
    print(count)
