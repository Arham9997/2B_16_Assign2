def is_sparse_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    total_elements = rows * cols
    zero_count = 0
    for row in matrix:
        zero_count += row.count(0)
    if zero_count > total_elements/2:
        return True
    else:
        return False
matrix = [
    [0, 0, 3],
    [0, 0, 0],
    [7, 0, 0]
]
if is_sparse_matrix(matrix):
    print("The matrix is sparse.")
else:
    print("The matrix is not sparse.")
