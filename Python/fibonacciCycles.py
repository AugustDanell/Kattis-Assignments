# fibonacci cycles
# There is a classic recursive algorithm for finding fibonacci sequences. The problem with that implementation is that
# a lot of work is done more than once (Many more times for larger n). A solution to that is either a memo version or
# a buttom_up approach (Dynamic Programming). We will use the later. For quick look ups we use a dictionary.

def buttom_up_fib(n):

    prev = 1
    curr = 1

    if(n <= 1):
        return 1
    else:
        for i in range(n-1):
            temp = curr
            curr = curr + prev
            prev = temp

    return curr

# Just test the base function:
assert buttom_up_fib(3) == 3
assert buttom_up_fib(4) == 5

# Q queries:
for i in range(int(input())):
    mod = int(input())
    n = 2
    number_dict = {}
    while(True):
        fib = buttom_up_fib(n) % mod
        if(number_dict.__contains__(fib)):
            n = number_dict[fib]
            break

        number_dict[fib] = n
        n += 1

    print(n)
