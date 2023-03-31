# https://open.kattis.com/problems/marko


number_map = {2:list("abc"),
              3:list("def"),
              4:list("ghi"),
              5:list("jkl"),
              6:list("mno"),
              7:list("pqrs"),
              8:list("tuv"),
              9:list("wxyz")
              }

# 1. Read in words and the number string:
n = int(input())
words = []
for i in range(n):
    words.append(list(input()))
number_string = list(input())

# 2. Just iterate over every word and see if their letters can be found in the map. Count it then:
count = 0
for i in range(len(number_string)):
    while len(words)> 0:
        word = words.pop(0)
        if not len(word) == len(number_string):
            continue
        else:
            match = True
            for j in range(len(word)):
                if not word[j] in number_map[int(number_string[j])]:
                    match = False
                    break
            if match:
                count += 1
                
# 3. Just print the count:
print(count)
