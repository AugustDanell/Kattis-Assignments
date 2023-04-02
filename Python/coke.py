# A solution to the problem: https://open.kattis.com/problems/coke

# General Idea
# 1. Exhaust all the tens that we have and buy a coke with them. 
# 2. For every ten we have we can increment our 1-coins with 2 (1 insertion) or we can put in three one-coins to increment the five-coins (total of 4 insertions). 
# I call this "borrowing as I put into a list how many 5's I have borrowed. This is then passed into a function dealing with fives and ones.
# 3. When I have an amount of fives and ones I first try to solve by using two fives (2 insertions). I then try to do five + 3 ones (4 insertions). If we are
# all out of five coins, and we still need more coke, we insert 8 1-coins (8 insertions per coin).


# A function that inserts all the tens and returns a burrow list:
def insert_tens(C,n_1,n_10):
    burrow_list = [0]
    counter = 0
    while C > 0 and n_10 > 0:
        C -= 1
        n_10 -= 1
        if n_1 >= 3:
            burrow_list.append(burrow_list[-1] + 1)
            n_1 -= 3
        else:
            n_1 += 2
        counter += 1

    return burrow_list,C,counter

# A function that optimally places fives and ones:
def ones_fives(C, n_5):
    s = 0
    # 1. For every n_5 more than C we double use 5:
    if n_5 > C:
        left_over = n_5 - C
        if (n_5//2 >= C):
            return 2*C
        else:
            C -= (left_over)
            s += 2*(left_over)
            n_5 = C

    # 2. Now we use 5 + 3*1
    C -= n_5
    s += 4*n_5

    # 3. Now we only have ones left:
    s += 8*C

    return s

# The Main function of the program, I made it a function since I wanted to do unit tests:.
def min_coins(C, n_1, n_5, n_10):
    # 1. Create a burrowlist and a new C with insertion of only tens:
    borrow_list, C, ten_counter = insert_tens(C, n_1, n_10)
    if C == 0:
        return ten_counter

    # 2. Iterate over every borrowed 5:
    min_coins = ten_counter
    for i in range(len(borrow_list)):
        borrow = borrow_list[i]
        
        # 3. For every "borrowed" five we insert it into min coins.
        coins = ten_counter + borrow * 3 + ones_fives(C, n_5 + borrow)
        if i == 0 or coins < min_coins:
            min_coins = coins

    return min_coins

# Normally I dont do test code often but for this problem I had to:
assert((insert_tens(4, 0, 8)[2]) == 4)
assert((insert_tens(8, 0, 4)[2]) == 4)
assert (len((insert_tens(10, 0, 20)[0])) > 0)
assert min_coins(2, 2, 1, 1) == 5
assert min_coins(2, 1, 4, 1) == 3
assert min_coins(20, 200, 3, 0) == 148
assert min_coins(15, 100, 10, 0) == 80
assert min_coins(13, 0, 10, 10) == 16
assert min_coins(5, 0, 10, 0) == 10
assert min_coins(6, 10, 10, 0) == 16

# 1. Driver Code, for every testcase, parse the data and pass it to the main code. Print the result:
testcases = int(input())
for _ in range(testcases):
    C, n_1, n_5, n_10 = list(map(int, input().split()))
    print(min_coins(C, n_1, n_5, n_10))
