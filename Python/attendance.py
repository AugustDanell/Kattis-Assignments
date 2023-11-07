# Problem Description: https://open.kattis.com/problems/attendance2

'''
    General Solution:
    1. Iterate over every name and save them to the list: allNames.
    2. During each iterative, save the last name.
    3. If "Present!" is called, add the last name to a list: presentNames.
    4. Lastly, iterate over every name and print them if they are NOT in presentNames.
'''

if __name__ == "__main__":
    N = int(input())
    prevName = ""
    allNames = []
    presentNames = []
    for _ in range(N):
        name = input()
        if name == "Present!":
            presentNames.append(prevName)
        else:
            allNames.append(name)
            prevName = name

    if len(presentNames) == len(allNames):
        print("No Absences")
    else:
        for student in allNames:
            if student not in presentNames:
                print(student)
#    print(allNames, presentNames)
