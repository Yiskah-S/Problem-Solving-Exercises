Activity: Example PSE
Problem Statement
Imagine working on software for a game of Rock, Paper, Scissors  .

Create a function named winner that takes two arguments, the move for player_1 and player_2 ("rock", "paper", or "scissors"), and returns the winner ("Player 1 wins!", "Player 2 wins!", or "It's a tie").

Example Input/Output
Input (Argument of the function)	Expected Output (Return value of the function)	Explanation
player_1 = "rock"
player_2 = "scissors"	"Player 1 wins!"	"rock" beats "scissors"
player_1 = "rock"
player_2 = "rock"	"It's a tie!"	player_1 and player_2 played the same move
Complete Rock, Paper, Scissors Rules
input (first argument)	input (second argument)	output
player_1	player_2	return value
"rock"	"rock"	"It's a tie!"
"paper"	"paper"	"It's a tie!"
"scissors"	"scissors"	"It's a tie!"
"rock"	"paper"	"Player 2 wins!"
"rock"	"scissors"	"Player 1 wins!"
"paper"	"rock"	"Player 1 wins!"
"paper"	"scissors"	"Player 2 wins!"
"scissors"	"rock"	"Player 2 wins!"
"scissors"	"paper"	"Player 1 wins!"


Prompts

Ask Clarifying Questions
Submitted on 03/25/2023
List three or more questions whose answers would clarify the problem statement. For each question, provide an answer which includes the effect your decision would have on how you would approach the problem.

How should the function handle invalid user input (i.e. player_1 = "lizards")?
Should a user automatically lose if they have invalid input?
What should happen if both users have invalid input?
Does capitalization matter?
Does extra whitespace / punctuation matter?
Should anything be printed to the console?
Is the speed / memory usage of this function important?
Should there be a default value for each of the arguments?

Write Unit Tests
Submitted on 03/25/2023
Use the comments provided to write at least two example input/outputs:
Consider at least one nominal and one edge case.
What is the expected output for the given input?
You can use the examples provided in the prompt, or other examples.
Write unit tests for winner for the nominal and edge cases you identified in the first step.
Note: Click the Run Tests button to save your tests for instructor feedback. No real tests are actually run again your unit tests.

Create Logical Steps
Submitted on 03/25/2023
Without writing code, describe how you would implement winner in enough detail that someone else could write the code.

It may be helpful to break up the problem/algorithm into smaller subproblems/algorithms. For example, 1. Handle invalid input, 2. Given valid input, perform the computation/solve the problem/etc.
Your logical steps could take the form of a numbered list, pseudo code, or anywhere in between. What's important at this stage is to think through and outline the implementation before writing code.

.Check if player_1 and player_2 are in ["rock", "paper", "scissors"]
If not, return None
Check for a tie:
if player_1 == player_2, return "It's a tie!"
First deal with the case that player_1 == "rock"
if player_2 == "scissors", return "Player 1 wins!"
else (player_2 = "paper"), return "Player 2 wins!"
Next deal with the case that player_1 == "paper"
if player_2 == "rock", return "Player 1 wins!"
else (player_2 = "scissors"), return "Player 2 wins!"
Next deal with the case that player_1 == "scissors"
if player_2 == "rock", return "Player 2 wins!"
else (player_2 = "paper"), return "Player 1 wins!"
4



