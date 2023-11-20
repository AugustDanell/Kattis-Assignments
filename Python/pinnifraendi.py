if __name__ == "__main__":
    ans = list("0.")
    N = int(input()) - 1
    for _ in range(N):
        ans.append("0")
    ans.append("1")

    print("".join(ans))