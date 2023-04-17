# A solution to the problem: https://open.kattis.com/problems/turtlemaster


def move_turtle(data, board):
    if data[2] == "right":
        if data[1] == 7:
            return "error"
        data[1] += 1

    elif data[2] == "up":
        if data[0] == 0:
            return "error"
        data[0] -= 1

    elif data[2] == "down":
        if data[0] == 7:
            return "error"
        data[0] += 1

    elif data[2] == "left":
        if data[1] == 0:
            return "error"
        data[1] -= 1

    if not board[data[0]][data[1]] in [".", "D"]:
        return "error"
def found_diamond(r,c, board):
    if board[r][c] == "D":
        return True
    return False
def rotate(current, left = True):
    directions = ["up", "right", "down", "left"]
    if left:
        return directions[(directions.index(current)-1)%4]
    else:
        return directions[(directions.index(current)+1)%4]
def fire_laser(r,c, direction, board):
    if (direction == "right"):
        if c == 7 or not board[r][c+1] == "I":
            return "error"
        else:
            board[r][c+1] = "."

    elif (direction == "left"):
        if c == 0 or not board[r][c-1] == "I":
            return "error"
        else:
            board[r][c-1] = "."

    elif (direction == "up"):
        if r == 0 or not board[r-1][c] == "I":
            return "error"
        else:
            board[r-1][c] = "."

    elif (direction == "down"):
        if r == 7 or not board[r+1][c] == "I":
            return "error"
        else:
            board[r+1][c] = "."

if __name__ == "__main__":
    board = []
    turtle = [7, 0, "right"]
    for _ in range(8):
        row = list(input())
        board.append(row)
    operations = list(input())
    diamond = True

    for op in operations:
        response = None

        if(op == "F"):
            response = move_turtle(turtle, board)
        elif(op == "R"):
            turtle[2] = rotate(turtle[2], False)
        elif(op == "L"):
            turtle[2] = rotate(turtle[2])
        elif(op == "X"):
            response = fire_laser(turtle[0], turtle[1], turtle[2], board)

        if response == "error":
            diamond = False
            break

    if (diamond) and found_diamond(turtle[0], turtle[1], board):
        print("Diamond!")
    else:
        print("Bug!")
