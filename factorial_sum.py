#####################################################
######## Done by Suvana Rohanlal ####################
#####################################################
######## Corigine Technical Assignment ##############
#####################################################

#Imports
import sys
import numpy as np

#Compute the factorial and sum
def main(n):
    #Perform the factorial of the input	
    fact = np.math.factorial(n)
    print(fact)
       
   
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
