# A ugly solution to the more so beautiful problem: https://open.kattis.com/problems/zigzag

if __name__ == "__main__":
    n = int(input())
    l = ["a"]
    if n <= 25:
        print("a" + chr(97+n))

    else:
        a = False
        while n > 0:
            n -= 25
            if a:
                l.append("a")
            else:
                l.append("z")
            a = not a
        a = not a

        if n % 2 == 1:
            if a:
                l[-1] = "b"
            else:
                l[-1] = "y"
        n+=1

        while n < 0:
            n+=2
            l[1] = chr(ord(l[1])-1)

        print("".join(l))
