# BFOR 206 Lab 4-2: For Loops

## Task Description

Write a script that accepts an integer argument or
reads user input, and then outputs that many
values of the Fibonacci sequence.

In the Fibonacci sequence, each number is the sum of
the two previous numbers in the sequence.

The sequence starts at 0 and 1. That is, the 0th
  number in the sequence is 0, the 1st number
  in the sequence is 1, the 2nd number is 0+1=1.

Because the sequence starts at 0,
the sequence up to the the fourth number is:
0 1 1 2 3

For more information about Fibonacci numbers,
see the
[Wikipedia page](https://en.wikipedia.org/wiki/Fibonacci_number).

## Normal Scenario

### Input

**Arguments:** an integer *n*.

***or***

**User Input:** an integer *n*.

### Output

**Terminal:** The sequence up to the position *n*.

## Test Cases

```shell
######## Normal scenarios ##########

# Input:
bash for_lab.sh 4

# Output:
0 1 1 2 3  

# Input:
bash for_lab.sh 8

# Output:
0 1 1 2 3 5 8 13 21

######### Special Cases ##########

#---- The 0th number of the sequence ----#
# Input:
bash for_lab.sh 0

# Output:
0

#---- The 1st number of the sequence ----#
# Input:
bash for_lab.sh 1

# Output:
0 1

```

## Submission instructions

**Scripts that output bash errors will not be accepted!**

When you are finished show the instructor:

1. Your code.
2. The correct output as defined in the test cases.
