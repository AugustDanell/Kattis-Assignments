def factor(triplet):
    acc = 1
    for element in triplet:
        acc*=element
    return acc

def increment(triplet):
    for i in range(len(triplet)):
        triplet[i] += 1

if __name__ == "__main__":
    N = int(input())
    triplet = [1,2,3]
    counter = 0
    while factor(triplet) < N:
        counter += 1
        increment(triplet)

    print(counter)