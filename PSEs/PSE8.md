Kth Missing Positive Number
Problem Description
Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is not present in the array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
    The 5th missing positive integer is 9.
 Save
Example 2:

Input: arr = [1,2,3,4], k = 2
Output: 6
Explanation: The missing positive integers 
    are [5,6,7,...]. The 2nd missing
    positive integer is 6.
 Save
Sourced from: Leetcode 

Prompts
1
Ask Clarifying Questions
Submitted on Today at 1:28 PM
List three or more questions whose answers would clarify the problem statement. For each question, provide an answer which includes the effect your decision would have on how you would approach the problem.

error handling edge cases:
- empty array 
- single digit array
- array without no missing ints
- k is a negative num

What if k is larger than the array of missing positive ints?
- add ints past last int in array

Does something need to be done in case the array contains extremely large numbers?
- Ensure the method of counting the missing numbers doesn't exceed the size of K

