Reshape the Matrix
Problem
In MATLAB, a programming platform for numeric computing, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the number of rows and number of columns of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

Example 1:

Input: 
nums = 
[[1,2],
 [3,4]]
r = 1, c = 4

Output: 
[[1,2,3,4]]
 Save
Explanation:

The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

Example 2:

Input: 
nums = 
[[1,2],
 [3,4]]
r = 2, c = 4

Output: 
[[1,2],
 [3,4]]
 Save
Explanation:

There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

Example 3:

Input: 
nums = 
[[1,2],
 [3,4],
 [5,6],
 [7,8]]
r = 2, c = 4

Output: 
[[1,2,3,4],
 [5,6,7,8]]
 Save
Explanation:

The original matrix was 4 * 2. The new reshaped matrix is a 2 * 4 matrix, fill it row by row by using the previous list.

Note:

The height and width of the given matrix is in range [1, 100]. The given r and c are all positive.

Sourced from: Leetcode 

Prompts:
1
Ask Clarifying Questions
Submitted on Yesterday at 8:37 AM
List three or more questions whose answers would clarify the problem statement. For each question, provide an answer which includes the effect your decision would have on how you would approach the problem.

- Should new matrix be a copy or replace the original?
Doesn't specify so put in new var for now.
- What if inputs exceed the constraints given?
Throw error
- Should there be a text output when the original is returned?
Yes, letting the user know is nice so that it's clear nothing went wrong.
- What if any of the inputs are invalid?
Throw error.

Create Logical Steps
Submitted on Yesterday at 8:41 AM
Without writing code, describe how you would implement reshape_matrix in enough detail that someone else could write the code.

It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 1. Handle invalid input, 2. Given valid input, perform the computation/solve the problem/etc.
Your logical steps could take the form of a numbered list, pseudo code, or anywhere in between. What's important at this stage is to think through and outline the implementation before writing code.
check if reshaping is possible by checking if r * c is the same as len(row) * number of rows, if not return original.

else add c number of elements to new array r number of times.


(Gotta be honest I'm struggling writing pseudo on this because I'm not quite picturing how I'm going to do it, so I'm just going to write code to play with it instead.)

