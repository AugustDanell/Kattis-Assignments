# Solution to the problem: https://open.kattis.com/problems/1dfroggereasy

# 1. Take in input:
n,s,m = list(map(int,input().split()))
visited = {s:True}
board = list(map(int,input().split()))
current = s
moves = 0

# 2. Play the game.
while True:

    # 3. If the current index finds the target we print, else we continue:
    if board[current-1] == m:
        print("magic")
        break
    
    # 4. Since we did not find the target we increment moves and continue. If some out of bounds check is done we print and we break.
    moves += 1
    next = current + board[current-1]
    if next < 1:
        print("left")
        break
    elif next > n:
        print("right")
        break
    elif visited.__contains__(next):
        print("cycle")
        break
    else:
        # 5. If nothing was found to break the loop we set current as next and continue the loop, as well as marking it as visited:
        current = next
        visited[next] = True

# 6. Lastly we print the amount of moves made:
print(moves)
