"""
A function to create a balanced Binary Search Tree from the contents of an array.

Parameters:
arr (list[int]): A list of sorted integers

Returns:
TreeNode: The root of the Binary Search Tree created from the given array, arr.
"""

from collections import deque
from typing import List
from queue import Queue

class TreeNode:
    def __init__(self, value=0, left = None, right = None):
        self.val = value
        self.left = left
        self.right = right

# Recursive approach
def arr_to_bst(arr):
    if not arr:
        return None
    
    if len(arr) == 1:
        return TreeNode(arr[0])

    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    
    root.left = arr_to_bst(arr[: mid])
    root.right = arr_to_bst(arr[mid + 1 :])

    return root 

# Iterative approach deque version
def arr_to_bst(arr):
    if not arr:
        return None
    
    if len(arr) == 1:
        return TreeNode(arr[0])

    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    queue = deque([(root, (0, mid - 1)), (root, (mid + 1, len(arr) - 1))])
    
    while queue:
        current = queue.popleft()
        parent = current[0]
        left = current[1][0]
        right = current[1][1]

        if left <= right and parent is not None:
            mid = (left + right) // 2
            child = TreeNode(arr[mid])
            
            queue.append((child.left, (left, mid - 1)))

            if right > left and parent is not None:
                mid = mid + 1
                child.right = TreeNode(arr[mid])
                queue.append((child.right, (mid + 1, right)))
    return root

# Iterative approach Queue version
def arr_to_bst(arr):
    if not arr:
        return None

    if len(arr) == 1:
        return TreeNode(arr[0])
    
    mid = len(arr) // 2
    root = TreeNode(arr[mid])
    queue = Queue([(root, (0, mid - 1)), (root, (mid + 1, len(arr) - 1))])

    while not queue.empty():
        current = queue.get()
        parent = current[0]
        left = current[1][0]
        right = current[1][1]

        if left <= right and parent is not None:
            mid = (left + right) // 2
            child = TreeNode(arr[mid])

            if arr[mid] < parent.val:
                parent.left = child
            else:
                parent.right = child

            queue.put((child, (left, mid - 1)))
            queue.put((child, (mid + 1, right)))

    return root