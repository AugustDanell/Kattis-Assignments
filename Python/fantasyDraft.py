# 665 Kattis, a solution to the problem: https://open.kattis.com/problems/fantasydraft?tab=metadata

''' General Solution Idea:
    This problem is all about effective code, that is to write code in a reasonable time complexity. We can use a combination of hashmaps (constant lookup / removal / insertion) in
    the average case and deques. A deque can be used like a double linked list so that we can remove the first element without refactoring the list, in constant time that is.
    What we can do is to save every player in a deque and in a hashmap, and we also save lists for teams' prefered players. We exhaust the list of prefered players by taking them from
    the hashmap. Once a team has no players to take from the hashmap we let them take from the deque that holds the players. Basically we pop from the left in this deque. We then take
    the element to see that it is still in the hashmap (so not another team has taken the member). The whole ordeal is a combination of linear terms which is why this code works.
'''

from collections import deque

# 1. Read in the data and intialize the lists of teams' preferences:
n,k = list(map(int,input().split()))
pref_list = []
for _ in range(n):
    preferences = deque((input().split())[1:])
    pref_list.append(preferences)

# 2. Read in the players and put them both in the hashmap "players" and the deque "total_namelist":
p = int(input())
players = {}
total_namelist = deque([])
for _ in range(p):
    player = input()
    players[player] = True
    total_namelist.append(player)

# 3. Initalize a list of lists for every team:
teams = []
for _ in range(n):
    teams.append([])

# 4. Iterate over n*k, that is to say, how many teams we have times how many players each team wants:
team_number = 0
i = 0
while i < n*k:
    
    # 5. In the iteration, start with setting the flag "found_player" to false and extract a deque of prefered players:
    prefered_players = pref_list[team_number]
    found_player = False
    
    # 6. Pop the leftmost player of the deque until the deque is empty or until we have found a non-taken player:
    while len(prefered_players) > 0 and not found_player:
        next_player = prefered_players.popleft()
        if next_player in players:
            found_player = True
            teams[team_number].append(next_player)
            players.pop(next_player)
    
    # 7. If we still have not found a player for the current team we check the deque where all players were kept and we pop it until we find a non-taken player (O(N)):
    while not found_player:
        next_player = total_namelist.popleft()
        if next_player in players:
            found_player = True
            teams[team_number].append(next_player)
            players.pop(next_player)
    
    # 8. Update the data for the next iteration:
    team_number = (team_number+1)%n
    i+= 1

# 9. Lastly, we iterate over each team and we print their players using the join function.
for team in teams:
    print(" ".join(team))
