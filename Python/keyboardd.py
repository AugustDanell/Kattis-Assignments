# Solution to this problem: https://open.kattis.com/problems/keyboardd

# Input and init of the hashmaps we use as counters:
text = list(input())
stickyText = list(input())
textOccurance = {}
stickyOccurance = {}

for i in range(len(stickyText)):
    # 1. Count the occurance of the sticky character:
    if not stickyOccurance.__contains__(stickyText[i]):
        stickyOccurance[stickyText[i]] = 1
    else:
        stickyOccurance[stickyText[i]] += 1

    # 2. If possible, count the occurance of the non-sticky character (if not out of bounds):
    if i < len(text):
        if not textOccurance.__contains__(text[i]):
            textOccurance[text[i]] = 1
        else:
            textOccurance[text[i]] += 1

# 3. They should have the same keys, append characters that do not have the same values:
stickyKeys = []
for key in textOccurance.keys():
    if not textOccurance[key] == stickyOccurance[key]:
        stickyKeys.append(key)

# 4. Print with the join function:
print("".join(stickyKeys))
