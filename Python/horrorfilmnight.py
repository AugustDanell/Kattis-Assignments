# 659th solution, a greedy solution to the problem: https://open.kattis.com/problems/horrorfilmnight

# A function to select the longest streak greedily:
def find_longest_streak(merged_list):
    # 1. Initialize the streak <- 0 and last_person <- -1.
    streak = 0
    last_person = "-1"
    
    # 2. Iterate over each movie:
    for movie in merged_list:
        
        # 3. Extract the person that likes the movie. If both like it, reset the last_person flag and increment the streak:
        person = movie[-1]
        if person == "both":
            streak += 1
            last_person = -1
        
        # 4. If the current person is not the same as the last person, the last person will have to watch this movie so we update the flag and increment the streak:
        elif not person == last_person:
            last_person = person
            streak += 1
            
        # 5. If the last person is the current person we do not increment the counter since that would violate the rule:
        else:
            last_person = person
    
    # 6. Return the streak:
    return streak

# 1. Read in the data:
l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))

# 2. Initialize in O(N) two dictionaries so that we can check overlap in constant time later:
d1 = {}
d2 = {}
for i in range(1, len(l1)):
    e = l1[i]
    d1[e] = True
for i in range(1, len(l2)):
    e = l2[i]
    d2[e] = True

# 3. Create a list that is the merged lists of l1 and l2, lableing overlaps as "both", else labling the index of the person:
merged_list = []
for i in range(1, len(l1)):
    if l1[i] in d2:
        e1 = [l1[i], "both"]
    else:
        e1 = [l1[i], "1"]
    merged_list.append(e1)
for i in range(1, len(l2)):
    if(not l2[i] in d1):
        e2 = [l2[i], "2"]
        merged_list.append(e2)

# 4. Create a lambda function as a key to sort the list based on the day of the movie, such that we have an ascending order of movies:
sorting_function = lambda x: x[0]
merged_list = sorted(merged_list, key = sorting_function)

# 5. Print the longest streak that we can find via a greedy search:
print(find_longest_streak(merged_list))
