def reshape_matrix(matrix, r, c):
    if r * c != len(matrix) * len(matrix[0]):
        return matrix
    
    one_list = []
    for row in matrix:
        for column in row:
            one_list.append(column)

    new_matrix = [c * [0] for _ in range(r)]
    for i in range(r):
        for j in range(c):
            new_matrix[i][j] = one_list.pop(0)
            
    return new_matrix

def reshape_matrix(matrix, r, c):
    one_list = [column for row in matrix for column in row]

    if r * c != len(one_list):
        return matrix

    return [[one_list.pop(0) for _ in range(c)] for _ in range(r)]

