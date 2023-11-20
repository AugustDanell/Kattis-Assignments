if __name__ == "__main__":
    N = int(input())
    peopleHome = {}
    for _ in range(N):
        fullName = input().split()
        if len(fullName) == 1:
            peopleHome[fullName[0]] = [fullName[0]]
        else:
            peopleHome[fullName[0]] = fullName

    Q = int(input())
    for _ in range(Q):
        name = input()
        if name in peopleHome:
            if len(peopleHome[name]) == 1:
                print("Jebb")
            else:
                fullName = peopleHome[name]
                print("Neibb en {0} {1} er heima".format(fullName[0], fullName[1]))
        else:
            print("Neibb")