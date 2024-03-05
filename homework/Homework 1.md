# Homework 1

The purpose of this homework is to develop a bash script that uses the ping
command to test whether a device is online. The results of this script
should be logged with a timestamp. The script should be run as a cron job.
If a server is not responding, email the system administrator (you).

## Useful commands

### exit status

The exit status of a command is stored in the variable `$?`. If 
a ping fails, then the exit status will be non-zero. You can use
this to check if a command was successful.

```console
ping -c1 1.2.3.4
echo $?
```

### ping

You can use this to check a device is responding.

```console
ping 192.168.1.1 -c3
ping google.com -c3
```

### mail (from mailutils package)

If you are on a Mac, you can skip the install process, it will work
out of the box. Send the mail to your UAlbany email in this case.

```bash

# To install:

sudo apt update # update software sources

sudo apt install mailutils # install mail package
```

```bash
# to send a message using echo
echo “message body” | mail -s “subject” kali@kali

# check mail with:
cat /var/mail/kali
```

## Script functionality

- Use a list of IP addresses using an input file or arguments
- Use a loop to ping a list of devices
- Parse the output of the ping command
- Check the output status
- If the ping is not responding or is missing packets, report this to the log
and send an email
- If the device is normal, report this to the log
- The script should run every five minutes.

## Grading

### 1. Ping devices (2 pts)

1. Show that the script pings addresses (1pt)
2. The script should be able to handle an arbitrary number of addresses to ping.
   To demonstrate this, ping at least *3* addresses.
   One of the addresses should contain your UAlbany NetID. For
   example, a NetID of AB123456 should ping 12.34.56.1. (1pt)

### 2. Log information (2 pts)

1. Show the log file with script output. The logs *must* have a timestamp
   for each entry (1pts)
2. Format the log file so that it is easy to read (1pt)

Example:

```console
2024-03-01 12:00:00 [INFO] ping 1.1.1.1 successful
2024-03-01 12:00:00 [WARNING] ping 1.2.3.4 failed
2024-03-01 12:00:00 [DEBUG] sending email here
```

### 3. Email when getting errors (3 pts)

1. Show the emails you receive from the failed pings for the out-of-service IP address.
   To receive credit for this, ping one address that does not respond and show the
   email that is sent as a result of the failed ping. (3pts)

### 4. Run task at regular intervals (3 pts)

1. Show the crontab file and the log demonstrating the program
   runs at the specified intervals. 5 minutes is a good interval to use. (3pts)

### 5. Avoid hard coded inputs (3 pts)

To recive credit for the following points, they must all be in a single script.

1. Accept addresses as arguments [Hint: $@ can be used to loop over
   all arguments]. (1pt)
2. Read addresses from a text file (1pt)
3. Read *multiple* addresses from a text file (1pt)

### 6. Code Management (1 pt)

1. Have at least 5 commits showing progress. They must be at least an hour apart (spamming 5 commits
   in a row doesn't count!) (1pt)
2. If two people worked on the assignment, then have at least 2 commits per person
  (1pt deduction if not).

## Scoring

The assignment is graded out of 12 points. Any score
above 12 is worth extra credit, meaning the highest
possible grade is 14/12.

## Submission

### Submission Format

**I will not run your code!**

Submissions include your code and screenshots for each of
the items you wish to receive credit for. Each screenshot should
be named according to the item, e.g. `Q5.1.jpg`. Submission materials
should be submitted to you the assignment repository.

### Point Reductions

I will deduct points for certain things:

1. Submitting code as a screenshot instead of the actual `.sh` file (-2 pts).
2. Screenshots that are not clearly labled. For example, submit a screenshot of the email
   you receive from the script. This would be named `Q3.1.jpg`. If a screenshot contains multiple parts,
   include them all in the filename (e.g. `Q2.1-2.jpg`). (1pt deduction for screenshots without labels).

### Submission Location

All homework will be submitted through Github Classroom.
The link for this assignment is on
[Github Classroom](https://classroom.github.com/a/yp1fHZH4).

## Teams (Optional)

You may work with one other person. If working with someone else,
then make sure to create a group submission. Include both names
in the README.md to make grading easier.
