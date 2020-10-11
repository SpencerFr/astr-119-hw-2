
#define the main() function
def main():
	i = 0 #integer i = 0
	x = 119.0 # x = 119.0

	for i in range(120): #loop i from 0 to 119, inclusive
		if((i%2)==0):    #if i is even
			x += 3.0	 	#add 3  to x
		else:			#if i is odd
			x -+ 5.0		#subtract 5 from x

	s = "The value of x is x = %3.2e" % x	#make a string containing x with
											#sci.notation w/ 2 decimal places

	print(s)								#print s to the screen						

#not the rest of the program continues

if __name__ == "__main__": #if the main() function exists
	main()