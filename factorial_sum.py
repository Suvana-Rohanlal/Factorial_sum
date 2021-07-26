#####################################################
######## Done by Suvana Rohanlal ####################
#####################################################
######## Corigine Technical Assignment ##############
#####################################################

#Imports
import sys
import numpy as np

# Find the sum of each digit after performing the factorial
def factorialSum(fact):
    finalSum=0
    while fact>0:
    	#Find each digit
        digit = np.mod(fact,10)

        #Find the sum of the digits
        finalSum = np.add(finalSum,digit)
        
        fact = fact//10
        
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
        userInput = int(sys.argv[1])
        
        #Check if the input is valid
        if userInput < 0:
            print("Number must be postive")
        else:
            main(userInput)
    except Exception as e:            
        print(e)
