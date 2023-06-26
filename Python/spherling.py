# 731th Kattis, Solution to the problem: https://open.kattis.com/problems/spehrling

# 1. Read in the data:
wanted_word = list(input())
written_word = list(input())

# 2. Start with potentially popping extra characters and calculate a disparity:
start_trims = 0
while len(written_word) > len(wanted_word):
    start_trims += 1
    written_word.pop()
disparity = max(start_trims, len(wanted_word) - len(written_word))

# 3. Now when the strings are equal in length, pop until starting substring is the same:
backsteps = 0
while len(written_word) > 0:
    if wanted_word[:len(written_word)] == written_word:
        break
    else:
        backsteps += 1
        written_word.pop()

# 4. Output the answer:
print(disparity + backsteps*2)
