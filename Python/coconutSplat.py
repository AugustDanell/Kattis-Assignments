''' General Solution Idea:
    Just iterate through the test cases, play the game by hand and compare to the python solution. This problem was seemingly easy yet more complicated and time
    consuming for me than it had to be. Its easy to make a mistake. My solution starts with setting the players according to rule 1 to "C %d" where %d is the number
    of the corrosponding player. The game is iterated until there is only one player left (this is checked quickly via a hashmap in "game_alive()". Every turn a
    pick is calculated according to the remaining amount of player and according to what was the provided number of syllables. A pick is made meaning we apply one
    of the rules on that specific element and thereafter we set the turn accordingly. This is easy to get wrong so this is why it seems prudent to do the 10 2 case
    and 1 2 case on paper and check to see if the rounds align with that, I tested it lazily with a print statement at row 30. 
'''

def game_alive(l):
    prevPlayers = {}
    for i in l:
        player = i.split()[1]
        if(not prevPlayers.__contains__(player) and len(prevPlayers) > 0):
            return True
        else:
            prevPlayers[player] = True

    return False

syllabels, players = list(map(int, input().split()))
hand_list = []
current_turn = 0

for i in range (players):
    hand_list.append("C %d" % (i+1))

round = 1
while(game_alive(hand_list)):
    #print("Round:", round, "Starting at:", current_turn, "List:", hand_list)
    pick = ((current_turn + syllabels) -1) % len(hand_list)
    s = hand_list[pick].split()

    if(s[0] == "C"):
        hand_list[pick] = "c %s" % s[1]
        hand_list.insert(pick, "c %s" % s[1])
        current_turn = pick

    elif(s[0] == "c"):
        hand_list[pick] = "t %s" % s[1]
        current_turn = (pick + 1)%len(hand_list)

    else:
        hand_list.pop(pick)
        current_turn = pick

    round += 1

print(hand_list[0].split()[1])
