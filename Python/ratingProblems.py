inp = input()
split = inp.split(" ")

N = int(split[0])
K = int(split[1])
sum = 0.0

for i in range(K):
    sum += int(input())

max = sum + (N-K)*3.
min = sum - (N-K)*3.

print((min/N).__str__() + " " + (max/N).__str__())