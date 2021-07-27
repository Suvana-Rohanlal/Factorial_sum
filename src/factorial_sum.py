#####################################################
######## Done by Suvana Rohanlal ####################
#####################################################
######## Corigine Technical Assignment ##############
#####################################################

#Imports
import sys
import optparse
import numpy as np

# Find the sum of each digit after performing the factorial
def factorialSum(fact):
    finalSum=0
    while fact>0:
    	#Find each digit
        fact, digit = divmod(fact,10)

        #Find the sum of the digits
        finalSum = np.add(finalSum,digit)
    return finalSum
    
#Compute the factorial and sum
def main(n):
    #Perform the factorial of the input	
    fact = np.math.factorial(n)
    
    #Display the result
    print(factorialSum(fact))
       
   
if __name__ == "__main__":
    try:
    	#Extract the input argument
    	parser = optparse.OptionParser()
    	parser.add_option('-n',dest='num',type='int', help='Input the number that you want to use to find the sum of the digits after factorial')
    	(options, args) = parser.parse_args()

    	#Check if the input is valid
    	if options.num < 0:
            print("Number must be postive")
    	else:
            main(options.num)
    except Exception as e:            
        print(e)
