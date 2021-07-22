rows,cols = list(map(int,input().split()))

game_matrix = []
for i in range(rows):
    game_matrix.append(list (input()))

stone_map = {}
changes_made = True
while(changes_made):
    changes_made = False
    for i in range(rows-1, 0, -1):
        above_row = game_matrix[i-1]
        #print(i)

        for j in range(cols):
            above_element = above_row[j]
            current_element = game_matrix[i][j]

            if(current_element == "." and above_element == "V"):
                changes_made = True
                game_matrix[i][j] = "V"

            elif(current_element == "#" and above_element == "V"):
                is_right_element = (j+1 < cols)
                is_left_element = (j > 0)

                if(is_right_element and not stone_map.__contains__((i-1,j+1))):

                    if(game_matrix[i-1][j+1] == "."):
                        game_matrix[i-1][j+1] = "V"
                        stone_map[(i-1, j + 1)] = True
                        changes_made = True

                if(is_left_element and not stone_map.__contains__((i-1,j-1))):
                    if (game_matrix[i - 1][j - 1] == "."):
                        game_matrix[i-1][j-1] = "V"
                        stone_map[(i-1,j-1)] = True
                        changes_made = True

for i in range(len(game_matrix)):
    print("".join(game_matrix[i]))
