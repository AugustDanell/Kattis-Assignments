def fib(n):
    f1 = 1
    f2 = 1
    f3 = 2

    l = [f1,f2,f3]
    while f3 <= n:
        f1 = f2
        f2 = f3
        f3 = f2 + f1
        l.append(f3)
    return l

if __name__ == "__main__":
    n = int(input())
    l = fib(n)
    sum_list = []
    while n > 0:
        if l[len(l)-1] <= n:
            difference = l[len(l)-1]
            n -= difference
            sum_list.append(difference)
        else:
            l.pop()
    print(" ".join(map(str,sorted(sum_list))))
