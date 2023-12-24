import pytest
from PSEs.PSE13_array_to_BST import TreeNode, arr_to_bst

# Below are functions used to test if the given tree is a balanced Binary Search Tree.
# Returns True if the BST provided is a valid BST.
def is_bst(root):
    if root is None:
        return True

    left = root.left
    if left is not None and root.val <= left.val:
        return False

    right = root.right
    if right is not None and root.val >= right.val:
        return False

    return is_bst(left) and is_bst(right)


# Returns the height of a tree
def height(root):
    if root is None:
        return 0
    
    left_height = height(root.left)
    right_height = height(root.right)

    if left_height > right_height:
        return left_height + 1
    else:
        return right_height + 1


# Returns True if a tree is balanced
def is_balanced_tree(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    left_check = is_balanced_tree(root.left)
    right_check = is_balanced_tree(root.right)

    return left_check and right_check


def test_will_return_balanced_bst_for_odd_lengthed_list():
        # Arrange
        arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]

        # Act
        result = arr_to_bst(arr)

        # Assert
        assert result.val == 25
        assert is_bst(result)
        assert is_balanced_tree(result)


def test_will_return_balanced_bst_for_even_lengthed_list():
    # Arrange
    arr = [10, 20, 30, 40, 50, 60]

    # Act
    result = arr_to_bst(arr)

    # Assert
    assert result.val == 30 or result.val == 40  # Since it's even, the root could be 30 or 40
    assert is_bst(result)
    assert is_balanced_tree(result)


def test_will_return_none_for_empty_list():
        # Arrange
        arr = []

        # Act
        result = arr_to_bst(arr)

        # Assert
        assert result is None


def test_will_return_correct_bst_for_single_element_list():
    # Arrange
    arr = [25]

    # Act
    result = arr_to_bst(arr)

    # Assert
    assert result.val == 25
    assert result.left is None
    assert result.right is None
    assert is_bst(result)
    assert is_balanced_tree(result)


def test_will_return_balanced_bst_for_long_list():
    # Arrange
    arr = list(range(100))

    # Act
    result = arr_to_bst(arr)

    # Assert
    assert is_bst(result)
    assert is_balanced_tree(result)

