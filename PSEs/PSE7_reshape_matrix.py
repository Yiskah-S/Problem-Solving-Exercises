# matrix = [[1,2],[3,4],[5,6],[7,8]]
# r = 2
# c = 4

# matrix = [[1,2],[3,4]]
# r = 2
# c = 4

# matrix = [[1,2],[3,4]]
# r = 1
# c = 4

matrix = [[7, 2, 1], [4, 3, 5], [6, 9, 8]]
r = 9
c = 1

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


result = reshape_matrix(matrix, r, c)
print(f"{result = }")

