Problem
Imagine working on software that processes lists of numbers. Create a function named merge_lists that takes two sorted lists and merges them into a single sorted list. This function should take in two lists of whole numbers. The function should return a new sorted list which consists of the elements of the two arguments.

List 1	List 2	Output
[1, 2, 4, 5]	[6]	[1, 2, 4, 5, 6]
[-30, -10, 0, 15, 16]	[-20, -5, 5]	[-30, -20, -10, -5, 0, 5, 15, 16]
Sourced from: Leetcode 

Prompts
1
Ask Clarifying Questions
List three or more questions whose answers would clarify the problem statement. For each question, provide an answer which includes the effect your decision would have on how you would approach the problem.


- input empty -> raise error
- duplicate numbers in list? -> merge only once using set?
- modify one of the input lists or create a new results one? -> create new list
- how to handle non-numerical items in list? -> raise error
- what if one list is empty? -> return other one sorted
- what if both of them are empty? -> raise error


Without writing code, describe how you would implement merge_lists in enough detail that someone else could write the code.

It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 1. Handle invalid input, 2. Given valid input, perform the computation/solve the problem/etc.
Your logical steps could take the form of a numbered list, pseudo code, or anywhere in between. What's important at this stage is to think through and outline the implementation before writing code.
if both lists empty, raise error
if list1 empty, return list2
if list 2 empty, return list 1

elif if 0 index of list1 > than 0 index of lists
return 0 index of list 1 + a recursive call of the merge function for all other positions
else return 0 index of list 2 + recursive call of the merge function for all other positions
if both lists empty, raise error
if list1 empty, return list2
if list 2 empty, return list 1

elif if 0 index of list1 > than 0 index of lists
return 0 index of list 1 + a recursive call of the merge function for all other positions
else return 0 index of list 2 + recursive call of the merge function for all other positions​
