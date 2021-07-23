cards = int(input())
card_deck = list(map(int,input().split()))
card_deck.sort()

score_sum = 0
lowest_sum = 0
is_consequitive = False
for i in range(cards-1):
    if(card_deck[i+1] - card_deck[i] == 1):
        if(not is_consequitive):
            is_consequitive = True
            lowest_sum = card_deck[i]
    else:
        is_consequitive = False
        score_sum += lowest_sum
        if(lowest_sum == 0):
            score_sum += card_deck[i]
        lowest_sum = 0

if(not card_deck[cards-1] - card_deck[cards-2] == 1):
    print(score_sum + card_deck[cards-1])

elif (lowest_sum > 0):
    print(score_sum + lowest_sum)

else:
    print(score_sum)

