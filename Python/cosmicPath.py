# Problem: https://open.kattis.com/problems/cosmicpathoptimization

if __name__ == "__main__":
    N = int(input())
    L = list(map(int,input().split()))
    print(int(sum(L)/N))
