if __name__ == "__main__":
    rows, cols = list(map(int,input().split()))
    letters = []
    for _ in range(rows):
        s = input()
        for letter in s:
            if letter != ".":
                letters.append(letter)
    
    print("".join(letters))