inp = input()
split = inp.split()

N = int(split[0])
Q = int(split[1])

initialLocationCompanies = input()
companyList = []
split = initialLocationCompanies.split()

for i in range(N):
    companyList.append(int(split[i]))

for i in range(Q):
    inquiry = input()
    inSplit = inquiry.split()

    if(inSplit[0] == "1"):
        c = int (inSplit[1])
        l = int (inSplit[2])

        companyList[c-1] = l

    else:
        d1 = companyList[int(inSplit[1])-1]
        d2 = companyList[int(inSplit[2])-1]

        print(abs(d1-d2))