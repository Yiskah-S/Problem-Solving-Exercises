Hamming
Problem Statment
Imagine working on software that analyzes mutations in DNA.

Create a function named hamming_distance that calculates the number of differences between two DNA strands (aka two strings). This method should take in two different DNA strands of the same length as parameters. This method should have a return value of the number of differences between each string.

For example, given these two DNA strands (strings), hamming_distance should return 7 because there are 7 differences:

Example Input	Expected Ouput
strand1 = "GAGCCTACTAACGGGAT"
strand2 = "CATCGTAATGACGGCCT"	7
Explanation:

Strand #1:   GAGCCTACTAACGGGAT
Strand #2:   CATCGTAATGACGGCCT
Differences: ^ ^ ^  ^ ^    ^^
             7 in total
 Save
(This problem is sourced from http://rosalind.info/problems/hamm/  )

Prompts
1
Ask Clarifying Questions
Submitted on 04/17/2023
List three or more questions whose answers would clarify the problem statement. For each question, provide an answer which includes the effect your decision would have on how you would approach the problem.

- If strands empty:
raise ValueError
- If strands not equal length:
raise ValueError
- If strand is not a string:
raise ValueError

Create Logical Steps
Submitted on 04/17/2023
Without writing code, describe how you would implement hamming_distance in enough detail that someone else could write the code.

It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 1. Handle invalid input, 2. Given valid input, perform the computation/solve the problem/etc.
Your logical steps could take the form of a numbered list, pseudo code, or anywhere in between. What's important at this stage is to think through and outline the implementation before writing code.

- check if strands are strings if not raise ValueError
- check if strands are empty if not raise ValueError
- check if strands are same length if not raise ValueError
- implement a counter
- make loop counting over each character in strand1
- check if index in strand1 == index in strand2
- increase counter if True
- return counter