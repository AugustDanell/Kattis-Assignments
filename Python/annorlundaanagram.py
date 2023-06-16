# 728th Kattis, solution to the problem: https://open.kattis.com/problems/annorlundaanagram

''' General Solution: Handling three different cases

    1. If a word is written containing only one letter we can write it off as impossible.
    2. If no letter occurs more than N//2 times we can construct a trivial solution (any sorted solution works)
    3. If a letter occurs more than N//2 times but less than N times we can first construct a substring of length N//2
    consisting of only this letter. We can then put the other letters in the middle. Finally we append the remainder 
    (constituteted of this specific letter). This will always work. The key to understanding this is to understand that
    if a letter occurs more than N//2 times no other letter can do the same so they can safely be squished in the middle,
    no problem.
    
'''

# 1. Read in the data:
word = list(input())
N = len(word)
largest_occurance = 0
most_frequent_letter = ""
unique_occurances = 0
letter_map = {}

# 2. Map every letter to a number of occurances:
for letter in word:
    if letter in letter_map:
        letter_map[letter] += 1
    else:
        letter_map[letter] = 1
        unique_occurances += 1

    if largest_occurance < letter_map[letter]:
        most_frequent_letter = letter
        largest_occurance = letter_map[letter]

# 3. Case handling:
if largest_occurance == N:
    print(-1)
elif largest_occurance <= N//2:
    print("".join(sorted(word)))
elif largest_occurance > N//2:
    match_str = ""
    for i in range(N//2):
        match_str += most_frequent_letter
    letter_map[most_frequent_letter] -= N//2

    for key in letter_map:
        if key == most_frequent_letter:
            continue
        repetitions = letter_map[key]
        for i in range(repetitions):
            match_str += key

    remainder = letter_map[most_frequent_letter]
    for i in range(remainder):
        match_str += most_frequent_letter
    print(match_str)
