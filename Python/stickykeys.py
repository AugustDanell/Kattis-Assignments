# Solution to the problem: https://open.kattis.com/problems/stickykeys

text = list(input())
index = 0
while index < len(text)-1:
    current = text[index]
    next = text[index+1]
    if current == next:
        text.pop(index)
    else:
        index += 1

print("".join(text))
