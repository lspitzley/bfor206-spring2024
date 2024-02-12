#!/bin/bash

# This script will demonstrate while loops

counter=0
LIMIT=10

# run a while loop with counter & limit

while [[ $counter -le $LIMIT ]]
do
  echo -n "$counter "
  let "counter += 1"
done

# Second example 
# printf lets you use the newline character \n
# https://stackoverflow.com/questions/8467424/echo-newline-in-bash-prints-literal-n
printf "\nStarting second example\n"

a=0
while [[ $a -le $LIMIT ]]
do
  (( a=a+1 ))

  if [[ $a -eq 3 ]] || [[ $a -eq 11 ]]
    then continue
  fi

  echo -n "$a "
done




