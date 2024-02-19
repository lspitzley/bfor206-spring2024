#!/bin/bash

# a few things to demonstrate read/write operations

echo "Script started."

# this line will not show up anywhere.
echo "This is not an important line" > /dev/null

# read from a file into a variable named "input"
# read input < input.txt

while IFS="" read -r input || [[ -n $input ]]
do

    echo "The content of input is $input"

    # ping the address stored in the input file
    ping -c3 $input > /dev/null

    # store the exit status so it doesn't get overwritten
    status=$?

    # proper log entry
    echo "[INFO] `date`: Ping to $input completed with status $status" >> output.log

done < input.txt


echo "Done."
