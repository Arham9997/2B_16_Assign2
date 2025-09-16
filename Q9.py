def is_identity_matrix(matrix):
    rows = len(matrix)
    for row in matrix:
        if len(row) != rows:
            return False
    for i in range(rows):
        for j in range(rows):
            if i == j and matrix[i][j] != 1:
                return False
            elif i != j and matrix[i][j] != 0:
                return False
    return True
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
print("Is identity matrix:", is_identity_matrix(matrix))
