# Problem ID: teacherevaluation
def avg(n,s):
    return s/n

data = input().split()
students = int(data[0])
p = int(data[1])
forge = 100

sum = 0
points = input().split()
for i in range(students):
    sum += int(points[i])


impossible = False
forges = 0

if(p == 100 and avg(students, sum) < p):
    impossible = True
else:
    while(avg(students, sum) < p):
        students += 1
        sum += forge
        forges += 1

if(not impossible):
    print(forges)
else:
    print("impossible")