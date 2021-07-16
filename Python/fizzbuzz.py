N,M = list(map(int, input().split()))

correct_answers = []
for i in range(1,M+1,1):
    if(i % 3 == 0 and i % 5 == 0):
        correct_answers.append("fizzbuzz")
    elif(i%3 == 0):
        correct_answers.append("fizz")
    elif(i%5 == 0):
        correct_answers.append("buzz")
    else:
        correct_answers.append(str(i))

most_correct = 0
best_cand = 1

for candidate in range(N):
    candidate_string = input().split()
    points = 0

    for i in range(len(candidate_string)):
        if(candidate_string[i] == correct_answers[i]):
            points += 1

    if(points > most_correct):
        best_cand = candidate+1
        most_correct = points

print(best_cand)
