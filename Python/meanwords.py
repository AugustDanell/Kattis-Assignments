# A solution to the problem: https://open.kattis.com/problems/meanwords

# Basic functionality for converting a character to its ascii value and back:
def num_to_chr(n):
    return chr(97+n)
def chr_to_num(c):
    return ord(c)-97

assert num_to_chr(0) == "a"
assert num_to_chr(25) == "z"
assert chr_to_num(num_to_chr(0)) == 0

# 1. Input:
n = int(input())
word_list = []
longest_word = 0
for _ in range(n):
  
    # 2. When reading in the words, save the length of the longest:
    word = input()
    length = len(word)
    word_list.append(word)
    if length > longest_word:
        longest_word = length

# 3. Initiate an empty list and iterate over the indices of every word, provided that it is within bounds:
new_word = []
for index in range(longest_word):
    s = 0
    s_words = 0
    
    # 4. If it is within bounds, add the average to the list
    for word in word_list:
        if index < len(word):
            s += chr_to_num(word[index])
            s_words += 1
    
    # 5. Round down the average with the built in division // and append the answer
    s //= s_words
    new_word.append(str(num_to_chr(s)))

# 6. Just output the answer.    
print("".join(new_word))
