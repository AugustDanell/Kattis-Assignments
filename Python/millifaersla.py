def getLowestInput(numbers):
    for i in range(len(numbers)):
        if numbers[i] == min(numbers):
            return i

numbers = []
for i in range(3):
    numbers.append(int(input()))
print(["Monnei", "Fjee", "Dolladollabilljoll"][getLowestInput(numbers)])