testcases = int(input())
for i in range(testcases):
    number1 = int(input().replace(" ", ""))
    number2 = int(input().replace(" ", ""))
    l = str(number1 + number2)

    # ugly sol
    s = ""
    for e in l:
        s += e + " "

    print(s[:-1])
