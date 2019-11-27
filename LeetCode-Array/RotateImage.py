
def rotateImage(matrix):

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    for row in matrix:
        row.reverse()

    return matrix
