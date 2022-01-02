def nullify_row(matrix, row):
    for i in range(len(matrix[0])):
        matrix[row][i] = 0
    return matrix


def nullify_col(matrix, col):
    for i in range(len(matrix)):
        matrix[i][col] = 0
    return matrix


def set_zeros(matrix):
    row = [False] * len(matrix)
    col = [False] * len(matrix[0])
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True

    for i in range(len(matrix)):
        if row[i]:
            nullify_row(matrix, i)

    for i in range(len(matrix[0])):
        if col[i]:
            nullify_col(matrix, i)
    return matrix


def set_zeros2(matrix):
    first_row_has_zero = False
    first_col_has_zero = False
    for i in range(len(matrix)):
        if matrix[i][0] == 0:
            first_col_has_zero = True
            break
    for i in range(len(matrix[0])):
        if matrix[0][i] == 0:
            first_row_has_zero = True
            break
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[0][i] = 0
                matrix[j][0] = 0
    for i in range(1, len(matrix)):
        if matrix[i][0] == 0:
            nullify_row(matrix, i)
    for i in range(1, len(matrix[0])):
        if matrix[0][i] == 0:
            nullify_col(matrix, i)
    if first_row_has_zero:
        nullify_row(matrix, 0)
    if first_col_has_zero:
        nullify_col(matrix, 0)


matrix = [[1, 2, 3, 4, 0],
          [5, 6, 7, 8, 9],
          [10, 0, 12, 13, 14],
          [15, 16, 17, 18, 19]]
set_zeros(matrix)
print(matrix)
