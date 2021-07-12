lines, columns, classes = map(int, input().split())

matrix = []
assigned_colors = {}
for i in range(lines):
    matrix.append(input())

combos = 0
for i in range(columns):
    adding_colors = True
    adding_list = []
    for j in range(lines):

        letter = matrix[j][i]
        if(assigned_colors.__contains__(letter)):
            adding_colors = False
        else:
            adding_list.append(letter)

    for x in adding_list:
        assigned_colors[x] = True

    if(adding_colors):
        combos += 1



print(combos)
