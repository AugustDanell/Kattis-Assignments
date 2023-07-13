# Link to problem: https://open.kattis.com/problems/doubleplusgood

''' General Solution:
    We can use a binary string to generate all permutations of concatenations and additions. 
    Then we can use the sum function to sum every permutation.
    We can check every number in a map for being distinct.
'''


def concatenate(operands):
    b = 2**(len(operands)-1)
    l = []
    for i in range(b):
        numbers = [str(operands[0])]
        bin_str = bin(i)[2:]
        while (len(bin_str) < len(operands)-1):
            bin_str = "0" + bin_str
            
        for j in range(len(bin_str)):
            bit = bin_str[j]
            if bit == "0":
                numbers.append(str(operands[j+1]))
            else:
                numbers[-1] += str(operands[j+1])
        l.append(numbers)
    return l

operands = input().split("+")
list_of_numbers = concatenate(operands)
distinct = {}
found_numbers = 0
for l in list_of_numbers:
    l = map(int, l)
    s = sum(l)
    if s not in distinct:
        distinct[s] = True
        found_numbers += 1
        
print(found_numbers)
