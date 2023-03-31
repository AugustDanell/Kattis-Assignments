# A solution to the problem: https://open.kattis.com/problems/smartphone

# Function to return the maximum distance between two words:
def abs_dist(w1,w2):
    return abs(len(w1) - len(w2))

# A function that calculate the difference between two words using the backspace operation as specified:
def calculate_word_diff(target, word):
    prefixed_index = 0
    while prefixed_index < len(word) and prefixed_index < len(target):
        if word[prefixed_index] == target[prefixed_index]:
            prefixed_index += 1
        else:
            break
    removals = len(word) - prefixed_index
    appendages = len(target) - prefixed_index
    return (removals + appendages)

# 1. Read in testcases:
testcases = int(input())
for _ in range(testcases):
    
    # 2. Initiate a target word:
    wanted_word = input()
    
    # 3. Initiate a start word:
    start_word = input()
    
    # 4. Initiate a global counter for how many operations are needed when just applying backspace directly:
    global_diff = calculate_word_diff(wanted_word,start_word)
    
    # 5. See if we can improve the amount of operations by looking through every candidate word, add 1 since pressing suggestion = 1 operation:
    for i in range(3):
        candidate_word = input()
        local_diff = calculate_word_diff(wanted_word, candidate_word) + 1
        if local_diff < global_diff:
            global_diff = local_diff
            
    # 6. Output the minimum amount of operations i.e keypresses.
    print(global_diff)
