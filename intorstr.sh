#!/bin/bash

tester() {
read -p "Input: " INPUT
if [[ $INPUT =~ ^[a-z]*$ ]]
then
	echo "You entered a string."
elif [[ $INPUT =~ ^[0-9]*$ ]]
then
	echo "You entered an integer."
else
	echo "I received invalid input."
fi
}

tester
