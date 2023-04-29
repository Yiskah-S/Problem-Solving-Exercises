Palindrome
Problem Statment
Imagine working on software that processes text. A palindrome is a word, phrase, or sequence that reads the same backward as forward.

Create a function named palindrome that determines if a string is a palindrome. This method should take in one string as a parameter. This method should return True if the string is a palindrome.

Examples
Original string as parameter	Is it a palindrome?
"Hello, world!"	No
"racecar"	Yes
"noon"	Yes
"mom"	Yes
"kayak"	Yes
Prompts
1
Ask Clarifying Questions
Submitted on Last Monday at 6:56 AM
List three or more questions whose answers would clarify the problem statement. For each question, provide an answer which includes the effect your decision would have on how you would approach the problem.

- does case matter?
-> convert to same case
- how to handle punctuation marks?
-> ignore them in the comparison?
- how to handle invalid input?
-> raise input error
- numerical palindromes?
-> should handle them as well so needs to handle letters and numbers
- how to handle spaces?
-> ignore them
- how to handle lists?
-> convert to single string

Create Logical Steps
Submitted on Last Monday at 7:51 AM
Without writing code, describe how you would implement palindrome in enough detail that someone else could write the code.

It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 1. Handle invalid input, 2. Given valid input, perform the computation/solve the problem/etc.
Your logical steps could take the form of a numbered list, pseudo code, or anywhere in between. What's important at this stage is to think through and outline the implementation before writing code.
Check if input is valid 
-> if empty or dict raise value error
Convert input to a string
Remove spaces, case, and punctuation
Use index to test if backwards is same as forwards
Return True
