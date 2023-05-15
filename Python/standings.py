# 660th Solution. A solution to the problem: https://open.kattis.com/problems/standings

# 1. Read in the testcases:
testcases = int(input())
for _ in range(testcases):
    input()
    N = int(input())
    
    # 2. Initiate a list of teams and add each team and their favorite spot:
    teams = []
    for _ in range(N):
        name, prefered_place = input().split()
        teams.append([name, int(prefered_place)])
  
    # 3. Pass in a sorting key for sorting based on prefered ranking
    sorting_key = lambda x: x[1]
    teams = sorted(teams, key = sorting_key)
    
    # 4. Define a "badness" by comparing the absolute value of the ranking and the prefered ranking and aggregate the residual:
    badness = 0
    for i in range(1, N+1):
        team = teams[i-1]
        rating = team[1]
        badness += abs(rating-i)
        
    # 5. Print the badness:
    print(badness)
