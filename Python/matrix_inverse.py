# Taken and modified from my own math library on Git:
# https://github.com/AugustDanell/Mathematics/blob/main/linear_algebra.py

def scalar_product(scalar, v):
    return list(map (lambda e : e*scalar, v))

def scalar_product_matrix(scalar, l):
    l2 = l.copy()
    for i in range(len(l2)):
        l2[i] = scalar_product(scalar,l2[i])
    return l2

def determinant_2x2(l):
    assert len(l[0]) == 2
    return l[0][0]*l[1][1] - l[1][0]*l[0][1]


def matrix_inverse_2x2(l):
    a,b = l[0][0], l[0][1]
    c,d = l[1][0], l[1][1]

    m2 = [[d, -b],[-c,a]]
    return scalar_product_matrix(1/determinant_2x2(l),m2)

from sys import stdin
mod_three = 0
row_one = []
row_two = []
cases = 1
A_inv = []

for line in stdin:
    mod_three = (mod_three + 1)%3
    
    if(mod_three == 1):
        row_one = list(map(int,line.split()))
    
    if(mod_three == 2):
        row_two = list(map(int,line.split()))
    
    if (mod_three == 0):
        print("Case %d:"%(cases))
        A_inv = matrix_inverse_2x2([row_one, row_two])
        row_one, row_two = A_inv
        print(int(row_one[0]), int(row_one[1]))
        print(int(row_two[0]), int(row_two[1]))
        cases += 1
