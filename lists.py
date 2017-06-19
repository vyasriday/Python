# In this file we will perform different operations on lists,What are lists and how are they created?

print("List in python are mutable sequences of objects")

lists  = [1,2,3,4,5,6,7,8,9,0]
print(lists)

for i in lists:
	print(i)

#IN PYTHON A LIST UNLIKE ARRAYS IN C/C++ CAN HAVE HETEROGENOUS TYPE OF DATA

print(lists[2:5]) # Here we are slicing the data and printing values from [2,5)

print(lists[0:4:2])      #Here we are performing the slicing in which we want to print data from 0 inclusive to 4 exclusive in steps of 2. It will print 1 and 3 

new_list = [1,2,3,4,"These","Are","strings",1.23,4.56,]

for values in new_list:
	print(values)

#new_list[9] = "We can not assign value to out of index values,This can only be done by using append() method"

new_list.append(10) # This will append 10 at the end of the list
print(new_list)

new_list[0] = " this is changed value"

print(new_list)

print(list("THIS IS A LIST CONSTRUCTOR")) # This is a list constructor which is used to create list

# There are many methods to create and copy lits

s = "This is how a sequence is created in a list".split()
print(s)

# We can copy this list in many ways
#1 using the list constructor 
new_list = list(s)
print(new_list)
print(s is new_list)

#2 using the copy method

new_list1 = s.copy()
print(new_list1)
print(s is new_list1)

#3 By Slicing in the list. We can separate or extract list elements by slicing them.

sliced_list = s[:] # 
print(sliced_list)
print(s is sliced_list)

print(s[:5])

print(s[3:])

print(s[1:6])

print(s[:])

#We can aslo use negative numbers in list slicing. 

'''
	This    	= 	s[0] , s[0]
	is      	=   s[1] , s[-9] 
	how         =   s[2] , s[-8] 
	a           =   s[3] , s[-7] 
	sequence    =   s[4] , s[-6] 
	is          =   s[5] , s[-5] 
	created     =   s[6] , s[-4] 
	in          =   s[7] , s[-3] 
	a           =   s[8] , s[-2] 
	list        =   s[9] , s[-1] 
'''


print("Here is a list of indexes with their negative counterparts\n")

print(s[0] , s[0])
print(s[1] , s[-9])
print(s[2] , s[-8])
print(s[3] , s[-7])
print(s[4] , s[-6])
print(s[5] , s[-5])
print(s[6] , s[-4])
print(s[7] , s[-3])
print(s[8] , s[-2])
print(s[9] , s[-1])


print(s[-5:-1])
print(s[:-1])
print(s[-1:])

l = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]

m  = l[:]
print("l" ,l)
print("m ",m)

print(l is m)
print(l==m)

# Since only outer list is duplicated the references in inner list are same and hence they refere to same objects
print(l[0] is m[0])
print(l[0] is m[0])
print(l[0] is m[0])

#let us append a new value in one list
l[0].append(12)
print(l,m) # We saw that when we append a new value in one list both the lists change.


# Now we will try to change the values at inner list for l list 
l[0] = [0,0,0]

# Let us now printt the changed list

print(l)
# The list m remains unchanged
print(m)

l[0].append(12)
print(l,m)

m[1].append(18)
print(l)
print(m)

l[0].append(12)
print(l,m)

y = [1,2,3,4]
z = y[:]
print(y,z)

y[0] = 12

print(y,z)

y.append(13) # Only y will have this effect as they both have different references and there are no inner lists.
print(y,z)

w = [[1,2],[3,4]]
s = w[:]

w.append([1,2,3]) # This append will create a new list reference and hence only w will be affected.
print(w,s)

print("List Repetetion")

b = [1,2,3,4]
print(b*2)

b = [[1,2,3],[0,0,0]]
print(b*4)
print(b)
b = b*5
print(b)

print(1 in b)

print(b.count([0,0,0])) # Count the occurences of an element in a list


print("How to remove an element from the list using the del keyword")

k = "you and I are in to this together".split()
print(k)

del k[0]  # Use del and the index of value we want to delete
print(k)

#Using remove method to delete an element

k.remove('together')
print(k)

#Finding the index of a value in a list

print(k.index('I'))

#Inserting a new elment in the list using insert method

k.insert(0,"You") #Here 0 is the index where we want to insert a new value and the "You" is the value itself

print(k)

#How to create a string back from a list

print(' '.join(k)) # Where ' ' is the separator for the list and k is the list we want to create string from.

# Using the extend list method to increase the size of a list

k.extend([12,13,14]) #This will extend k with the new elements. extend takes one parameter therefore pass a list

print(k)

k += [1,2,3]
print(k)

# Reversing and sorting in the list

# Reversing the list using reverse method
t = [11,2,30,14,5]
t.reverse()
print(t)

# Sorting the list using sort method

t.sort(reverse=True) # Print in reverse order i.e descending order

print(t)

t.sort(reverse=False) # Ascending order

print(t)

t.sort() # By default the list is sorted in ascending order
print(t)

y = "I do know  not doctors for handwriting family ".split()
print(y)

y.sort(key=len) # sort list on the bsis of length of elements

print(y)

print(' '.join(y))

#sort and reverse this methods modify the original lists. We can use sorted() and reversed() method which do not modify original lists

x = [12,15,0,1,78]
#q = x.sorted() Need to see why it is not working here.

#print(x)
#print(q)
