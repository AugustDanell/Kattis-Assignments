# A solution to the problem: https://open.kattis.com/problems/perket

# General idea: Take in the list of ingredients and brute force every choice
def brute_force(l):

    # 1. Initiate the global diff to be 0 but set it at first given time:
    global_diff = 0
    
    # 2. Iterate over every number from 1 to 2^n, this number corrosponds to a bit string signifying a choice. 1 = we take the ingredient, 0 = we dont:
    for i in range(1, 2**len(l)):
        binary_string = bin(i)[2:]
        sum_ = 0
        factor_ = 1

        # 3. Add Padding to the string so that it always corrosponds to all the choices:
        while len(binary_string) < len(l):
            binary_string = "0" + binary_string
        
        # 4. Iterate over the bit string, if we find a 1 we append that specific ingredient.
        for j in range(len(binary_string)):
            if binary_string[j]=="1":
                sum_ += int(l[j][1])
                factor_ *= int(l[j][0])
        
        # 5. Initiate a local diff which we assign to global diff if the differance is smaller than max. We also automatically assign it on first iteration: 
        local_diff = abs(sum_ - factor_)
        if i == 1 or local_diff < global_diff:
            global_diff = local_diff

    # 6. Return the smallest global difference:
    return global_diff

# 1. Read in the ingredients into a list and put the list into the brute force algorithm:
n = int(input())
ingredients = []
for _ in range(n):
    ingredients.append(list(map(int,input().split())))
print(brute_force(ingredients))
