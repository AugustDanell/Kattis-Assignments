if __name__ == "__main__":
    P, W  = list(map(int, input().split()))
    steps = int((W/100)*P)
    progressBar = "[" + "#"*steps + "-"*(W-steps) + "]"
    print(progressBar, end = " ")
    suffix = " " + str(P) + "%"
    while len(suffix) < 5:
        suffix = " " + suffix
    print("|" + suffix)