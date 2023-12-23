import pytest
from PSEs.PSE12_linked_list_intersection import intersection_node, Node

def test_will_return_intersection_for_lists_of_same_length():
    # Arrange
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    node_x = Node("X")
    node_y = Node("Y")
    node_z = Node("Z")

    node_one = Node("1")
    node_two = Node("2")
    node_three = Node("3")
    node_one.next = node_two
    node_two.next = node_three

    # List A: ["D", "E", "F", "1", "2", "3"]
    node_d.next = node_e
    node_e.next = node_f
    node_f.next = node_one

    # List B: ["X", "Y", "Z", "1", "2", "3"]
    node_x.next = node_y
    node_y.next = node_z
    node_z.next = node_one

    head_a = node_d
    head_b = node_x

    # Act
    answer = intersection_node(head_a, head_b)

    # Assert
    assert answer == node_one

def test_will_return_intersection_with_lists_of_differing_lengths_a_is_longest():
    # Arrange
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    node_x = Node("X")

    node_one = Node("1")
    node_two = Node("2")
    node_three = Node("3")
    node_one.next = node_two
    node_two.next = node_three

    # List A: ["D", "E", "F", "1", "2", "3"]
    node_d.next = node_e
    node_e.next = node_f
    node_f.next = node_one

    # List B: ["X", "1", "2", "3"]
    node_x.next = node_one

    head_a = node_d
    head_b = node_x

    # Act
    answer = intersection_node(head_a, head_b)

    # Assert
    assert answer == node_one

def test_will_return_intersection_with_lists_of_differing_lengths_b_is_longest():
    # Arrange
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    node_x = Node("X")

    node_one = Node("1")
    node_two = Node("2")
    node_three = Node("3")
    node_one.next = node_two
    node_two.next = node_three

    # List A: ["X", "1", "2", "3"]
    node_x.next = node_one

    # List B: ["D", "E", "F", "1", "2", "3"]
    node_d.next = node_e
    node_e.next = node_f
    node_f.next = node_one


    head_a = node_x
    head_b = node_d

    # Act
    answer = intersection_node(head_a, head_b)

    # Assert
    assert answer == node_one

def test_will_return_none_with_one_empty_list():
    # Arrange
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    # List A: ["D", "E", "F"]
    node_d.next = node_e
    node_e.next = node_f

    # List B: [] <-- empty list

    # Act
    answer = intersection_node(node_d, None)

    # Assert
    assert answer is None

def test_will_return_none_when_no_intersection():
    # Arrange
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    node_x = Node("X")
    node_y = Node("Y")
    node_z = Node("Z")

    # List A: ["D", "E", "F"]
    node_d.next = node_e
    node_e.next = node_f

    # List B: ["X", "Y", "Z"]
    node_x.next = node_y
    node_y.next = node_z

    head_a = node_d
    head_b = node_x

    # Act
    answer = intersection_node(head_a, head_b)

    # Assert
    assert answer is None

def test_will_return_none_for_two_empty_lists():
    # Arrange

    # List A: [] <-- empty list
    # List B: [] <-- empty list

    # Act
    answer = intersection_node(None, None)

    # Assert
    assert answer is None

def test_will_return_none_for_tails_with_same_values_but_different_memory_location():
    # Arrange
    node_d = Node("D")
    node_e1 = Node("E")
    node_f1 = Node("F")

    node_x = Node("X")
    node_e2 = Node("E")
    node_f2 = Node("F")

    # List A: ["D", "E", "F"]
    node_d.next = node_e1
    node_e1.next = node_f1

    # List B:
    node_x.next = node_e2
    node_e2.next = node_f2

    # Act
    answer = intersection_node(node_d, node_x)

    # Assert
    assert answer is None

def test_will_return_intersection_for_tails_with_same_values_and_same_memory_location():
    # Arrange
    node_d = Node("D")
    node_e = Node("E")
    node_f = Node("F")

    # List A: ["D", "E", "F"]
    node_d.next = node_e
    node_e.next = node_f

    # List B: ["D", "E", "F"]
    node_x = node_d
    node_y = node_e
    node_z = node_f

    # Act
    answer = intersection_node(node_d, node_x)

    # Assert
    assert answer == node_d
