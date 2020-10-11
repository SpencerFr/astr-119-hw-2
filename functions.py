import numpy as np
import sys

#Define a function that returns a value
def expo(x):
	return np.exp(x) #return the np e^x function

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) #call the expo function


#define our main function
def main():

	n = 10 # default value for n

	#check if there is a command line arg provided
	if(len(sys.argv)>1):
		n = int(sys.argv[1]) #if an arg was provided, set n to it

	print("The value of n is ",n)

	show_expo(n) #call the show_expo sub

#run the main function
if __name__ == "__main__":
	main()