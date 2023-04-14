# A solution to the problem: https://open.kattis.com/problems/wertyu

import sys
if __name__ == "__main__":
    shifts = list("`1234567890-=qwertyuiop[]\\asdfghjkl;\'zxcvbnm,./".upper())
    for line in sys.stdin:
        l = ""
        for letter in line:
            if letter in shifts:
                l+= shifts[shifts.index(letter)-1]
            else:
                l += letter
        print(l)
