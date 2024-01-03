# Problem Description: https://open.kattis.com/problems/pubrunda
if __name__ == "__main__":
    N = int(input())
    maxTime = 0
    bestPub = "_"
    for _ in range(N):
        pub, ppl, queue = input().split()
        queue = int(queue)
        ppl = int(ppl)
        totalTime = queue*(ppl+1)
        if totalTime > maxTime:
            bestPub = pub
            maxTime = totalTime

    print(bestPub, maxTime)
