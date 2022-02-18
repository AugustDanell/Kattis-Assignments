s = input()
left = 0
hasPassedCentre = False
right = 0
for i in s:
    if i == '|':
        if(not hasPassedCentre):
            left += 1
        else:
            right += 1
    elif i == '(':
        hasPassedCentre = True

if(left == right):
    print('correct')
else:
    print('fix')
