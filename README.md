## Project name: Factorial Sum using Python3

## Description:
This is a python implementation of the sum of the digits after performing a factorial. All mathematical operations are completed using numpy. 
 
## Table of Contents:
	1. Files
	2. Explantion
	3. Usage
	4. Results
	5. Credits

## Files:
	1. src/factorial_sum.py - python file containing the computation of the factorial and sum of digits.
	2. Dockerfile - Used to create the docker container
	3. requirements.txt - contains the dependicies required for installation 

## Explanation
	For factorial, n! means n x (n-1) X (n-2) ... 3 x 2 x 1
	For example, 10! = 10 x 9 x 8 ... x 3 x 2 x 1 = 3628800
	Finding the sum of all the digits for 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
	
## Usage:
	1. Navigate into the project folder using the following command:
		cd Factorial_sum
		
	2. Build the file using the following command:
		docker build -t factorial_sum .
	
	3. Run the file using the following command:
		docker run --rm factorial_sum -n10

	If permission is denied use:
	sudo docker build -t factorial_sum .
	sudo docker run --rm factorial_sum -n10
	
	4. "docker run --rm factorial_sum -h" allows you to check what arguments are required. 
	
	Arguments:
	The number at the end (10) is an argument and can be changed to any number that you would like to test.
	The argument is set as follows: 
	-n followed by the number. Example, -n100 will find the factorial sum of 100 

## Results:
	1. The result will be displayed in the command line after running the file. 

## License :
	MIT

##### Credits: Done by Suvana Rohanlal - 26/07/2021
