# A solution to the problem: https://open.kattis.com/problems/glitchbot

''' Solution:
    Write a function that executes every operation. Then change the list of operations, changing every item to any other operation, and iterate through the list.
    This solution is O(n^2), not too bad. The problem instance is small so it works no problem. 
'''

def left(deg):
    return (deg-90)%360
def right(deg):
    return (deg+90)%360

def move(coordinates, deg):
    if deg == 0:
        coordinates[1] += 1
    elif deg == 90:
        coordinates[0] += 1
    elif(deg == 180):
        coordinates[1] -= 1
    else:
        coordinates[0] -= 1
def execute_operations(op_list):
    person = [0, 0]
    degrees = 0
    for operation in op_list:
        if operation == "Forward":
            move(person, degrees)
        elif operation == "Left":
            degrees = left(degrees)
        elif operation == "Right":
            degrees = right(degrees)
    return person

def brute_force(op_list, target):
    for i in range(len(op_list)):
        temp = op_list[i]
        for op in ["Forward", "Right", "Left"]:
            op_list[i] = op
            x,y = execute_operations(op_list)
            if target[0] == x and target[1] == y:
                print((i+1), op)
                return
        op_list[i] = temp

if __name__ == "__main__":
    target_x, target_y = list(map(int,input().split()))
    target = [target_x, target_y]
    n = int(input())
    operations = []
    for _ in range(n):
        operations.append(input())
    brute_force(operations, target)
