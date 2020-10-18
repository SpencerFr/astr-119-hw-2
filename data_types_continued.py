#string

s = "I am a string"
print("The type of s is ",type(s))

#boolean
yes = True
print("The type of yes is ",type(yes))
no = False
print("The type of no is ",type(no))

#List -- ordered and changeable

alpha_list = ["a","b","c"] # list of str
print("The type of alpha_list is ",type(alpha_list))		#will say list
print("The type of alpha_list[0] is ",type(alpha_list[0]))	#will say string
alpha_list.append("d")										#will add "d" to the list end
print(alpha_list)											#will print list

#tuple -- ordered and unchangeable

alpha_tuple = ("a","b","c")								#tuple initialization
print("The type of alpha_tuple is ",type(alpha_tuple))	#will say tuple

try:													#attempt the following line
	alpha_tuple[2] = "d"								#won't work and will raise TypeError
except TypeError:										#when we get a TypeError
		print("We can't add elements to tuples!")		#print this message
print(alpha_tuple)										#will print tuple