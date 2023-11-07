# Problem Description: https://open.kattis.com/problems/dontbefake

''' General Solution:
    This is a dumb & trivial solution to a trivial problem.
    I am just brute forcing.
    1. I iterate over every iterval and add a friend.
    2. Then I calculate a max by iterating over every value and finding it.
    3. Then I calculate how many max points there are and print
'''

if __name__ == "__main__":
    N = int(input())
    secondToFriends = {}

    # Step 1
    for friend in range(N):
        data = input().split()
        for i in range(int(data[0])):
            L = int(data[2*i+1])
            R = int(data[2*i+2])
            for second in range(L, R+1):
                if second not in secondToFriends:
                    secondToFriends[second] = {friend:True}
                else:
                    secondToFriends[second][friend] = True

    # Step 2
    maxFriends = 0
    for second in secondToFriends:
        if len(secondToFriends[second]) > maxFriends:
            maxFriends = len(secondToFriends[second])

    # Step 3
    counter = 0
    for second in secondToFriends:
        if len(secondToFriends[second]) == maxFriends:
            counter += 1

    print(maxFriends)
    print(counter)
