# Good Morning
# Lets start with generating possible numbers. We can construct the problem as a graph. Each node can go up and down
# and to itself. We can also carry a digit sum and when that digit sum is less than 2 we do a recrusive call.

# For example, we start with no number at all. From there we have to go to 1 so node = 1 is entered by start.
# From node = 1 we can go to 2 and 4 (optionally entering them in) or we can enter in another 1. 
# From node = 2 we can go to 3 and 5 (again optionally entering them in), or enteri ing 2 again.
# From node = 3 we can only go down to 6 (optionally entering it in) or repeat 3.
# ... Etc. 

def generate_numbers(node, l, acc):
    if (not l.__contains__(acc)):
        l.append(acc)
    
    # Base Case:
    if(len(acc) == 3):
        return

    if(node == 1):
        generate_numbers(2, l, acc)
        generate_numbers(4, l, acc)

        acc += "1"
        generate_numbers(1, l, acc)
        generate_numbers(2, l, acc)
        generate_numbers(4, l, acc)

    if(node == 2):
        generate_numbers(3, l, acc)
        generate_numbers(5, l, acc)

        acc += "2"
        generate_numbers(2, l, acc)
        generate_numbers(3, l, acc)
        generate_numbers(5, l, acc)

    if(node == 3):
        generate_numbers(6, l, acc)

        acc += "3"
        generate_numbers(3, l, acc)
        generate_numbers(6, l, acc)

    if(node == 4):
        generate_numbers(5, l, acc)
        generate_numbers(7, l, acc)

        acc += "4"
        generate_numbers(4, l, acc)
        generate_numbers(5, l, acc)
        generate_numbers(7, l, acc)

    if(node == 5):
        generate_numbers(6, l, acc)
        generate_numbers(8, l, acc)

        acc += "5"
        generate_numbers(5, l, acc)
        generate_numbers(6, l, acc)
        generate_numbers(8, l, acc)

    if(node == 6):
        generate_numbers(9, l, acc)
        acc += "6"
        generate_numbers(6, l, acc)
        generate_numbers(9, l, acc)

    if(node == 7):
        generate_numbers(8, l, acc)
        acc += "7"
        generate_numbers(7, l, acc)
        generate_numbers(8, l, acc)

    if(node == 8):
        generate_numbers(9, l, acc)
        generate_numbers(0, l, acc)
        acc += "8"
        generate_numbers(8, l, acc)
        generate_numbers(9, l, acc)
        generate_numbers(0, l, acc)

    if(node == 9):
        acc += "9"
        generate_numbers(9, l, acc)

    if(node == 0):
        acc += "0"
        generate_numbers(0, l, acc)

l = []
generate_numbers(1, l, "")
l.pop(0) # Pop so we can safely cast every item to an int. 
m = list(map(int, l))
m.sort()
#print(m)

test_cases = int(input())
for i in range(test_cases):
    code = int(input())

    for j in range(len(m)):
        if(code == m[j]):
            print(code)
        elif(j + 1 < len(m) and m[j] < code and m[j+1] > code):
            if(code - m[j] <= m[j+1] - code):
                print(m[j])
            else:
                print(m[j+1])
