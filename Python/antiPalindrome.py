# Problem Description: https://open.kattis.com/problems/antipalindrome

'''
    General Solution:
    Basically the problem is to determine if a palindrome can be made of a substring
    that omits anything other than alphabetic characters. The solution is trivial,
    we can brute force test every substring.
'''

def filter(text):
    newText = []
    for c in text:
        if 65 <= ord(c) <= 90:
           newText.append(chr(ord(c)+32))
        elif 97 <= ord(c) <= 122:
            newText.append(c)
    return "".join(newText)

def isPalindrome(text):
    for i in range(len(text)//2):
        if(not (text[i] == text[len(text)-1-i])):
            return False
    return True

if __name__ == "__main__":
    text = filter(input())
    palindromeFlag = False
    for start in range(len(text)-1):
        for end in range(start+1, len(text)):
            subStr = text[start:end+1]
            if isPalindrome(subStr):
                palindromeFlag = True
                break
            if palindromeFlag:
                break

    if palindromeFlag:
        print("Palindrome")
    else:
        print("Anti-Palindrome")
