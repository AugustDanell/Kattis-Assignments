# A Rank Problem
# This problem seems rather easy. We fill a list of the different teams.
# From that we can just change the order each time they play by
# popping the losing team if their index is lower than the winning team and then reinsert it.
# That's all. 

team_list = []
teams, queries = list(map(int, input().split()))

for i in range(teams):
    team_list.append("T%d" % (i+1))

for i in range(queries):
    W,L = input().split()
    W_index, L_index = team_list.index(W), team_list.index(L)
    if(W_index < L_index):
        # DO NOTHING BECAUSE IT IS AN EXPECTED VICTORY
        pass
    else:
        elem = team_list.pop(L_index)
        team_list.insert(W_index, elem)

print(" ".join(team_list))
