'''These are some of the collection types in Python

1. tuples
2. str
3. list
4. dict
5. range
6. set

'''

# FIRST OF ALL LETS TALK ABOUT TUPLES
def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)
print("\n")
banner('TUPLES')
print("\n")

t = (12,14,125) # This is how we create tuples. 
print(t)

# If we want to create single element tuple this is how we create one

single_t = (21) # this is how instead of tuple int is created
print(type(single_t))

single_t = (21,)  # This is the way of creasting a single element tuple

print(type(single_t))

# We can expand our tuples by using + operation

single_t + ('New','Elements') # Here the original tuple remains unchanged

print(single_t)

print(single_t + ('New','Elements'))

# We can also do nesting of tuples
# Nested tuples work like 2D arrays
nested_t = ((1,2,3),(2,3,4),(4,5,6))

print(nested_t[0][2])  # Prints 3

print("nested list")
# We can print each element in nested tuple by this way
for i in range(3):
	for j in range(3):
		print(nested_t[i][j])



more_nested_t = (((1,2,3),(4,5,6),(7,8,9)),(('a','b','c'),('d','e','f'),('g','h','i')),((1.2,3.4,5.6),(0.1,6.7,7,8),(9.2,9.1,9.1)))

print("Here comes the more nested list")
for i in range(3):
	for j in range(3):
		for k in range(3):

			print(more_nested_t[i][j][k])



direct_t = (a,b,(c,(d,e),f),g) = (0,1,(2,(3,4),5),6)

for i in range(4):
	print(direct_t[i]) 

print("direct_t = ",direct_t)
print("direct_t[0] = ",direct_t[0])
print("direct_t[1] = ",direct_t[1])
print("direct_t[2] = ",direct_t[2])
print("direct_t[2][0] = ",direct_t[2][0])
print("direct_t[2][1] = ",direct_t[2][1])
print("direct_t[2][1][0] = ",direct_t[2][1][0])
print("direct_t[2][1][1] = ",direct_t[2][1][1])
print("direct_t[2][2] = ",direct_t[2][2])
print("direct_t[3] = ",direct_t[3])


# Using in and not in operators we can test if a number belongs to a tuple or not

print(2 in direct_t) # returns false becuase 2 is present in nesting 

print( 6 in direct_t) # will return false

# We can also generate a tuple from an existing list or strings using tuple constructor

print(tuple([12,13,14,15]))
print(tuple([[1,2,3],[3,4,5],6]))

print(tuple("characters"))

print("\n\n")
banner("Strings",'*')
print("\n")

# Now we will talk about strings

s = "Hridayesh Sharam"
print(len(s))

# Strings can be concated using + operation

new_S = "Hridayesh " + " Sharma " + "cool"
print(new_S)

# HOW TO USE JOIN OPERATION ON STRINGS

join_string = ';'.join(['First_String','Second_String','Third_String','fourth_Strng'])
print(join_string) # Here the above list will be joined using ; as delimiter

# We can use anything in join operation to delimit strings
# We need to pass a list because join only takes one argument
join_string_1 = '*'.join(['First_String','Second_String','Third_String','fourth_Strng'])

print(join_string_1)

# This is how we reverse the join operation

print(join_string.split(';'))

# PARTITION OPERTION ON STRINGS

print("UNFORGETTble".partition('GET')) # this will separate the string into UNFOR,GET,Tble and returns a tuple
print("separate me from myself".partition('me'))

departure , arrival , gone = "LONDON:NEWYORK:SPAIN".partition(':')

print(departure)
print(arrival)
print(gone)

# Using format() method to take strings

print( "The age of {} is {}".format('Jim','32'))
print("The age of {0} is {1}".format('John Snow',45))

print("The age of {0} is {1}. {0} Birthday is on {2}".format('Jim Morialty',26,'31 Oct 2017'))
print("The age of {} is {}. {} Birthday is on {}".format('Jim Morialty',26,'Jim Morialty','31 Oct 2017'))

print("Current position is {latitude} {longitude}".format(longitude="43W",latitude="81N"))

pos = (3,5,2)
print("Galactic position is x = {pos[0]}, y ={pos[1]}, z = {pos[2]}".format(pos=pos))

import math

print("Math Constants : pi = {m.pi}, e = {m.e}".format(m = math))
print("Math Constants : pi = {m.pi:.4f}, e = {m.e:.3f}".format(m = math)) #:.3f stands for string formatting

banner("\n\nRANGE\n",'_')

print("\n")

print(range(5))
print(range(0,5))
print(range(12,15,1))
print(range(0,50,2))

for i in range(0,50,2):
	print(i)

#for i in enumerate(10):
#	print(i) error int object is not iterable

tuple_t = (1,23,4,5,6)

for p in enumerate(tuple_t): # It prits index no as well as value at that index
	print(p)

for p in range(len(tuple_t)):
	print(p)

#for p in range(tuple_t):
#	print(p)   this also creates error tuple is not iterable

x = ['color','yellow','red','blue']
for i in enumerate(x):

 	print(i)



banner("\n\nLIST AND SET DONE IN SEPARATE FILE\n")



