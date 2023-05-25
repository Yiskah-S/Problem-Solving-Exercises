import pytest
from PSEs.PSE3_hamming import hamming_distance

def test_strands_are_same_length():
    strand1 = "GAG"
    strand2 = "GAGG"    

    try:
        hamming_distance(strand1, strand2)
    except ValueError as err:
        assert str(err) == "Strands must be of equal length."
    else:
        assert False, "Expected ValueError."

def test_valid_string_return_correct_output():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGACGGCCT"
    
    output = hamming_distance(strand1, strand2)

    assert output == 7

def test_empty_strand_raises_value_error():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = ""
    
    try:
        hamming_distance(strand1, strand2)
    except ValueError as err:
        assert str(err) == "Strands cannot be empty."
    else:
        assert False, "Expected ValueError."

def test_non_string_input_raises_value_error():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = ["C", "A", "T"]
    
    try:
        hamming_distance(strand1, strand2)
    except ValueError as err:
        assert str(err) == "Both strands must be strings."
    else:
        assert False, "Expected ValueError."

def test_hamming_distance_with_single_character_difference():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "GAGCCTACTAACGGGAA"
    
    output = hamming_distance(strand1, strand2)
    
    assert output == 1

def test_hamming_distance_with_no_difference():
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "GAGCCTACTAACGGGAT"
    
    output = hamming_distance(strand1, strand2)
    
    assert output == 0

def test_hamming_distance_with_maximum_difference():
    strand1 = "AAAAAAAAAAAAAAA"
    strand2 = "TTTTTTTTTTTTTTT"
    
    output = hamming_distance(strand1, strand2)
    
    assert output == 15
