"""
Given the heads of two singly linked-lists `head_a` and `head_b`, 
return the node at which the two lists intersect.

Parameters:
head_a (Node): head node of list A
head_b (Node): head node of list B

Returns:
Node: the node at which list A and list B intersect, 
or None if they do not intersect.
"""

class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

# # Add first list to a set and check if any nodes from the longer list are in the set
# def intersection_node(head_a, head_b):
#     if not head_a or not head_b:
#         return None

#     # Create a set to store the nodes from the first list
#     node_set = set()

#     # Traverse the first list and store its nodes in the set
#     current_a = head_a
#     while current_a:
#         node_set.add(current_a)
#         current_a = current_a.next

#     # Traverse the second list and check if any node is in the set
#     current_b = head_b
#     while current_b:
#         if current_b in node_set:
#             return current_b
#         current_b = current_b.next

#     # If no intersection is found, return None
#     return None







# Moving the pointer of the longer list forward by the difference in length
# def intersection_node(head_a, head_b):
#     if not (head_a or head_b):
#         return None
    
#     # Find the length of list A
#     length_a = 0
#     current_a = head_a
#     while current_a:
#         length_a += 1
#         current_a = current_a.next

#     # Find the length of list B
#     length_b = 0
#     current_b = head_b
#     while current_b:
#         length_b += 1
#         current_b = current_b.next

#     # Find the difference in length between the two lists
#     length_diff = abs(length_a - length_b)

#     # Set the pointers to the heads of the two lists
#     current_a = head_a
#     current_b = head_b

#     # Move the pointer of the longer list forward by the difference in length
#     if length_a > length_b:
#         for _ in range(length_diff):
#             current_a = current_a.next
#     else:
#         for _ in range(length_diff):
#             current_b = current_b.next

#     # Move the pointers of both lists forward until they meet
#     while current_a != current_b:
#         current_a = current_a.next
#         current_b = current_b.next

#     return current_a






# Changed to move the pointers forward until they meet
def intersection_node(head_a, head_b):
    if not (head_a or head_b):
        return None
    
    # Set the pointers to the heads of the two lists
    pointer_a = head_a
    pointer_b = head_b

    # Move the pointers forward until they meet
    while pointer_a != pointer_b:
        pointer_a = pointer_a.next if pointer_a else head_b
        pointer_b = pointer_b.next if pointer_b else head_a

    return pointer_a
