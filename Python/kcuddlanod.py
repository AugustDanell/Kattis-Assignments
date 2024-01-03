# Problem Description: https://open.kattis.com/problems/kcuddlanod
def getText(text):
    text = text.replace("2", ".")
    text = text.replace("5", "2")
    text = text.replace(".", "5")
    return text[::-1]

if __name__ == "__main__":
    t1, t2 = list(map(getText, input().split()))
    s1, s2 = int(t1), int(t2)
    print(["1", "2"][s2 > s1])
