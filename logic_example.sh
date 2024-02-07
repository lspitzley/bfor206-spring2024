#!/bin/bash

# This script will demonstrate logical tests with if statements.

savings=1000000
goal=1000000

if [[ $savings -gt $goal ]]
then
  echo "Time to retire."

elif [[ $savings -lt $goal ]]
then
  echo "keep working, buddy."

else
  echo "Savings are exactly the same as your goal."

fi
