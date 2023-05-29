# 694th Kattis. Solution to the problem: https://open.kattis.com/problems/opensource

''' General Solution: Dictionaries for bookkeeping and sorting functions.
    We read in companies and people signing up for said companies and we bookkeep the
    system in constant time with three dictionaries. Two dictionaries map each person
    to a company and each company to the set of assigned people, respectively. The 
    last dictionary is a so called "skip list" used to skip people who have been 
    subtracted for. Basically we save each person and if they occur more than twice 
    we subtract them from the first company and then put the person on the skiplist.
    If a person is assigned more than once to the same company we also skip.
    
    Then when "1" is inputted we put our dictionary of how man ppl each company has
    to the function handle_two_sort. In there we use a lambda function to sort on 
    the value. We then partition each group of a certain value into l and we put l
    inside a larger list called L which we then return. Lastly we then just iterate
    over every entry in L.
'''

import sys

def handle_two_sort(company_to_score):
    keys = company_to_score.keys()
    sorting_func = lambda company: company_to_score[company]
    sorted_companies = sorted(keys, key = sorting_func, reverse=True)
    L = []
    prev = -1
    l = []
    for key in sorted_companies:
        if company_to_score[key] == prev:
            l.append(key)
        else:
            if not prev == -1:
                L.append(l)
            l = [key]
        prev = company_to_score[key]
    if len(l) > 0:
        L.append(l)
    return L


person_to_company = {}
company_to_score  = {}
skip_list = {}
for line in sys.stdin:
    line = line.strip()
    if line == "1":
        L = handle_two_sort(company_to_score)
        index = 0
        while index < len(L):
            l = sorted(L[index])
            for key in l:
                print(key, company_to_score[key])
            index += 1

        company_to_score  = {}
        person_to_company = {}


    elif line == "0":
        break
    elif line[0].isupper():
        company = line
        company_to_score[company] = 0
    else:
        person = line
        if (person in person_to_company and person_to_company[person] == company) or person in skip_list:
            continue
        elif person in person_to_company:
            c = person_to_company[person]
            company_to_score[c] -= 1
            person_to_company.pop(person)
            skip_list[person] = True
        else:
            person_to_company[person] = company
            company_to_score[company] += 1
