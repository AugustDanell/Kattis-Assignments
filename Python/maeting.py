# problem description: https://open.kattis.com/problems/maeting

'''
    General Solution:
    Read in the solution and put them in a hashmap that takes in
    how many anttendes there are, sort and print.
'''

if __name__ == "__main__":
    N = int(input())
    peopleMap = {}
    for _ in range(N):
        person = input()
        peopleMap[person] = 0

    M = int(input())
    for _ in range(M):
        course = input().split()
        for i in range(1, len(course)):
            attendee = course[i]
            peopleMap[attendee] += 1

    sortedPeople = list(sorted(peopleMap.keys(), key = lambda x : peopleMap[x], reverse = True))
    for person in sortedPeople:
        print(peopleMap[person], person)
