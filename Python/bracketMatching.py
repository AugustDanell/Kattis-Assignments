# Input:
n = int(input())                                    # The amount of brackets
bracketList = list(input())                         # The list of brackets.
bracketInv = [")", "}", "]"]                        # A list of closing brackets, used with bracketConversion.
bracketConversion = {")" : "(", "}":"{", "]":"["}   # A dictionary to convert closing brackets to corrosponding opening.
invalid = False                                     # A flag to discern validity.
openingBrackets = []                                # A stack to push opening brackets to.

# Iterate through every bracket:
for bracket in bracketList:

    # A) We get an opening bracket as bracket, push the bracket to the stack: 
    if not bracket in bracketInv:
        openingBrackets.append(bracket)

    # B) We get a closing bracket as bracket:
    else:
        # 1. If there are no open brackets currently, return invalid: 
        if len(openingBrackets) == 0:
            invalid = True
            break
        
        # 2. Check the last opening bracket and convert the current bracket to its corrosponding opening bracket:
        lastBracket = openingBrackets.pop()
        openingBracket = bracketConversion[bracket]
        
        # 3. If the two brackets obtained in 2. do not match we return invalid.
        if not lastBracket == openingBracket:
            invalid = True
            break

# Lastly we return invalid if we still have open brackets after iterating through all brackets (The imbalanced case).
if len(openingBrackets) > 0:
    invalid = True

# Kattis output, if the flag invalid is true output "Invalid" else output "Valid":
if invalid:
    print("Invalid")
else:
    print("Valid")
