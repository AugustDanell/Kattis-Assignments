def increment_one(l):
    l[0] += 1
    for i in range(0, len(l)-1):
        if(l[i] == 20):
            l[i+1] += 1
            l[i] = 0
        else:
            break

def print_names(N, consonants):
    l = []
    for _ in range(10):
        l.append(0)

    for i in range(N):
        l2 = [consonants[l[0]], consonants[l[1]], "a", consonants[l[2]], consonants[l[3]], "a", consonants[l[4]], consonants[l[5]]]
        print("".join(l2))
        increment_one(l)
        #print(l)

names = int(input())
vowels = ["a", "e", "i", "o", "u"]
consonants = []
for i in range(97,122+1):
    if chr(i) not in vowels:
        consonants.append(chr(i))

print_names(names, consonants)
