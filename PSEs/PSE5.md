Pairs With a Given Sum
Problem
Imagine working on software that processes lists of numbers. Create a function named pairs_with_given_sum It finds the number of pairs of numbers in a list which add up to a given target. This function should take in a list of whole numbers and a target as parameters. This function should have a return value of the integer of number of pairs.

numbers	target	Number of pairs (return value)
[1, 2, 4, 5]	6	2
[97, 51, 49, 35, 3, 65]	100	3
Sourced from: Geeks for Geeks 

Prompts
1
Ask Clarifying Questions
Submitted on Today at 4:42 PM
List three or more questions whose answers would clarify the problem statement. For each question, provide an answer which includes the effect your decision would have on how you would approach the problem.

- Does list/target contain negative numbers? 
  Assume yes and write code to handle negative numbers appropriately
- Does list/target contain floats?
  Assume yes and round to 2 decimal places
- Is the list sorted?
  Assume no, convert list to dict for faster referencing
- Return in case of empty?
  Raise error
- What if target is not a number?
  Raise error
- What if item in list is not a number?
  Ignore if there are numbers, otherwise raise an error saying no valid input
- Does list/target contain negative numbers? 
  Assume yes and write code to handle negative numbers appropriately
- Does list/target contain floats?
  Assume yes and round to 2 decimal places
- Is the list sorted?
  Assume no, convert list to dict for faster referencing
- Return in case of empty?
  Raise error
- What if target is not a number?
  Raise error
- What if item in list is not a number?
  Ignore if there are numbers, otherwise raise an error saying no valid input​
- Assume numbers can't be reused because otherwise the list would be a set


Create Logical Steps
Without writing code, describe how you would implement pairs_with_given_sum in enough detail that someone else could write the code.

It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 1. Handle invalid input, 2. Given valid input, perform the computation/solve the problem/etc.
Your logical steps could take the form of a numbered list, pseudo code, or anywhere in between. What's important at this stage is to think through and outline the implementation before writing code.

- Check if target is number -> raise type error
- Check if list is empty -> raise value error
- check if list contains numbers - raise value error

Loop over list and for each 
- find it's complement by subtracting it from the target
- add to dict
- look up if complement is in dict
- if yes add to count 
- return count