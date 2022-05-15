prize, cost, prob = list(map(float, input().split()))
if(prize*prob >= cost):
    print("spela inte!")
else:
    print("spela")
