import pytest
from PSE1_highest_rated.PSE1 import get_highest_rated


def test_get_highest_rating_in_multiple_restaurants_list():
    # ^rename with meaningful test name
    # and complete test implementation below
    # arrange
    restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]

    # act
    result = get_highest_rated(restaurants)

    # assert
    assert result == {"name": "Crow's Nest", "rating": 5}

def test_empty_restaurants_list():
    # ^rename with meaningful test name
    # and complete test implementation below
    pass
    
    # arrange
    restaurants = []
    
    # act
    result = get_highest_rated(restaurants)
    
    # assert
    assert result == None