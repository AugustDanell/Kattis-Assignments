# 695th Kattis. A solution to the problem: https://open.kattis.com/problems/nizovi

''' General Solution: character handling
    Use two lists, l and word. Word is used for concatenating letters and l is used
    as a list for the entire paragraph. Brackets and commas are handled separetly
    and have special rules for them according to the assignment. Commas create a
    newline if they are not preceeded by a bracket (special rule 0). Brackets 
    themself are added and they increment a space counter and empty the word (rule 1).
    Commas create a new line and put the word into the text (rule 2).
    Normal letters are just added into word (rule 3). 
'''

spaces = 0
l = []
word = []
for character in list(input()):
  
    # 0 Special handling for adding new line to specific previous elemetns:
    if len(l) > 0 and not character == "," and l[-1] in ["{", "}"]:
        l[-1] += "\n"

    # 1. Handle brackets:
    if character in ["{", "}"]:
        if len(word) > 0:
            if not word[-1] == "\n":
                word.append("\n")
            l.append("".join(word))
            word = []

        if character == "{":
            l.append(" " * spaces)
            l.append("{")
            spaces += 2
        else:
            spaces -= 2
            l.append(" " * spaces)
            l.append("}")

    # 2. Handle comma:
    elif character == ",":
        word.append(",\n")
        if not word == []:
            l.append("".join(word))
            word = []

    # 3. Handle normal letters:
    else:
        if len(word) == 0:
            word.append(" "*spaces)
        word.append(character)

print("".join(l))
