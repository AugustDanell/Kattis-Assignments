sentence = input()
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
count = 0

for i in sentence:
    if(i in vowels):
        count += 1

print(count)
