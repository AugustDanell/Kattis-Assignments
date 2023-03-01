def hasSquareDivisor(n):
    for i in range(2, n):
        if i**2 > n:
            return False
        if n % i**2 == 0:
            return True
    return False

n = int(input())
m = 2
largest = 2

while m < n:
    k = n*m
    if not hasSquareDivisor(k):
        largest = m
        break

    m += 1

print(largest)
