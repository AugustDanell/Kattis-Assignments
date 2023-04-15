# Solution to the problem: https://open.kattis.com/problems/sim
'''
General Idea:
The idea is that we have a list of lists. The last list is always the textstring that ends the total string. Each time we recieve a [ token we can create a new list.
We can fill this new list with tokens. If we recieve another [ we create yet another list, and so on, and so forth. If we recieve the ] token we switch to just write
to the first list that we got. The < token will remove a character from any list unless we have emptied that list. This is unless we are on the first list, in which
case the < operator will overflow into the second list, etc. Essentially these list of lists form substrings and we just puzzle them together lastly.
'''

def handle_text(s):

    # 1. Initiate the list of lists, with the first list within it:
    l = [[]]
    first_row = True
    for letter in s:
      
        # 2. If the letter is [ this means that we should write to a new list. Check if it exists, else append it:
        if letter == "[":
            first_row = False
            if len(l[-1]) == 0:
                continue
            else:
                l.append([])
        
        # 3. If ] is the token this means that the flag first_row is true meaning that we will write to the first index list in l, meaning l[0]:
        elif letter == "]":
            first_row = True
        
        # 4. If the token is < this means that we will pop element either from the current list or from l[0]. l[0] is a bit special and can overflow into other lists:
        elif letter == "<":
            if first_row and len(l[0]) > 0:
                l[0].pop()
            elif first_row and len(l[0]) == 0 and len(l) > 1:
                if len(l[1]) == 0:
                    l.pop(1)
                else:
                    l[1].pop()
            elif not first_row and len(l[-1]) > 0:
                l[-1].pop()
                
        # 5. Else we append either into the last list or into the first depending on the flag:
        else:
            if first_row:
                l[0].append(letter)
            else:
                l[-1].append(letter)
    
    # 6. Print the results. We have to end with a empty print statement so to "flush" the output, lest we fail if T > 1:
    for i in range(len(l) - 1, -1, -1):
        print("".join(l[i]), end="")
    print()

if __name__ == "__main__":
    testcases = int(input())
    for _ in range(testcases):
        text = input()
        handle_text(text)
