total,solved = list(map(float,input().split()))
total_avg, est_avg = list(map(float,input().split()))


remaining = total - solved
total_left = total_avg*total - solved*est_avg

est_remainder = total_left/remaining
if(est_remainder > 100.0 or est_remainder < 0.):
    print("impossible")
else:
    print(est_remainder)
