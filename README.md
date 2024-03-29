# Problem Solving Exercises 
Practice skills related to thinking about problems through a technical lens, to include:  
* Communicating and displaying thought processes prior to coding
* Considering requirements 
* Asking questions of myself that may provide clarity about design
* Writing basic unit tests to ensure understanding of input vs output and/or requisite changes to mutable objects  



## Format 
---  

The format of each PSE (problem solving exercise) will include: 
1. Problem statement describing requirements
2. A clarifying questions exercise to practice thinking through how to approach the problem.
3. An exercise practicing writing pseudo code.
4. A unit test file to both test the sollution as well as practice writing tests.
5. A history of all the different ways I approached the problem in chronological order, with older sollutions commented out.

---  

## **Example PSE - Rock, Paper, Scissors**  

**Problem Statement** 

Imagine working on software for a game of Rock, Paper, Scissors  .

Create a function named winner that takes two arguments, the move for player_1 and player_2 ("rock", "paper", or "scissors"), and returns the winner ("Player 1 wins!", "Player 2 wins!", or "It's a tie").

*Example Input/Output*
![Image](images/Ex_input.png)

*Complete Rock, Paper, Scissors Rules*
![Image](images/Ex_output.png)

**Clarifying questions** 

- How should the function handle invalid user input (i.e. player_1 = "lizards")?
- Should a user automatically lose if they have invalid input?
- What should happen if both users have invalid input?
- Does capitalization matter?
- Does extra whitespace / punctuation matter?
- Should anything be printed to the console?
- Is the speed / memory usage of this function important?
- Should there be a default value for each of the arguments?

**Pseudo Code** 

- Check if player_1 and player_2 are in ["rock", "paper", "scissors"]
- If not, return None

Check for a tie:
- If player_1 == player_2, return "It's a tie!"
- First deal with the case that player_1 == "rock"
- If player_2 == "scissors", return "Player 1 wins!"
- Else (player_2 = "paper"), return "Player 2 wins!"
- Next deal with the case that player_1 == "paper"
- If player_2 == "rock", return "Player 1 wins!"
- Else (player_2 = "scissors"), return "Player 2 wins!"
- Next deal with the case that player_1 == "scissors"
  If player_2 == "rock", return "Player 2 wins!"
- Else (player_2 = "paper"), return "Player 1 wins!"


## **PSE 1 - Highest Rated**  

**Problem Statement** 

Create a function named `get_highest_rated` that is responsible for finding the highest rated restaurant.  

The function should take in a list of dictionaries named `restaurants` as a parameter. Each dictionary represents the data associated with a restaurant, including its rating. This function should have a return value of the restaurant with the highest rating.  

*Example Input/Output*
![Image](images/PS1.png)


**Clarifying questions**  

What should the function return if there are multiple restaurants tied for the highest rating?
How should the function handle restaurant dictionaries with missing data (name or rating)?
How should the function handle restaurant dictionaries with keys in addition to "name" and "rating"?
How should the function handle non-numerical values for "rating"?
How should the function handle input that is a single dictionary (not a list)?

**Pseudo Code** 

- Get the highest dict value
- If only 1 one highest value -> return message with highest rating
- If multiple tied for highest value -> return message with highest rating
- If no valid input available return "None"

---  

## **PSE 2 - Adagrams**  

**Problem Statement** 

Imagine programming the logic for a word game.

In this game, every player submits one word. Each word gets a score based on the letters in the word and its point value.

Create a function named score that is responsible for scoring a given word.
This function should take in a string named word as a parameter. This function should return the word's total number of points.

Refer to this table for the point values of each letter.

*Letter	Value*
![Image](images/PSE2_bank.png)

*Examples*
![Image](images/PSE2_sol.png)

**Clarifying questions**  

- Do we need to verify case? With which method? Test for this.
- Empty word string returns 0. Verify with test.
- Duplicate letters return the correct score. Verify with test.

**Pseudo Code** 

- Make a dict where each key is a letter and each value the score.
- Make a var to hold the value
- Write a loop so that for each letter in the word we look up the corresponding score value in the dict and add it to the value var.
- Return the value var

---  

## **PSE 3 - Hamming**  


**Problem Statement**  

Imagine working on software that analyzes mutations in DNA.

Create a function named hamming_distance that calculates the number of differences between two DNA strands (aka two strings). This method should take in two different DNA strands of the same length as parameters. This method should have a return value of the number of differences between each string.

For example, given these two DNA strands (strings), hamming_distance should return 7 because there are 7 differences:

![Image](images/PSE3.png)

Sourced from http://rosalind.info/problems/hamm/

**Clarifying questions** 

- If strands empty:
raise ValueError
- If strands not equal length:
raise ValueError
- If strand is not a string:
raise ValueError

**Pseudo Code** 

- check if strands are strings if not raise ValueError
- check if strands are empty if not raise ValueError
- check if strands are same length if not raise ValueError
- implement a counter
- make loop counting over each character in strand1
- check if index in strand1 == index in strand2
- increase counter if True
- return counter

---  

## **PSE 4 - Palindrome**  


**Problem Statement**  

Imagine working on software that processes text. A palindrome is a word, phrase, or sequence that reads the same backward as forward.

Create a function named palindrome that determines if a string is a palindrome. This method should take in one string as a parameter. This method should return True if the string is a palindrome.

*Examples*
![Image](images/PSE4.png)

**Clarifying questions** 

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

**Pseudo Code** 

Check if input is valid 
-> if empty or dict raise value error
Convert input to a string
Remove spaces, case, and punctuation
Use index to test if backwards is same as forwards
Return True

---  

## **PSE 5 - Pairs With a Given Sum**  


**Problem Statement**  

Imagine working on software that processes lists of numbers. Create a function named pairs_with_given_sum It finds the number of pairs of numbers in a list which add up to a given target. This function should take in a list of whole numbers and a target as parameters. This function should have a return value of the integer of number of pairs.

![Image](images/PSE5.png)

Sourced from: [Geeks for Geeks](https://www.geeksforgeeks.org/count-pairs-with-given-sum/) 

**Clarifying questions** 

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
- Assume numbers can't be reused because otherwise the list would be a set

**Pseudo Code** 

- Check if target is number -> raise type error
- Check if list is empty -> raise value error
- check if list contains numbers - raise value error

Loop over list and for each 
- find it's complement by subtracting it from the target
- add to dict
- look up if complement is in dict
- if yes add to count 
- return count

---  

## **PSE 6 - Merging Sorted Lists**  


**Problem Statement**  

Imagine working on software that processes lists of numbers. Create a function named merge_lists that takes two sorted lists and merges them into a single sorted list. This function should take in two lists of whole numbers. The function should return a new sorted list which consists of the elements of the two arguments.

![Image](images/PSE6.png)

Sourced from: [Leetcode](https://leetcode.com/problems/merge-sorted-array/) 

**Clarifying questions** 

- duplicate numbers in list? -> merge only once using set?
- modify one of the input lists or create a new results one? -> create new list
- how to handle non-numerical items in list? -> raise error
- what if one list is empty? -> return other one sorted
- what if both of them are empty? -> raise error

**Pseudo Code** 

if both lists empty, raise error
if list1 empty, return list2
if list 2 empty, return list 1

elif if 0 index of list1 > than 0 index of lists
return 0 index of list 1 + a recursive call of the merge function for all other positions
else return 0 index of list 2 + recursive call of the merge function for all other positions

for recursion:
num + whichever one is biggest of list1[0] and list2[0]

---  

## **PSE 7 - Reshape the Matrix**  


**Problem Statement**  

In MATLAB, a programming platform for numeric computing, there is a very useful function called 'reshape', which can reshape a matrix into a new one with different size but keep its original data.

You're given a matrix represented by a two-dimensional array, and two positive integers r and c representing the number of rows and number of columns of the wanted reshaped matrix, respectively.

The reshaped matrix need to be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the 'reshape' operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

*Example 1:*
![Image](images/PSE7-1.png)

*Explanation:*

The row-traversing of nums is [1,2,3,4]. The new reshaped matrix is a 1 * 4 matrix, fill it row by row by using the previous list.

*Example 2:*
![Image](images/PSE7-2.png)

*Explanation:*

There is no way to reshape a 2 * 2 matrix to a 2 * 4 matrix. So output the original matrix.

*Example 3:*
![Image](images/PSE7-3.png)

*Explanation:*

The original matrix was 4 * 2. The new reshaped matrix is a 2 * 4 matrix, fill it row by row by using the previous list.

*Note:*

The height and width of the given matrix is in range [1, 100]. The given r and c are all positive.

Sourced from: [Leetcode](https://leetcode.com/problems/reshape-the-matrix/) 

**Clarifying questions** 

- Should new matrix be a copy or replace the original?
Doesn't specify so put in new var for now.
- What if inputs exceed the constraints given?
Throw error
- Should there be a text output when the original is returned?
Yes, letting the user know is nice so that it's clear nothing went wrong.
- What if any of the inputs are invalid?
Throw error.

**Pseudo Code** 

- Create a one-dimensional list from the original matrix
    one_list = []
    for row in matrix:
        for column in row:
            append column to one_list

- Check if the reshaped matrix is valid
    if r * c is not equal to the length of one_list:
        return the original matrix

- Reshape the matrix
    reshaped_matrix = create an empty two-dimensional list
    for i from 1 to r:
        create a new row_list
        for j from 1 to c:
            pop the first element from one_list and append it to row_list
        append row_list to reshaped_matrix

- return reshaped_matrix

---  

## **PSE 8 - Kth Missing Positive Number**  


**Problem Statement**  

Given an array arr of positive integers sorted in a strictly increasing order, and an integer k.

Find the kth positive integer that is not present in the array.

*Example 1:*
![Image](images/PSE8-1.png)

*Example 2:*
![Image](images/PSE8-2.png)

**Clarifying questions** 

error handling edge cases:
- empty array 
- k is a negative num

What if k is larger than the array of missing positive ints or there are no missing ints in the set?
- add ints past last int in array

Does something need to be done in case the array contains extremely large numbers?
- Ensure the method of counting the missing numbers doesn't exceed the size of K

**Pseudo Code** 

if not arr or k == negative num throw error

Implement missing num counter
Implement missing num tracker

if num count != k:
num tracker += 1
if num tracker not in arr num counter += 1
else return num counter

---  

## **PSE 9 - Tic Tac Toe**  


**Problem Statement**  

Imagine working on software that determines the winner of a game of Tic Tac Toe. Create a function named tic_tac_toe_winner that is responsible for determing the state of a Tic Tac Toe board - Either there's no winner, it's a tie, 'X' won, or 'O' won. This function should take in 3x3 matrix as a parameter. Each element is either an 'X', 'O', or empty string ''. This function should have a return value of the winner 'X' or 'O', 'Tie' (for a full board with no winner), or None (for a game that is still in progress).

Example 1: Input:

[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'X', 'O']
]
 Save
Output: 'Tie'

Example 2: Input:

[
    ['X', 'O', 'X'],
    ['O', 'O', 'X'],
    ['X', 'O', '']
]
 Save
Output: 'O'

Example 3: Input:

[
    ['X', 'O', 'O'],
    ['O', 'X', 'O'],
    ['', '', 'X']
]
 Save
Output: 'X'

Example 4: Input:

[
    ['X', '', 'O'],
    ['O', 'X', 'X'],
    ['', '', '']
]
 Save
Output: None

**Clarifying questions** 

- Can we exit as none as soon as we find a ' '?
No, because there may be a winner.
- Can the input every be anything but valid?
No

**Pseudo Code** 

for each row, check that the first value is not ' ' and all the values are identical, if so return first value

for each column do the same

for each diagonal do the same

if no winner is found, check for ' ', if none are found return tie

return none

---  

## **PSE 10 - **  


**Problem Statement**  



**
![Image]()

**
![Image]()

**Clarifying questions** 



**Pseudo Code** 

---  

## **PSE 11 - Most Frequent K Elements**  


**Problem Statement**  



**
![Image]()

**
![Image]()

**Clarifying questions** 



**Pseudo Code** 

---  

## **PSE 12 - Linked List Intersection**  


**Problem Statement**  

Given the heads of two singly linked-lists head_a and head_b, return the node at which the two lists intersect. If the two linked lists do not intersect, the function should return None.

For example, the following two linked lists begin to intersect at the node 8:

*Example 1:*
![PSE12-1](images/PSE12-1.png)

The following two linked lists do not intersect at all.

*Example 2:*
![PSE12-2](images/PSE12-2.png)

For this problem, we want to focus on the nodes themselves and not necessarily the value inside of the node.

For example, while the following linked lists have tails that share the same values, they are not considered to intersect because the nodes of the linked lists are not the same nodes in memory.

*Example 3:*
![PSE12-3](images/PSE12-3.png)


**Clarifying questions** 

 - Do the lists have the same size leading up to the intersection point?
- Is there a size limit to the lists?
- What is the return if both lists are empty?
- What is the return if there is no intersection?
- Is the length of the lists known?
  

**Pseudo Code** 

If either list is empty, return None

Create a set to hold the nodes of list_a

Loop over list_a and add each node to the set

Loop over list_b and check if each node is in the set

---  

## **PSE 13 - Array to BST**  


**Problem Statement**  

Given a sorted array of integers, arr, write a function to create a balanced Binary Search Tree from the contents of the array. Return the root of the Binary Search Tree.

Example:

arr = [5, 10, 15, 20, 25, 30, 35, 40, 45]

should result in a tree with the following root/height:

![Alt text](images/PSE13.png)

Please note the following:

There will not be any duplicate elements in the array
One is not required to implement a self-balancing Binary Search Tree in order to solve this exercise. For an extra challenge, consider why it is unnecessary!


**Clarifying questions** 

- What do we return when array is empty?
- What if the array has only 1 element?
- Is there a preferred traversal and insertion method?
- What kind of data is stored in the Tree Nodes?

**Pseudo Code** 

1. Check for base cases:
   a. If the array is empty (length is 0), return `None` as there are no nodes to create the BST.
   b. If the array has only one element, create a new BST node with that element and return it.

2. Recursive case:
   a. Find the middle index of the array. If the length is odd, select the middle element. If the length is even, select one of the two middle elements.
   b. Create a new BST node with the value at the middle index. 

3. Construct the left and right subtrees:
   a. Recursively call function with the left subarray and assign the return value to the `left` attribute of the current node.
   b. Recursively call function with the right subarray and assign the return value to the `right` attribute of the current node.

4. Once the recursion bottoms out, it will backtrack, thereby constructing the entire BST from bottom to top.

5. Return the root node of the constructed BST.

---  

## **PSE 14 - Number of Provinces**  


**Problem Statement**  
Create a function num_provinces that takes in an adjacency matrix representing a graph of cities, is_connected. The function should return the total number of provinces represented by is_connected .

is_connected is a graph with N nodes. Each node represents a city. Two cities a and b belong to a single province if there is a possible path from a to b or vice versa.

Paths from a to b through intermediary cities such as a city c are valid paths.

is_connected[i][j] = 1 indicates that cities i and j are directly connected. Otherwise is_connected[i][j] = 0, even if there is an indirect path from i to j.

Return the total number of provinces in is_connected.

Adapted from: https://leetcode.com/problems/number-of-provinces 

*Example 1:*
![Alt text](images/PSE14-1.png)

Input:

```
is_connected = [
    [0, 0, 1],
    [0, 0, 0],
    [1, 0, 0]
]
```

Output: 2


*Example 2:*
![Alt text](images/PSE14-2.png)

Input:

```
is_connected = [
    [0, 1, 1],
    [1, 0, 1],
    [1, 1, 0]
]
```

Output: 1

*Example 3:*

![Alt text](images/PSE14-3.png)

Input:

```
is_connected = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
```

Output: 3

**Clarifying questions** 

- What do we return for an empty graph?
- If there is only 1 element in the graph, we can return immediately
- Will graph edges always be undirected?
- Will there be loops in the graph?
- What should we do in case of a malformed graph?
- Do we know the expected size of the graph?

**Pseudo Code** 

1. Check for base cases:
   a. If the graph is empty (length is 0), return 0.
   b. If the graph has elements other than 1 or 0 return False.
2. Create a set to hold the visited nodes.
3. Create a variable to hold the number of provinces.
4. Loop over the graph:
   a. If the current node has not been visited:
      i. Increment the number of provinces by 1.
      ii. Perform a depth-first search on the current node.
5. Return the number of provinces.
6. The depth-first search function:
   a. Add the current node to the visited set.
   b. Loop over the neighbors of the current node:
      i. If the neighbor has not been visited, perform a depth-first search on the neighbor.


---  

## **PSE 15 - Network Delay**  


**Problem Statement**  

For this exercise, create a function network_delay_time which accepts the following parameters:

A list of travel times, times. Each element of times represents a directed edge times[i] = (uᵢ, vᵢ, wᵢ) where uᵢ is the source node, vᵢ is the target node, and wᵢ is the time it takes for a signal to travel from the source node to the target node
The total number of nodes in the graph, n
The node from which a signal is being sent, source
The nodes in the graph are labeled from 1 to n.

Return the minimum time it takes for all of the nodes in the graph to receive the signal from the source node. If it is not possible for all of the nodes to receive the signal, return -1.

*Example 1*

![Alt text](/images/PSE15-1.png)

Input: times = [[2,1,1], [2,3,1], [3,4,1]], source = 2, n = 4
Output: 2
Explanation:
Starting from node 2: it takes 1 unit of time to reach node 1, 1 unit of 
time to reach node 3, and 2 units of time to reach node 4 (1 unit of time from 
2 -> 3 and 1 unit of time from 3 -> 4 so 2 units overall). 

Therefore, to reach all of the nodes, it would take a minimum of 2 units of time. 

*Example 2*
![Alt text](/images/PSE15-2.png)

Input: times =[[2,1,1], [2, 3, 2], [3, 1, 1]], source = 1, n = 3
Output: -1
It is not possible to reach any other node from node 1, so the function would 
return -1 to indicate it is not possible to reach all of the nodes in the graph
from the given source node.

*Example 3*
![Alt text](/images/PSE15-3.png)

Input: times =[[2, 3, 2]], source = 2, n = 3
Output: -1
It is not possible to reach all of the nodes in the graph due to the graph being 
disconnected, so the function would return -1 to indicate it is not possible to 
reach all of the nodes in the graph from the given source node.

**Clarifying questions** 

Edge cases:
- invalid input array/source
- array with 1 node
Are the weights all positive numbers or not?
Can there be multiple edges between the same nodes?
Is the graph always directed?

**Pseudo Code for Netwok Delay** 

1. Check for edge cases:
   a. If the graph is empty (length is 0), return -1.
   b. If the graph has elements other than ints return invalid.
   c. If the source node is not in the graph, return invalid.
   d. Check if the graph is directed or not.
   e. Check if the weights are all positive numbers.
2. Create a distance array with the length of the number of nodes in the graph
3. Set the distance of the source node to 0 and the distance of all other nodes to infinity
4. Create a priority queue and add the source node to it
5. While the priority queue is not empty:
   a. Pop the node with the smallest distance from the priority queue
   b. Loop over the neighbors of the popped node:
      i. Calculate the distance from the popped node to the neighbor
      ii. If the distance is less than the current distance of the neighbor, update the distance of the neighbor
      iii. Add the neighbor to the priority queue
6. Return the maximum distance in the distance array
7. If the maximum distance in the distance array is infinity, return -1

---  

## **PSE 16 - **  


**Problem Statement**  



**
![Image]()

**
![Image]()

**Clarifying questions** 



**Pseudo Code** 