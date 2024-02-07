#!/bin/bash

# This script is going to show examples of arrays and for loops

# if statements to control which example is run.
if [[ $1 -eq 0 ]]
then
  # array examples
  test_array=( "one" "two" "three" )

  echo "the variable \$test_array is ${test_array[@]}"
  echo "the value at position 0 is ${test_array[0]}"
  echo "the value at position 1 is ${test_array[1]}"
  echo "the value at position 2 is ${test_array[2]}"

elif [[ $1 -eq 1 ]]
then
  # first for loop example
  for i in {0..5}
  do
    echo "The value of \$i is $i"
  done

elif [[ $1 -eq 2 ]]
then
  # second for loop example with an array
  name='Lee A Spitzley'
  for part in $name
  do
    echo "The value of \$part is $part"
  done

elif [[ $1 -eq 3 ]]
then
  # Example showing increments other than 1
  for n in  {0..10..2}
  do
    sum=$(( $sum + $n ))
    echo "The value of \$n is $n and \$sum = $sum"
  done

elif [[ $1 -eq 4 ]]
then
  # Example with C-style control
  N=10
  for (( i=0; i<N; i++ ))
  do
    echo "The value of \$i is $i"
  done
fi
