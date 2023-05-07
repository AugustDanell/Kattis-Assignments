# Insert a binary string and a sub set and get back the sum for the indices where i = 1 in the binary str:
def get_sum(binary_str, sub_set):
    s = 0
    for i in range(len(binary_str)):
        if binary_str[i] == "1":
            s += sub_set[i]
    return s

# Create a binary string of length N, and numeric value s:
def create_binary_str(N, s):
    bin_str = bin(s)[2:]

    # Add Padding:
    while len(bin_str) < N:
        bin_str = "0" + bin_str
    return bin_str

# Take in two binary strings that evaluate to the same numeric value. Print the terms they use from the subset:
def print_answers(bin_str1, bin_str2, subset):
    for i in range(len(bin_str1)):
        if bin_str1[i] == "1":
            print(subset[i], end = " ")
    print()

    for i in range(len(bin_str2)):
        if bin_str2[i] == "1":
            print(subset[i], end = " ")
    print()

if __name__ == "__main__":
    testcases = int(input())
    
    # 1. Iterate over every testcase and initiate an empty hashmap for answers, read in the subset, and initate a false flag:
    for i in range(testcases):
        print("Case #{0}:".format(i+1))
        subset = list(map(int,input().split()))[1:]
        N = 20
        answers = {}
        found = False
        
        # 2. Iterate over each possible combination of subset. Save their numeric value into answers. If two equals are found, mark found, and print. Else continue:
        for Y in range(1, 2**N+1):
            bin_str = create_binary_str(N, Y)
            s = get_sum(bin_str, subset)
            if s in answers:
                found = True
                bin_str_1 = answers[s]
                bin_str_2 = bin_str
                print_answers(bin_str_1, bin_str_2, subset)
                break
            else:
                answers[s] = bin_str
        
        # 3. If we have iterated over step 2 and not found two equals then we print that it is impossible:
        if not found:
            print("impossible")
