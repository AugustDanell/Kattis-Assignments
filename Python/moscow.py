s = input()
split = s.split()

easy = int(split[0])
med = int(split[1])
hard = int(split[2])

problems = int(split[3])
canDo = True

if(problems < 3):
    canDo = False

if(easy == 0):
    canDo = False
else:
    problems = problems - easy

if(med == 0):
    canDo = False
else:
    problems = problems - med

if(hard == 0):
    canDo = False
else:
    problems = problems - hard

if(problems > 0):
    canDo = False

if(canDo):
    print("YES")
else:
    print("NO")