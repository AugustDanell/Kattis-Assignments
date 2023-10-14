# 779th solution: https://open.kattis.com/problems/spacerace

if __name__ == "__main__":

    # 1. Read in data:
    n = int(input())
    d = float(input())
    bestEffiency = -1
    bestCar = None

    # 2. Loop over every car and compare quantities:
    for _ in range(n):
        car, velocity, fuel = input().split()
        velocity = float(velocity)
        fuel = float(fuel)
        time = d/velocity
        rateOfFuel = fuel / time
        efficiency = velocity / rateOfFuel
        if(bestEffiency == -1 or efficiency > bestEffiency):
            bestCar = car
            bestEffiency = efficiency

    # 3. Print the best car:
    print(bestCar)
