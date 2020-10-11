import numpy as np 

#integers
i = 10 #integer
print(type(i)) #print out the data type of i

a_i = np.zeros(i,dtype=int) #declare an array of ints
print("The type of a_i is ",type(a_i)) #print out the data type
print("The type of a_i[0] is ",type(a_i[0])) #print out the data type

#floats
x = 119.0 #floating point number
print("The type of x is ",type(x)) #print out the data type

y = 1.19e2
print("The type of y is ",type(y)) #print out the data type

z = np.zeros(i,dtype=float) #array of floats
print("The type of z is ",type(z)) #print out the data type
print("The type of z[0] is ",type(z[0])) #print out the data type

d = np.zeros((2,2),dtype=(float))
d[0,0] = 1.0
d[0,1] = 1.0
print(d)