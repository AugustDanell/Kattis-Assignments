# A solution to the problem: https://open.kattis.com/problems/palindromicpassword

''' Solution Idea:
    A Palindrome has to have even length so we can say that length Palindrome = 2N.
    We can generate every combination for a palindrome using the formula for a palindrome: x1 x2 x3 x3 x2 x1
    x1 can be [1,9] since there can be no leading zeroes.
    (x2,x3) can be [0,9]. This will equate to 10**2 + 9 combinations, for a total of 900 combinations to check. 
    This solution takes in a number and saves the closest palindrome. Since the check is made in ascending order
    the strictly less than operation will ensure that we always get the smallest answer (as asked of us) provided
    that there are multiple correct answers.
'''

def cloesest_palindrome(n):
    closest = -1
    for x1 in range(1,9+1):
        for x2 in range(0,9+1):
            for x3 in range(0,9+1):
                palindrome = x1 + x2*10 + x3 * 10**2 + x3*10**3 + x2*10**4 + x1*10**5
                if closest == -1:
                    closest = palindrome
                else:
                    dist = abs(palindrome-n)
                    if dist < abs(closest-n):
                        closest = palindrome
    return closest

if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        print(cloesest_palindrome(int(input())))
