intervals_left = int(input())
d = 0
t = 0
biggest_sum = 0

while intervals_left > 0:
    intervals_left -= 1
    a,b = input().split(" ")
    if(a == b == "0"):
        continue

    A,B = int(a),int(b)
    #print(A,B,d,t)
    sum = int((B-t)/(A-d))
    d,t = A,B

    if sum > biggest_sum:
        biggest_sum = sum

print(biggest_sum)
