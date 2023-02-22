def convertToLand(i, j, matrix, visited):
    if not matrix[i][j] == "L" or (visited[i])[j]:
        return
    else:
        (visited[i])[j] = True
        if not i == 0 and not matrix[i-1][j] == "W":
            matrix[i-1][j] = "L"
            convertToLand(i-1, j, matrix, visited)

        if not i == len(matrix)-1 and not matrix[i+1][j] == "W":
            matrix[i+1][j] = "L"
            convertToLand(i+1, j, matrix, visited)

        if not j == 0 and not matrix[i][j-1] == "W":
            matrix[i][j-1] = "L"
            convertToLand(i, j-1, matrix, visited)

        if not j == len(matrix[0])-1 and not matrix[i][j+1] == "W":
            matrix[i][j+1] = "L"
            convertToLand(i, j+1, matrix, visited)

def recCount(i, j, matrix, visited):
    pass

def countIslands(i, j, matrix, visited):
    if visited[i][j] or not matrix[i][j] == "L":
        return 0
    else:
        visited[i][j] = True
        if not i == 0:
            countIslands(i-1, j, matrix, visited)

        if not i == len(matrix) - 1:
            countIslands(i+1, j, matrix, visited)

        if not j == 0:
            countIslands(i, j-1, matrix, visited)

        if not j == len(matrix[0]) -1:
            countIslands(i, j+1, matrix, visited)

        return 1

# 1. Input
rows, cols = list(map(int, input().split()))
matrix = []
clouds = 0
visitedConvert = []
visitedCount = []
for i in range(rows):
    row = list(input())
    matrix.append(row)
    convertRow = []
    countRow = []
    for j in range(cols):
        convertRow.append(False)
        countRow.append(False)
    visitedConvert.append(convertRow)
    visitedCount.append(countRow)

# 2. First we convert C into L/W:
for i in range(rows):
    for j in range(cols):
        convertToLand(i, j, matrix, visitedConvert)

# 3. Now we count the islands:
islands = 0
for i in range(rows):
    for j in range(cols):
        islands += countIslands(i, j, matrix, visitedCount)

#print(matrix)
print(islands)
