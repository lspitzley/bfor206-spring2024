# BFOR 206 Lab 6-1: read/write

## Task Description

Write a script that pings multiple addresses
and logs the date/time and the ping
result to a log file.

## Normal Scenario

### Input Description

**File:** File containing a URL or IP address

### Output Description

**File:** The date/time and result of the ping
          ping command.

## Test Cases

```shell
######## Normal scenarios ##########

# Input (from file):
github.com
albany.edu
1.2.3.4

# Output (in a file)

[INFO] Sun Feb 18 22:50:17 EST 2024: Ping to github.com completed with status 0
[INFO] Sun Feb 18 22:50:19 EST 2024: Ping to albany.edu completed with status 0
[INFO] Sun Feb 18 22:50:32 EST 2024: Ping to 1.2.3.4 completed with status 2

```

## Submission instructions

**Scripts that output bash errors will not be accepted!**

Run the script at least twice to show the
results being appendend to the file.

When you are finished, show the instructor:

1. Your code.
2. An output **file** that looks very
   similar to the output in the test cases.
