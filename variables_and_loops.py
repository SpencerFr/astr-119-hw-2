import numpy as np #we ise numpy for lots of things

def main(): #define the main function
	
	i = 0 #declare integer i = 0

	n = 10 # declare n = 10 integer

	x = 119.0 # float point num are declared with .

	# we can use numpy to declare arrays quickly

	y = np.zeros(n,dtype=float)

	#we can use loops to iterate through arrays
	for i in range(n): # in range 0-9
		y[i] = 2.0 * float(i) +1.0 # y = 2*i +1

	#we can also iterate through a variable
	for y_element in y:
		print(y_element)



#execute the main function
if __name__ == "__main__":
	main()