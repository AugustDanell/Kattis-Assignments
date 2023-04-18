# A solution to the problem: https://open.kattis.com/problems/flipflow

if __name__ == "__main__":
    t,s,n = list(map(int,input().split()))
    upper_half = s
    lower_half = 0
    flipped = False
    flip_list = list(map(int,input().split()))
    index = 0

    for i in range(t):
       # print(i, upper_half, lower_half)
        if not (index > len(flip_list)-1) and i == flip_list[index]:
            index += 1
            flipped = not flipped

        # Drip sand:
        if flipped and upper_half > 0:
            upper_half -= 1
            lower_half += 1
        elif not flipped and lower_half > 0:
            upper_half += 1
            lower_half -= 1

    #print(upper_half)
    if len(flip_list) % 2 == 1:
        print(upper_half)
    else:
        print(lower_half)
