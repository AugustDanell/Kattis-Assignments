knots = int(input())
all_knots = list(map(int,input().split()))
done_knots = list(map(int,input().split()))

all_knots.sort()
done_knots.sort()
for i in range(knots):
    if(i+1 == knots):
        print(all_knots[knots-1])
        break

    if(not all_knots[i] == done_knots[i]):
        print(all_knots[i])
        break
