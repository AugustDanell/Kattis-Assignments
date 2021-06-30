word = list(input())
guess = list(input())

lives = 10
for i in guess:
    #print(word)

    if(len(word) == 0):
        break

    if(word.__contains__(i)):
        while(word.__contains__(i)):
            word.remove(i)

    else:
        lives = lives -1

if(lives > 0):
    print("WIN")
else:
    print("LOSE")