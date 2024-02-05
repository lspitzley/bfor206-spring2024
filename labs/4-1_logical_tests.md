# BFOR 206 Lab 4-1: Logical Tests

## Task Description

Write a script that accepts takes two integers and adds them together.

The script should use an if statement to check that there are two arguments.
If there are greater/fewer than two arguments, let the user know.
If there are exactly two arguments, add them together and show the result.

## Normal Scenario

### Input
**Arguments:** two integers

### Output

**Terminal:** The sum of two numbers.

## Abnormal Scenario

### Input

**Arguments:** fewer or greater than two args

### Output

**Terminal:** Message informing user that the
number of arguments is incorrect.

## Test Cases

```shell
######## Normal scenario ##########

# Input: 
bash logic_lab.sh 20 21
# Output: 
sum = 41

######## Abnormal scenarios ##########

# Input:  
bash logic_lab.sh 9
# Output: 
Error! 1 argument(s), need exactly two.

# Input 
bash logic_lab 1 2 3
# Output: 
Error! 3 argument(s), need exactly two.
```

## Submission instructions

**Scripts that output bash errors will not be accepted!**

When you are finished, show the instructor:

1. Your code.
2. The correct output as defined in the test
   cases.
