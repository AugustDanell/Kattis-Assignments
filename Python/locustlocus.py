# A Brute Force Solution to the problem: https://open.kattis.com/problems/locustlocus

''' General Solution:
    I attempted to write a more clean solution at first with extracting the highest common factor of two numbers and use that as a divisor to the product of the numbers.
    I think this in theory is a correct solution but I have made a mistake somewhere. I couldn't immediately find a testcase that broke the x*y/HCF scheme, so I decided
    to just brute force instead. Since the problem instance is pretty small brute forcing is well within the time limit of the problem. 
'''

def prime_factorization(n):
    l = []
    i = 2
    while i <= n:
        if n%i == 0:
            l.append(i)
            n = n//i
        else:
            i+= 1

    return l

  def hcf(x,y):
    x_list = prime_factorization(x)
    y_list = prime_factorization(y)
    hcf = 1
    visited = {}
    for x_i in x_list:
        if x_i in visited:
            continue
        if x_i in y_list:
            hcf *= min(x_list.count(x_i)*x_i, y_list.count(x_i)*x_i)
            visited[x_i] = True
    return (x*y)//hcf
  
def test_hcf():
    assert hcf(5,4) == hcf(4,5) == 20
    assert hcf(3,3) == 3
    assert hcf(4,2) == hcf(2,4) == 4
    assert hcf(20, 10) == hcf(10, 20) == 20
    assert hcf(7,3) == hcf(3,7) == 21
    assert hcf(31,3) == hcf(3, 31) ==93
    assert hcf(300,20) == hcf(20, 300) == (300*20)//20
    assert hcf(1, 31) == hcf(31, 1) == 31
    
def brute_force(x,y):
    start = max(x,y)
    for i in range(start, x*y+1):
        if i % x == 0 and i % y == 0:
            return i


if __name__ == "__main__":
    earliest_year = -1
    test_hcf()
    n = int(input())
    for _ in range(n):
        year, x, y = list(map(int,input().split()))
        current_year = year + brute_force(x,y)

        if earliest_year == -1 or current_year < earliest_year:
            earliest_year = current_year

    print(earliest_year)
