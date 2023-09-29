n = int(input())
staircases = list(map(int,input().split()))
cost = 0
for index in range(n-1):
    currentStep = staircases[index]
    nextStep = staircases[index+1]
    if(currentStep - nextStep > 1):
        cost += (currentStep - nextStep) - 1

print(cost + staircases[-1] - 1)