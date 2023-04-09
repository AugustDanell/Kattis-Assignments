# A solution to the problem: https://open.kattis.com/problems/awkwardparty

# 1. Read input. Initiate a global awkwardness and a list of people:
n = int(input())
global_awkwardness = n
people = list(map(int,input().split()))
last_person = {}

# 2. Iterate over every index and store the index of a speaker of a language. If that language comes again we can quickly calculate a local awkwardness:
for i in range(n):
    person = people[i]
    if person in last_person:
        local_awkwardness = i - last_person[person]

        # 3. The local awkwardness is quickly calculated. If it is now less than the global one we update the global counter:
        if local_awkwardness < global_awkwardness:
            global_awkwardness = local_awkwardness
    
    # 4. Lastly we document the index of person i:
    last_person[person] = i

# 5. And print the global result:
print(global_awkwardness)
