# 725th Kattis. A Solution to the problem: https://open.kattis.com/problems/lektira

''' General Solution: Braindead, Brute Force.
    Just try every string and see which one is the best (lexiographically).
'''


word = list(input())
best_str = None
for i in range(1, len(word)-1):
    for j in range(i+1, len(word)):
        first_str = word[0:i]
        second_str = word[i:j]
        third_str = word[j::]
        concat_str = "".join(first_str[::-1]) + "".join(second_str[::-1]) + "".join(third_str[::-1])
        if best_str == None or concat_str < best_str:
            best_str = concat_str
print(best_str)
