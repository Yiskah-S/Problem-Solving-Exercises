"""
A function which takes in a list of edges representing a graph of network nodes
and the time to travel between the nodes, the number of nodes in the network
graph, and a source node. 

The function returns the minimum amount of time to travel to all of the nodes in
the graph from the source node.

Parameters:
times (List[List[int]]): List of edges representing the time to travel between nodes in the graph.
n (int): The total number of nodes in the network graph
source (int): The source node from which to travel the network

Returns:
Int: The minimum amount of time to travel to all of the nodes in the graph.
"""

import heapq

def network_delay_time(times, n, source):
    if not is_valid_input(times, n, source):
        return False

    adj_dict = {}
    for node in range(1, n + 1):
        adj_dict[node] = []

    for node, neighbor, weight in times:
        adj_dict[node].append((neighbor, weight))

    distance = (n + 1) * [float('inf')]
    distance[source] = 0
    priority_queue = [(0, source)]
    visited = set()

    while priority_queue:
        dist, node = heapq.heappop(priority_queue)
        if node in visited:
            continue
        visited.add(node)
        for neighbor, weight in adj_dict[node]:
            if dist + weight < distance[neighbor]:
                distance[neighbor] = dist + weight
                heapq.heappush(priority_queue, (distance[neighbor], neighbor))

    max_dist = max(distance[1 :])

    return max_dist if max_dist < float('inf') else -1



def is_valid_input(times, n, source):
    if not times or n <= 0 or source <= 0 or source > n:
        raise ValueError("Invalid input: times is empty, n or source is out of range")

    for node, neighbor, edge in times:
        if not (isinstance(node, int) and isinstance(neighbor, int) and isinstance(edge, int)):
            raise ValueError("Invalid input: node, neighbor, or edge is not an integer")
        if node < 1 or node > n or neighbor < 1 or neighbor > n:
            raise ValueError("Invalid input: node or neighbor is out of valid range")
        if edge < 0:
            raise ValueError("Invalid input: edge weight is negative")

    return True




# Given a list of integers L, find the maximum length of a sequence of consecutive numbers that can be formed using elements from L.

def find_max_len_seq(arr):
    vis = [False] * len(arr)
    length = 0
    max_len = 0
    arr_set = set(arr)
    for i in range(0, len(arr)):
        if not vis[i]:
            vis[i] = True
            length += 1

            forward = arr[i] + 1
            while forward in arr_set:
                vis[forward] = True
                length += 1
                forward += 1

            backward = arr[i] - 1
            while backward in arr_set:
                vis[backward] = True
                len += 1
                backward -= 1
            max_len = max(max_len, length)
            length = 0
    return max_len

def find_max_len_seq(arr):
    arr_set = set(arr)
    max_len = 0

    for num in arr:
        if num - 1 not in arr_set:  # Start of a new sequence
            length = 1
            while num + length in arr_set:  # Extend the sequence forward
                length += 1
            max_len = max(max_len, length)

    return max_len

# Example usage:
arr = [1, 9, 3, 10, 4, 20, 2]
print("Maximum length of consecutive sequence:", find_max_len_seq(arr))


def find_max_consecutive_sequence(L):
    num_set = set(L)
    max_length = 0
    max_sequence = []

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            current_sequence = [current_num]

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                current_sequence.append(current_num)
                num_set.remove(current_num)  # Remove visited numbers from the set

            if current_length > max_length:
                max_length = current_length
                max_sequence = current_sequence

    return max_length, max_sequence

# Example usage:
L = [1, 2, 3, 6, 7, 8, 9, 10]
length, sequence = find_max_consecutive_sequence(L)
print("Maximum length of consecutive sequence:", length)
print("Numbers in the sequence:", sequence)

User
def find_max_consecutive_length(L):
    num_set = set(L)
    max_length = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_length = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
                num_set.remove(current_num)  # Remove visited numbers from the set

            max_length = max(max_length, current_length)

    return max_length

# Example usage:
L = [1, 2, 3, 6, 7, 8, 9, 10]
result = find_max_consecutive_length(L)
print("Maximum length of consecutive sequence:", result)