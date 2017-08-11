# How to get default encoding in Pythno

import sys

print(sys.getdefaultencoding())

# f is pointer which will point to file

f = open('wasate.txt',mode ='wt',encoding='utf-8')
#Let us see what f has for us
print(f)

# Now let us write some data in to the file

f.write('This data may get appended to in the new file\n')
f.write('This is another line I am going to write in my file')

# Now let us close the file

f.close()

# Data can be read from a file using read() method which takes no characters to read a an argument

f = open('wasate.txt',mode='rt',encoding='utf-8')


print(f.read(12)) #pointer is at 12 and next read is done from 13 
print(f.read(50))

f.read() # Do not pass any argument to read all of the data

f.seek(0) # brings the file pointer to 0 or beginning of the file

# Better method for th eabove thing is readline() method

f.readline() # reads one line at a time
# Once we reach the end of the file furthr calling readline() returns empty string

# To read multiple lines we can call readlines() method
f.seek(0)
f.readlines()
f.close()
# To append data to our file we can open our file in a mode

f = open('wasate.txt',mode='at',encoding='utf-8')

f.write('Let see if this data gets appended to our file\n')
f.write('Let us hope so')

f.close()
f = open('wasate.txt',mode='rt',encoding='utf-8')

print(f.readlines())

f.close()

# We can also write multiple lines to a file using writelines() method

f = open('wasate.txt',mode='at',encoding='utf-8')

f.writelines(['This is first string\n' , 
				'Here comes the another\n',
				"Now the third line that's it"])

f.close()

f = open('wasate.txt',mode='rt',encoding='utf-8')

print(f.readlines())


f.close()

f = open('wasate.txt',mode='rt',encoding='utf-8')

print("\nHere we will print the data using iterators in files\n")

for line in f:
	print(line)

f.close()

# Using above methods each time we need to explicitly close the file because it is necessary to close the file once we are done with it.
# we can also do the following 
# Open file using with ... as

with open('wasate.txt', mode='rt',encoding='utf-8') as f:
	for line in f:
		print(line)

# Once we are done with for the with automatically closes the file.

f = open('wasate.txt', mode='rt',encoding='utf-8')
print(f.readlines())

f.close()
#f.write('Here I am trying to learn with ... as constructs')

#f.close()

