# A solution to the matrix problem: https://open.kattis.com/problems/tajna

def run_tests():
    assert get_dimensions("bok") == [1,3]
    assert get_dimensions("koaski") == [2,3]
    assert get_dimensions("boudonuimilcbsai") == [4,4]

def get_dimensions(word):
    rows = 1
    cols = len(word)
    new_rows = 1
    while True:
        new_rows += 1
        if len(word) % new_rows == 0:
            if new_rows > len(word) // new_rows:
                break
            else:
                rows = new_rows
                cols = len(word) // new_rows
    return [rows,cols]
  
def get_col_matrix(word, dimensions):
    matrix = []
    for r in range(dimensions[0]):
        row = []
        for c in range(dimensions[1]):
            index = c*dimensions[0] + r
            row.append(word[index])
        matrix.append(row)
    return(matrix)

if __name__ == "__main__":
    run_tests()
    word = list(input())
    dimensions = get_dimensions(word)
    matrix = get_col_matrix(word, dimensions)

    s = ""
    for row in matrix:
        for letter in row:
            s += letter
    print(s)
