logs = int(input())
users = 0
user_list = {}
word_occurance = {}
unique_occurances = {}
used_by = {}

'''
    Stepwise solution:
    1. Four dictionaries:
        - One keeps track of the global use of every word (word_occurance)
        - The other keeps track of unique occurances, that is, how many times a word uniquely has been used.
        - The dictionary "used_by" takes a word and outputs a dictionary where a word can be provided and either
          true or false is returned, a meshed dictionary taking in a name and a word to see if that word is used
          by that user.
        - User list, a dictionary that keeps track of users so we can increment the counter "users" if there a new
          user comes in. The counter "users" is useful because in step 2 we need it to generate a list of valid words.
    
    2. Generate a list of valid words:
       We create a new empty list and we only append words that match their unique_occurance to that of the counter.
       
    3. Sorting and printing:
       Lastly we sort and we print, we start with sorting alphabetically (lexiographically) and then we apply an own sort
       to the sorted list to override it we the amount of total occurances. 
'''

def opt_bubble_sort(list, d):
    n = len(list)
    for i in range(n):
        for j in range(n-i-1):
            if (d[list[j+1]] > d[list[j]]):
                list[j], list[j + 1] = list[j + 1], list[j]

    return list

# 1: Suffering with dictionaries.
for i in range(logs):
    log = input().split()
    name = log[0]

    if(not used_by.__contains__(name)):
        used_by[name] = {}

    if(not user_list.__contains__(name)):
        user_list[name] = True
        users += 1

    for w in log[1:]:
        if(word_occurance.__contains__(w)):
            word_occurance[w] += 1
        else:
            word_occurance[w] = 1

        if(not used_by[name].__contains__(w)):
            (used_by[name])[w] = True

            if(not unique_occurances.__contains__(w)):
                unique_occurances[w] = 1
            else:
                unique_occurances[w] += 1

# 2:
l = []
for u in unique_occurances:
    if(unique_occurances[u] == users):
        l.append(u)

l.sort()
l = opt_bubble_sort(l, word_occurance)

for w in l:
    print(w)

if(l == []):
    print('ALL CLEAR')
#print(unique_occurances)
#print(word_occurance)
