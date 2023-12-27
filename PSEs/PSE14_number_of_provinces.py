"""
A function that takes in an adjacency list representing a graph of
cities, and returns the total number of provinces represented by
the graph.

Parameters:
is_connected (2D matrix of integers): An adjacency matrix
    representing a graph of cities and their connections. The value
    at is_connected[i][j] is 1 if cities i and j are connected, and
    0 otherwise.

Returns:
Integer: The total number of provinces represented by the graph.
"""

# Edge cases:
def is_valid_matrix(is_connected):
    if not is_connected:
        return False
    
    num_rows = len(is_connected)

    for row in is_connected:
        if len(row) != num_rows:
            return False
        for num in row:
            if num != 0 and num != 1:
                return False
    return True


# Recursive solution
def num_provinces(is_connected):
    if not is_valid_matrix(is_connected):
        return False

    visited = set()
    provinces = 0

    for node in range(len(is_connected)):
        if node in visited:
            continue
        else:
            dfs(node, visited, is_connected)
            provinces += 1

    return provinces

def dfs(node, visited, is_connected):
    visited.add(node)
    for neighbor in range(node + 1, len(is_connected)):
        if is_connected[node][neighbor] == 1 and neighbor not in visited:
            dfs(neighbor, visited, is_connected)



# Iterative solution
def num_provinces(is_connected):
    if not is_valid_matrix(is_connected):
        return False

    visited = set()
    provinces = 0

    for node in range(len(is_connected)):
        if node in visited:
            continue
        else:
            stack = [node]
            while stack:
                current_node = stack.pop()
                visited.add(current_node)
                for neighbor in range(current_node + 1, len(is_connected)):
                    if is_connected[current_node][neighbor] == 1:
                        stack.append(neighbor)
            provinces += 1

    return provinces