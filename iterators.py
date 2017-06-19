# LIST COMPREHENSION

words = "This is how I find it nearly impossible to combat the war".split()
print(words)

print([len(word) for word in words])


new = words[:]

print("New List is " ,new)

new.extend(['lets','us','update','the','list'])

print(new)

print([len(word) for word in new])

def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

banner("\n\nMethod for list comprehension : [expr(item) for item in iterable]\n",'-')

from math import factorial

lengths = [len(str(factorial(x))) for x in range(25)]
print(lengths)

print(type(lengths))


print("\n")
for i in range(25):
	print(factorial(i))

# SET COMPREHENSION

banner("\n\n Method for set comprehension : {expr(item) for item in iterable}",'-')

s = set(lengths)
print(s) # duplicates will be removed

newS = {len(str(i)) for i in range(0,10000,241)}
print(newS)

banner("\nDictionary comprehension are done as : {key_expr:value_expr for item in iterable}\n")

from pprint import  pprint as pp

country_to_capital = {'India' : 'New Delhi', 'Pakistan' : 'Karachi','Britain' : 'London', 'Brazil' :'Brazilia'}

pp(country_to_capital)

capital_to_country = {capital:country for country,capital in country_to_capital.items()}
print("\n")
pp(capital_to_country)

# In case of duplicates later keys overrite the earlier keys

x_words = ['Hi' ,'Hello','How','Are','You']

pp({x[0]:x for x in x_words})

import os
import glob
file_sizes = {os.path.realpath(p) : os.stat(p).st_size for p in glob.glob('*py')}

pp(file_sizes)


# Prime Number check program

from  math import sqrt

# We can use predicate filtering with comprehension. All of three list,set and dictionary comprehension allow predicate filteting

banner("For Predicate Filtering Use : [expr(item) for item in set/dict/list if predicate(item)]")
def isPrime(x):
	if x<2:
		return False

	for i in range(2,int(sqrt(x))+1):
		if(x%i==0):
			return False
	return x

print(isPrime(5))

# Elements which are not prime here will be printed as False
print([isPrime(i) for i in range(100)])

# What if we just want to see prime numbers. We can use predicate filtering
# Only those numbers will be printed for which isPrime() is True

print({isPrime(i) for i in range(101) if isPrime(i)})

print({isPrime(i) for i in range(101) if not isPrime(i)}) #Sice it is a set only one False is Printed.

pp({x : (1,x,x*x) for x in range(151)})


# Concept of iterator and iterable objects

iterable = ['Spring','Autuum','Winter','Summer']

iterator = iter(iterable)

print(iterator)

for i in range(4):
	print(next(iterator))

#We can also use the same iterable objects and iterator concept in dictionaries and sets  as well as tuples

t = (1,2,3,4,5,6,7,)

iterator = iter(t)

for i in range(len(t)):
	print(next(iterator))

# In case of dictionaries keys are iterated

set_t = {11,2,1,1,2,3,4,5,6}

iterator = iter(set_t)

for i in range(len(set_t)):
	print(next(iterator)) # Only on eoccurence of any repeted element is printed

# Using exception handling to handle StopIteration error in Python

def first(iteration):

	iterator = iter(iteration)
	try:

		return next(iterator)

    except StopIteration:

		raise ValueError("Iterable is Empty")
		pass

first(set())





