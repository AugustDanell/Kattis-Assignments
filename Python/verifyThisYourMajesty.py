def check(N, L, reverse = 0):
    rows = {}
    cols = {}
    dia_sums = {}
    positions = []
    correct = True
    for i in range(N):

        if(reverse == 0):
            position = list(map(int, input().split()))
        else:
            position = L[i]

        positions.append(position)
        row = position[0]
        col = position[1]

        if reverse == 1:
            temp = row
            row = N - 1 - col
            col = temp

        dia_sum = row - col

        if(rows.__contains__(row)):
            correct = False
            break

        if(cols.__contains__(col)):
            correct = False
            break

        if(dia_sums.__contains__(dia_sum)):
            correct = False
            break

        rows[row] = True
        cols[col] = True
        dia_sums[dia_sum] = True

    return positions, correct

N = int(input())


# Check for the order i = 1 ... N and then rotate:
pos, corr = check(N, [])
if(corr):
    pos, corr = check(N, pos, 1)

if(corr):
    print('CORRECT')
else:
    print('INCORRECT')
