# Assignment: https://open.kattis.com/problems/refrigerator

import math

# Input: 
Pa, Ka, Pb, Kb, n = list(map(int,input().split()))

# We assume that we just drive the first car:
aTrips = math.ceil(n/Ka)
bTrips = 0
currentCapacity = aTrips * Ka
currentPrice = Pa * aTrips + Pb * bTrips
bestPrice = currentPrice
bestDivision = [aTrips, bTrips]

# Now we balance over to the other car meaning we increment its trips with one until aTrip is empty:
while aTrips > 0:
    currentCapacity += (Kb)
    bTrips += 1
    
    # For every added bTrip we try to subtract the maximum amount of aTrips:
    while currentCapacity - Ka >= n:
        aTrips -= 1
        currentCapacity -= Ka
    
    # Update the globally lowest price if appropriate:
    currentPrice = Pa * aTrips + Pb*bTrips
    if(currentPrice < bestPrice):
        bestDivision = [aTrips, bTrips]
        bestPrice = currentPrice

# Print the best organization of the two cars and its associated price as output:
print(bestDivision[0], bestDivision[1], bestPrice)
