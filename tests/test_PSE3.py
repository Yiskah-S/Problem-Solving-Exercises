import pytest
from PSEs.PSE3_hamming import hamming_distance

def test_strands_are_same_length():
    # arrange
    strand1 = "GAG"
    strand2 = "GAGG"    

    # act/assert
    try:
        hamming_distance(strand1, strand2)
    except ValueError as err:
        assert str(err) == "Strands must be of equal length."
    else:
        assert False, "Expected ValueError."

def test_valid_string_return_correct_output():
    # arrange
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGACGGCCT"
    
    # act
    output = hamming_distance(strand1, strand2)
    
    # assert
    assert output == 7