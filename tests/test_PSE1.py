import pytest
from PSEs.PSE1_highest_rated import get_highest_rated


def test_get_highest_rating_in_multiple_restaurants_list():
    restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]
    result = get_highest_rated(restaurants)
    assert result == {"name": "Crow's Nest", "rating": 5}

def test_empty_restaurants_list():
    restaurants = []
    result = get_highest_rated(restaurants)
    assert result == None

def test_get_highest_rating_in_empty_list():
    restaurants = []
    result = get_highest_rated(restaurants)
    assert result == None

def test_get_highest_rating_in_unrated_restaurants_list():
    restaurants = [
        {"name": "Burger Joint"},
        {"name": "Pizza Place"},
        {"name": "Sushi Bar"}
    ]
    result = get_highest_rated(restaurants)
    assert result == None

def test_get_highest_rating_in_single_restaurant_list():
    restaurants = [{"name": "Taco Shack", "rating": 4.5}]
    result = get_highest_rated(restaurants)
    assert result == {"name": "Taco Shack", "rating": 4.5}

def test_get_highest_rating_in_multiple_restaurants_list_with_ties():
    restaurants = [
        {"name": "Burger Joint", "rating": 3.8},
        {"name": "Pizza Place", "rating": 4.2},
        {"name": "Sushi Bar", "rating": 4.2},
        {"name": "Mexican Grill", "rating": 3.9},
        {"name": "Steakhouse", "rating": 4.1},
    ]
    result = get_highest_rated(restaurants)
    assert result == [
        {"name": "Pizza Place", "rating": 4.2},
        {"name": "Sushi Bar", "rating": 4.2}
    ]

def test_get_highest_rating_with_missing_rating_key():
    restaurants = [
        {"name": "Burger Joint", "rating": 4.1},
        {"name": "Pizza Place"},
        {"name": "Sushi Bar", "rating": 3.9},
        {"name": "Mexican Grill"},
        {"name": "Steakhouse", "rating": 4.0},
    ]
    result = get_highest_rated(restaurants)
    assert result == {"name": "Burger Joint", "rating": 4.1}
