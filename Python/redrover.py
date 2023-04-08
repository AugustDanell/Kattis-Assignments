# Red Rover
# A naive solution to the problem: https://open.kattis.com/problems/redrover
# Naive in that the solution iterates over indices in which the answer cannot exist. The solution is quick enough though:

# 1. This is a minimization problem so initiate global_ans to be the worst possible answer and read in the string s:
s = input()
global_ans = len(s)


if __name__ == "__main__":
    # 2. Iterate over every possible size (actually sizes over len(s)/2 will always be suboptmial):
    for size in range(0, len(s), 1):

        # 3. Create the substring of a given size:
        for index in range(0, len(s), 1):
            sub_string = s[index:size + index]

            # 4. Calculate the new string using the macro and the cost of writing the macro itself:
            rep_string = s.replace(sub_string, "M")
            local_ans = len(rep_string) + size

            # 5. If this cost is less than the current global max we saive it:
            if local_ans < global_ans:
                global_ans = local_ans

    # 6. Print the global max:
    print(global_ans)
