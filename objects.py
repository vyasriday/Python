def modify(l):
	l.append(12)
	print("Modified list m = ",l)


print("In case of python the function changes the actual list as when it is passed to  a function it;s references is passed to function")



m = [2,3,4,5,] # This is our original list
p = m
print("m =",m)       # It prints [2,3,4,5]
modify(m)      # List is modified here and modified list is printed in function. Here actual reference of list is passed not a copy of it.
print("m = ",m)       # It prints the same modified list as it also gets modified outside the function.

print("p = ",p)       # Even we copied before function call but it prints the same modified list because it contains the same original reference to list object       

# Here we will try to replace the original list Let us see how that works.
def replace(g):
	g = ['a','b','c']
	print("g = ",g)

f = [14,17,287,]
replace(f)
print("f =",f)  # f is still the same unmodified list.

# How to change the contents of original list

def replace_contente(y): # This is how original list contents are changed.
	y[0] = 1
	y[1] = 2
	y[3] = 5
	print(" y =",y)
y = [0,0,0,0]
replace_contente(y)


# Pytohn uses strong typechecking and does not implicitly convert one type in to another
# eg . we can do 'abc' + 123

