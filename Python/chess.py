# 664th Kattis. A solution to the problem: https://open.kattis.com/problems/chess

# General solution: Very simple. See if target has an intersectional diagonal, a direct diagonal, or if target == start.
# Worst case (intersection) output that intersection. Else just output the direct path. Every square of same color is reached in 2 moves so if they have
# no intersectionality then just output: impossible. 

def get_intersection(l1, l2):
    for item in l1:
        if item in l2:
            return item
    return -1

def ascii_to_num(c):
    return ord(c)-64
def num_to_ascii(n):
    return chr(n+64)
def get_diagonal(pos):
    moves = []
    for stepsize in range(1,8):
        x,y = pos
        if x+stepsize <= 8 and y+stepsize <= 8:
            next_move = [x+stepsize, y+stepsize]
            moves.append(next_move)
        if x+stepsize <= 8 and y-stepsize >= 1:
            next_move = [x+stepsize, y-stepsize]
            moves.append(next_move)
        if x-stepsize >= 1 and y + stepsize <= 8:
            next_move = [x-stepsize, y + stepsize]
            moves.append(next_move)
        if x-stepsize >= 1 and y - stepsize <= 8:
            next_move = [x-stepsize, y-stepsize]
            moves.append(next_move)
    return moves

n = int(input())
for _ in range(n):
    line = input().split()
    start =  [ascii_to_num(line[0]), int(line[1])]
    target = [ascii_to_num(line[2]), int(line[3])]
    start_diagonal  = get_diagonal(start)
    target_diagonal = get_diagonal(target)
    intersection = get_intersection(start_diagonal, target_diagonal)
    #print(intersection)

    if target == start:
        print(0, line[0], line[1])
    elif target in start_diagonal:
        print(1, line[0], line[1], line[2], line[3])
    elif not intersection == -1:
        print(2, line[0], line[1], num_to_ascii(intersection[0]), (intersection[1]), line[2], line[3])
    else:
        print("Impossible")
