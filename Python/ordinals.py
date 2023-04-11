# A solution to the problem: https://open.kattis.com/problems/ordinals
if __name__ == "__main__":
    n = int(input())
    ord_map = {}
    ord_map[0] = "{}"
    for i in range(1, n+1):
        l = []
        for j in range(0, i):
            l.append(ord_map[j])
        s = ",".join(l)
        ord_map[i] = "{" + s + "}"

    print(ord_map[n])
