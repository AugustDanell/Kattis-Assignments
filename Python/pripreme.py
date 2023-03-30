# A solution to the problem: https://open.kattis.com/problems/pripreme

# General Idea:
# If one team is slower than all other teams the first teacher will loop around to that team and the time will be that team times two.
# Else the time will be the aggregated time of every team.

n = int(input())
teams = sorted(list(map(int,input().split())), reverse=True)
if teams[0] > sum(teams[1:]):
    print(teams[0]*2)
else:
    print(sum(teams))
