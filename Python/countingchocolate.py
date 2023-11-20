# Problem Description: https://open.kattis.com/problems/countingchocolate

'''
    General Solution:
    A) The solution here is to use dynamic programming to reach the target sum of
    N // 2. If one person can reach that sum, then the remainder of the chocolates
    would also get N // 2 chocolate pieces. We can always get 0 pieces (by refusing
    every box).

    B) From there we can update our dynamic programming array (partialSums)
    by checking to see if partialSums(j-chocolate) is true. For example, if we have
    a chocolate box of 4. We can update it as true by seeing that partialSums(j-4 = 0) = True.

    C) Dynamically we can keep going until every chocolate is tested. If, by that point, the
    target is reached, we return True, else we return False.
'''
def canSplitChocolate(chocolates):
    totalChocolates = sum(chocolates)

    # 1. If the total number of chocolates is odd, it's not possible to split equally
    if not totalChocolates % 2 == 0:
        return "NO"

    # 2. Target sum for each group
    targetSum = totalChocolates // 2

    # 3. Initialize a boolean array to store which sums are possible
    partialSums = [False] * (targetSum + 1)
    partialSums[0] = True

    # 4. Iterate through each chocolate box and update the partialSums array:
    for chocolate in chocolates:
        for j in range(targetSum, chocolate - 1, -1):
            if partialSums[j-chocolate]:
                partialSums[j] = True

    # 5. If the target sum is achievable, it means we can split the chocolates equally
    if partialSums[targetSum]:
        return "YES"
    else:
        return "NO"

if __name__ =="__main__":
    # 1. Read input
    n = int(input())
    chocolates = list(map(int, input().split()))

    # 2. Output the result
    print(canSplitChocolate(chocolates))
