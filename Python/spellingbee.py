hex_word = list(input())
center_letter = hex_word[0]
letter_list = hex_word

matched_words = []
test_cases = int(input())
for i in range(test_cases):
    candidate = input()
    if(len(candidate) >= 4 and candidate.__contains__(center_letter)):
        bad_list = [x for x in candidate if(not x in letter_list)]
        #print(bad_list)
        if(len(bad_list) == 0):
            matched_words.append(candidate)

for i in matched_words:
    print(i)
