# def get_highest_rated(restaurants):
#     if not restaurants:
#         return None
#     rated_restaurants = []
#     for restaurant in restaurants:
#         if 'rating' in restaurant:
#             rated_restaurants.append(restaurant)

#     if not rated_restaurants:
#         return None
    
#     highest_rated = []
#     max_score = max(rated_restaurants, key=lambda restaurant: restaurant['rating'])
#     highest_rated = [restaurant for restaurant in rated_restaurants if restaurant['rating'] == max_score['rating']]
    
#     if len(highest_rated) == 1:
#         return highest_rated[0]
#     elif len(highest_rated) > 1:
#         # In case of a tie, return all highest-rated restaurants
#         return highest_rated
#     else:
#         return None