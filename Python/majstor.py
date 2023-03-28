# 1. Input:
rounds = int(input())
sven = list(input())
friends = int(input())
columns = []
for _ in range(rounds):
    columns.append([])

# 2. Calculate the actual score and also make sure to append to a list that stores every column played:
score = 0
for _ in range(friends):
    friend = list(input())

    for i in range(rounds):
        if sven[i] == "S":
            if friend[i] == "P":
                score += 2
            elif friend[i] == "S":
                score += 1

        if sven[i] == "P":
            if friend[i] == "R":
                score += 2
            elif friend[i] == "P":
                score += 1

        if sven[i] == "R":
            if friend[i] == "S":
                score += 2
            elif friend[i] == "R":
                score += 1

        columns[i].append(friend[i])

# 3. For every column, calculate the score of playing every role. Increment the optimal score by the max of these 3 scores:
optimal_score = 0
for col in columns:
    S,P,R = col.count("S"), col.count("P"), col.count("R")
    S_score = 2*P + S
    P_score = 2*R + P
    R_score = 2*S + R
    optimal_score += max(S_score, P_score, R_score)

# 4. Print score and optimal score, as per the description of the problem
print(score)
print(optimal_score)
