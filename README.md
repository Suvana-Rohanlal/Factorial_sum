Project name: Factorial Sum using Python3
Description:

This is a python implementation of the sum of the digits after performing a factorial. All mathematical operations are completed using numpy. 
 
Table of Contents:

1. Files
2. Usage
3. Results
4. Credits

Files:
1. src/factorial_sum.py - python file containing the computation of the factorial and sum of digits.
2. Dockerfile - Used to create the docker container
3. requirements.txt - contains the dependicies required for installation 

Usage:
1. Build the file using the following command:
	docker build -t factorial_sum .
	
2. Run the file using the following command:
	docker run --rm factorial_sum 10

If permission is denied use:
	sudo docker build -t factorial_sum .
	sudo docker run --rm factorial_sum 10

The number at the end (10) can be changed to any that you would like to test.

Results:
1. The result will be displayed in the command line after running the file. 

License :

MIT

Credits: Done by Suvana Rohanlal - 20/01/2021
