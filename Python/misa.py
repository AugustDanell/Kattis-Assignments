# A solution to the problem: https://open.kattis.com/problems/misa
# Handshake Lemma: The amount of handshakes will be (degree of all nodes) / 2.

if __name__ == "__main__":
    grid = []
    row,col = list(map(int,input().split()))
    for _ in range(row):
        grid.append(list(input()))

    handshakes = 0
    best_mirko = 0
    for row_number in range(row):
        for col_number in range(col):
            local_handshakes = 0
            for x_neighbour in [row_number-1, row_number, row_number+1]:
                for y_neighbour in [col_number-1, col_number, col_number+1]:
                    if x_neighbour == row_number and y_neighbour == col_number:
                        continue
                    elif x_neighbour < 0 or x_neighbour >= row:
                        continue
                    elif y_neighbour < 0 or y_neighbour >= col:
                        continue
                    elif grid[x_neighbour][y_neighbour] == "o":
                        local_handshakes += 1

            if grid[row_number][col_number] == "o":
                handshakes += local_handshakes
            elif grid[row_number][col_number] == "." and local_handshakes > best_mirko:
                best_mirko = local_handshakes


    print(handshakes//2 + best_mirko)
