Adagrams
Problem Statement
Imagine programming the logic for a word game.

In this game, every player submits one word. Each word gets a score based on the letters in the word and its point value.

Create a function named score that is responsible for scoring a given word.

This function should take in a string named word as a parameter. This function should return the word's total number of points.

Refer to this table for the point values of each letter.

Letter	Value
A, E, I, O, U, L, N, R, S, T	1
D, G	2
B, C, M, P	3
F, H, V, W, Y	4
K	5
J, X	8
Q, Z	10
Examples
Input	Expected Output
"DOG"	5
"CAT"	5
"CABBAGE"	14
"QUARTZ" 	24
Prompts
1
Ask Clarifying Questions
Submitted on 04/02/2023
List three or more questions whose answers would clarify the problem statement. For each question, provide an answer which includes the effect your decision would have on how you would approach the problem.

- Do we need to verify case? With which method? Test for this.

- Empty word string returns 0. Verify with test.

- Duplicate letters return the correct score. Verify with test.

Create Logical Steps
Submitted on 04/02/2023
Without writing code, describe how you would implement score in enough detail that someone else could write the code.

It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 1. Handle invalid input, 2. Given valid input, perform the computation/solve the problem/etc.
Your logical steps could take the form of a numbered list, pseudo code, or anywhere in between. What's important at this stage is to think through and outline the implementation before writing code.

Make a dict where each key is a letter and each value the score.

Make a var to hold the value

Write a loop so that for each letter in the word we look up the corresponding score value in the dict and add it to the value var.

Return the value var