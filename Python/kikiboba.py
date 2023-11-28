# Problem Description: https://open.kattis.com/problems/kikiboba

word = input()
if word.count("b") > word.count("k"):
    print("boba")
elif word.count("k") > word.count("b"):
    print("kiki")
elif word.count("k") == word.count("b") == 0:
    print("none")
else:
    print("boki")
