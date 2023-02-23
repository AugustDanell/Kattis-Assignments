def twitterize(l):
    oneForward = len(l)-1
    twoForward = len(l)-2
    threeForward = len(l)-3
    i = 0

    while i < len(l):
        isUpperCase = l[i] in ["B", "C", "I", "O", "R", "U", "Y"]
        upperCase = ["B", "C", "I", "O", "R", "U", "Y"]
        lowerCase = ["b", "c", "i", "o", "r", "u", "y"]

        # Rule 1:
        if i < oneForward and l[i] in ["a", "A"] and l[i+1] in ["t", "T"]:
            l[i] = "@"
            l.pop(i+1)

        # Rule 2:
        elif i < twoForward and l[i] in ["a", "A"] and l[i+1] in ["n", "N"] and l[i+2] in ["d", "D"]:
            l[i] = "&"
            l.pop(i+1)
            l.pop(i+1)

        # Rule 3:
        elif i < twoForward and l[i] in ["o", "O"] and l[i+1] in ["n", "N"] and l[i+2] in ["e", "E"]:
            l[i] = "1"
            l.pop(i+1)
            l.pop(i+1)
        elif i < twoForward and l[i] in ["w", "W"] and l[i+1] in ["o", "O"] and l[i+2] in ["n", "N"]:
            l[i] = "1"
            l.pop(i+1)
            l.pop(i+1)

        # Rule 4:
        elif i < twoForward and l[i] in ["t", "T"] and l[i+1] in ["w", "W"] and l[i+2] in ["o", "O"]:
            l[i] = "2"
            l.pop(i+1)
            l.pop(i+1)
        elif i < twoForward and l[i] in ["t", "T"] and l[i+1] in ["o", "O"] and l[i+2] in ["o", "O"]:
            l[i] = "2"
            l.pop(i+1)
            l.pop(i+1)
        elif i < oneForward and l[i] in ["t", "T"] and l[i+1] in ["o", "O"]:
            l[i] = "2"
            l.pop(i+1)

        # Rule 5:
        elif i < threeForward and l[i] in ["f", "F"] and l[i+1] in ["o", "O"] and l[i+2] in ["u", "U"] and l[i+3] in ["r", "R"]:
            l[i] = "4"
            l.pop(i + 1)
            l.pop(i + 1)
            l.pop(i + 1)

        elif i < twoForward and l[i] in ["f", "F"] and l[i+1] in ["o", "O"] and l[i+2] in ["r", "R"]:
            l[i] = "4"
            l.pop(i + 1)
            l.pop(i + 1)

        # Rule 6:
        elif i < twoForward and l[i] in ["b", "B"] and l[i+1] in ["e", "E"] and l[i+2] in ["e", "E"]:
            l[i] = "b"
            l.pop(i + 1)
            l.pop(i + 1)

        elif i < twoForward and l[i] in ["b", "B"] and l[i+1] in ["e", "E"] and l[i+2] in ["a", "A"]:
            l[i] = "b"
            l.pop(i + 1)
            l.pop(i + 1)

        elif i < oneForward and l[i] in ["b", "B"] and l[i+1] in ["e", "E"]:
            l[i] = "b"
            l.pop(i + 1)

        # Rule 7:
        elif i < twoForward and l[i] in ["s", "S"] and l[i+1] in ["e", "E"] and l[i+2] in ["e", "E", "a", "A"]:
            l[i] = "c"
            l.pop(i + 1)
            l.pop(i + 1)

        # Rule 8:
        elif i < twoForward and l[i] in ["e", "E"] and l[i+1] in ["y", "Y"] and l[i+2] in ["e", "E"]:
            l[i] = "i"
            l.pop(i + 1)
            l.pop(i + 1)

        # Rule 9:
        elif i < twoForward and l[i] in ["o", "O"] and l[i+1] in ["w", "W"] and l[i+2] in ["e", "E"]:
            l[i] = "o"
            l.pop(i + 1)
            l.pop(i + 1)

        elif i < oneForward and l[i] in ["o", "O"] and l[i+1] in ["h", "H"]:
            l[i] = "o"
            l.pop(i+1)


        # Rule 10:
        elif i < twoForward and l[i] in ["a", "A"] and l[i+1] in ["r", "R"] and l[i+2] in ["e", "E"]:
            l[i] = "r"
            l.pop(i+1)
            l.pop(i+1)

        # Rule 11:
        elif i < twoForward and l[i] in ["y", "Y"] and l[i+1] in ["o", "O"] and l[i+2] in ["u", "U"]:
            l[i] = "u"
            l.pop(i+1)
            l.pop(i+1)

        elif i < twoForward and l[i] in ["w", "W"] and l[i+1] in ["h", "H"] and l[i+2] in ["y", "Y"]:
            l[i] = "y"
            l.pop(i+1)
            l.pop(i+1)

        if isUpperCase and l[i] in lowerCase:
            l[i] = upperCase[lowerCase.index(l[i])]

        oneForward = len(l) - 1
        twoForward = len(l) - 2
        threeForward = len(l) - 3
        i += 1

    return "".join(l)

test = False
if test:
    print("Twitterize the tests:\n1. Come at me one by one -> ", twitterize(list("Come at me one by one")))
    print("2. Four four Flour->", twitterize(list("Four four Flour")))
    print("3. Oh! ->", twitterize(list("Oh!")))
    print("4. oweh ->", twitterize(list("oweh")))
testcases = int(input())
for i in range(testcases):
    line = input()
    print(twitterize(list(line)))
