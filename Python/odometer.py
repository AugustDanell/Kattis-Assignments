# Basically taking a sum (O(n)) and then using the distances as a stream algorithm for O(n):
cases = int(input())
distances = list(map(int, input().split()))
mapping = {}
possibleDistances = []
s = sum(distances)

for neglectDist in distances:
    if not mapping.__contains__(neglectDist):
        possibleDistances.append(s - neglectDist)
        mapping[neglectDist] = True

possibleDistances.sort()
print(len(possibleDistances))
print(" ".join(list(map(str, possibleDistances))))
