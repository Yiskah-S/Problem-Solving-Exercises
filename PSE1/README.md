Highest Rated
Problem Statement
Imagine working on software that deals with restaurant reviews.

Create a function named get_highest_rated that is responsible for finding the highest-rated restaurant.

This function should take in a list of dictionaries named restaurants as a parameter. Each dictionary represents the data associated with a restaurant, including its rating. This function should have a return value of the restaurant with the highest rating.

Example Input/Output
Input (Argument of the function)
Expected Output
(Return value of the function)
Explanation
restaurants = [{"name": "Grillby's", "rating": 1}, {"name": "Crow's Nest", "rating": 5}]	{"name": "Crow's Nest", "rating": 5}	There are two restaurants: "Grillby's" and "Crow's Nest." The rating of "Grillby's" is 1, and the rating of "Crow's Nest" is 5. "Crow's Nest" has the highest rating. The return value of this function should be a dictionary, which contains the name and rating of this restaurant.
restaurants = [{"name": "Crow's Nest", "rating": 1}]	{"name": "Crow's Nest", "rating": 1}	There is one restaurant in the input. Its name is "Crow's Nest," and its rating is 1. Even though there's only one restaurant, it has the highest rating in this list! The return value of this function should be a dictionary, which contains the name and rating of "Crow's Nest."
restaurants = []	None	The input is an empty list, which means that there are zero restaurants. Because there are no restaurants at all, the output, or return value, of this function should be None.
This is a common edge case to consider. In this case, it is provided. Often, behavior for this sort of edge case will need to be clarified by you!
Prompts
1
Ask Clarifying Questions
Submitted on 03/25/2023
List three or more questions whose answers would clarify the problem statement. For each question, provide an answer which includes the effect your decision would have on how you would approach the problem.

What should the function return if there are multiple restaurants tied for the highest rating?
How should the function handle restaurant dictionaries with missing data (name or rating)?
How should the function handle restaurant dictionaries with keys in addition to "name" and "rating"?
How should the function handle non-numerical values for "rating"?
How should the function handle input that is a single dictionary (not a list)?

Create Logical Steps
Submitted on 03/25/2023
Without writing code, describe how you would implement get_highest_rating in enough detail that someone else could write the code.

It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 1. Handle invalid input, 2. Given valid input, perform the computation/solve the problem/etc.
Your logical steps could take the form of a numbered list, pseudo code, or anywhere inbetween. What's important at this stage is to think through and outline the implementation before writing code.

- get highest dict value
- if only 1 return message with highest rating
- if multiple tied, return message with highest rating
- if no valid input available return "None"