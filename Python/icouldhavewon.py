# A solution to the problem: https://open.kattis.com/problems/icouldhavewon
game = list(input())
valid_k = []
for k in range(1, len(game)+1):
    score = [0, 0]
    games = [0, 0]

    for i in range(len(game)):
        if game[i] == "A":
            score[0] += 1
        else:
            score[1] += 1

        if score[0] == k:
            games[0] += 1
            score = [0,0]
        elif score[1] == k:
            games[1] += 1
            score = [0,0]

    if games[0] > games[1]:
        valid_k.append(str(k))

print(len(valid_k))
print(" ".join(valid_k))
