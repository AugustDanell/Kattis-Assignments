testcases = int(input())

c1,p1,c2,p2 = 0,0,0,0

# Reading in data:
for t in range(testcases):
    c1 = int(input())
    p1 = list(map(int,input().split()))
    c2 = int(input())
    p2 = list(map(int, input().split()))

    pol_res = []
    for i in range(len(p1)):
        for j in range(len(p2)):
            factor = p1[i]*p2[j]
            index = i+j             # Rule of exponentials

            if(len(pol_res) == index):
                pol_res.append(factor)
            else:
                pol_res[index] += factor

    print(len(pol_res) -1)
    print(pol_res.__str__()[1:-1].replace(",",""))
