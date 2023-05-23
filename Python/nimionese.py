# 683th Kattis Solution. A solution to the problem: https://open.kattis.com/problems/nimionese

''' General Solution:
    Apply the rules and transform every word according to nimionese grammer.
    Then just output every word. Straightforward. 
''' 

def dist(c1, c2):
    return abs(ord(c1) - ord(c2))

def find_closest(c1, hard_consonants):
    global_d = -1
    closest_letter = -1
    for c2 in hard_consonants:
        local_d = dist(c1,c2)
        if global_d == -1 or local_d < global_d:
            global_d = local_d
            closest_letter = c2
        elif local_d > global_d:
            break

    return closest_letter

def rule_one(w, hard_consonants):
    w[0] = w[0].lower()
    replace_letter = find_closest(w[0], hard_consonants)
    w[0] = replace_letter

def rule_two(w, hardconsonants):
    replace_letter = w[0]
    index = 0
    makeReplace = False
    while index < len(w):
        if w[index] == "-":
            #replace_letter = w[index+1]
            makeReplace = True
            w.pop(index)
        else:
            if makeReplace and w[index] in hardconsonants:
                w[index] = replace_letter
            index += 1

    return w

def rule_three(w, vowels, hardconsonants):
    if w[-1].lower() not in hardconsonants:
        return

    closest = find_closest(w[-1], vowels)
    w.append(closest)
    w.append("h")

hard_consonants = list("(bcdgknpt")
vowels = ["a", "o", "u"]
in_words = input().split(" ")
out_words = []
for i in range(len(in_words)):
    word = list(in_words[i])
    is_capital = word[0].isupper()
    rule_one(word, hard_consonants)
    rule_two(word, hard_consonants)
    rule_three(word, vowels, hard_consonants)
    if is_capital:
        word[0] = word[0].upper()
    out_words.append(word)

for word in out_words:
    print("".join(word), end = " ")
