def square_matrix_simple(matrix=[]):
    new_mat = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]
    squ_mat = [
            [2, 2, 2],
            [2, 2, 2],
            [2, 2, 2]
            ]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_mat[i][j] = new_mat[i][j] + matrix[i][j]
            new_mat[i][j] = new_mat[i][j] ** squ_mat[i][j]

    return (new_mat)
