P,D = list(map(int,input().split()))
districts = []
for i in range(D):
    districts.append([0,0])

for i in range(P):
    D,A,B = list(map(int,input().split()))
    (districts[D-1])[0] += A
    (districts[D-1])[1] += B

totalVotes = 0
wastedVotes = [0, 0]
for district in districts:
    A,B = district
    majorityVotes = (A+B)//2 + 1
    totalVotes += A + B

    if A >= majorityVotes:
        print("A {0} {1}".format(A - majorityVotes, B))
        wastedVotes[0] += A - majorityVotes
        wastedVotes[1] += B
    else:
        print("B {0} {1}".format(A, B-majorityVotes))
        wastedVotes[0] += A
        wastedVotes[1] += B-majorityVotes

print(abs(wastedVotes[0] - wastedVotes[1])/totalVotes)
