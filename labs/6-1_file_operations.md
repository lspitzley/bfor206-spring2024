# BFOR 206 Lab 6-1: read/write

## Task Description

Write a script that pings multiple addresses
and logs the date/time and the ping
result to a log file.

Name the script `read_write_lab.sh` to allow automatic grading.

## Normal Scenario

### Input Description

**File:** File containing the following lines:
```shell
github.com
albany.edu
1.2.3.4
```

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

## Running the script
```bash
bash read_write_lab.sh
```

## Submission instructions

**Scripts that output bash errors will not be accepted!**

Run the script at least twice to show the
results being appendend to the file.

When you are finished, show the instructor:

1. Your code.
2. An output **file** that looks very
   similar to the output in the test cases. On some systems the 
   exit code will be 1 for the failed ping.
