if __name__ == "__main__":
    R, C = list(map(int,input().split()))
    total = C-1 + (C*(R-1))
    print(["Alf", "Beata"][int(total % 2 == 0)])