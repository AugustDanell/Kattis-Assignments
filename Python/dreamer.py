# Problem Description: https://open.kattis.com/problems/dreamer
'''
    General Solution:
    1. Use itertools to generate every permutation of every possible date (8! variations)
    2. Check that every permutation is unique.
    3. Check that the permutation is valid.
    4. Check if it is the current best one, if so save it.
    5. Print the globally best date. 
'''

from itertools import permutations
def dateToNumeric(date):
    return date[0] + date[1]*32 + date[2]*13*32

def formatDateToStr(date):
    ans = list(map(str, date))
    if len(ans[0]) == 1:
        ans[0] = "0" + ans[0]
    if len(ans[1]) == 1:
        ans[1] = "0" + ans[1]

    return " ".join(ans)
def isLeapYear(n):
    if n % 400 == 0:
        return True
    elif n % 100 == 0 and n % 400 != 0:
        return False
    elif n % 4 == 0 and n % 100 != 0:
        return True
    elif n % 4 != 0:
        return False
def isValidDate(d, m, y, monthMapping):
    ceilDay = -1
    if m == 2:
        ceilDay = int(isLeapYear(y)) + 28
    elif m < 1 or m > 12:
        return 0
    else:
        ceilDay = monthMapping[m]
    if d < 1 or d > ceilDay:
        return 0
    if y < 2000:
        return 0

    return [day, month, year]

if __name__ == "__main__":
    tests = int(input())
    for _ in range(tests):
        numbers = []
        data = list(input())
        for number in data:
            if number != " ":
                numbers.append(number)

        monthMapping = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31
        }

        allPermutations = list(permutations(numbers))
        bestDate = 0
        bestVal = -1
        counter = 0
        repetitionMap = {}
        for permutation in allPermutations:
            day = int(str(permutation[0]) + str(permutation[1]))
            month = int(str(permutation[2]) + str(permutation[3]))
            year = int(str(permutation[4]) + str(permutation[5]) + str(permutation[6]) + str(permutation[7]))
            repeatStr = ""
            for c in permutation:
                repeatStr += c

            if repeatStr in repetitionMap:
                continue

            repetitionMap[repeatStr] = True
            date = isValidDate(day, month, year, monthMapping)
            if date != 0:
                counter += 1
                val = dateToNumeric(date)
                if bestVal == -1 or bestVal > val:
                    bestVal = val
                    bestDate = date
        #print(repetitionMap)
        if bestDate != 0:
            print(counter, formatDateToStr(bestDate))
        else:
            print(0)
