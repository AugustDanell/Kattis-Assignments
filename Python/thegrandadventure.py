# Solution to: https://open.kattis.com/problems/thegrandadventure

if __name__ == "__main__":
    
    # 1. Input, and iterate over every item:
    n = int(input())
    for _ in range(n):
        stack = []
        adventure = list(input())
        impossible = False
        for i in adventure:
            if i in ["$", "|", "*"]:
                stack.append(i)

            elif i == ".":
                continue

            # 2. Cases for failing the quest:
            elif i in ["t", "j", "b"] and len(stack) == 0:
                impossible = True
                break
            elif i == "t" and not stack[len(stack)-1] == "|":
                impossible = True
                break
            elif i == "b" and not stack[len(stack)-1] == "$":
                impossible = True
                break
            elif i == "j" and not stack[len(stack)-1] == "*":
                impossible = True
                break

            else:
                stack.pop()
        
        # 3. If the quest is failed already or if he stil has things in the stack, fail. Else succeed:
        if impossible or len(stack) > 0:
            print("NO")
        else:
            print("YES")
