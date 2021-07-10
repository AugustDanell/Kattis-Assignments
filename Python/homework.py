s = input().split(";")
problems = 0

for i in s:
    if(i.__contains__("-")):
        a,b = i.split("-")
        problems += int(b) - int(a)

    problems += 1



print(problems)
