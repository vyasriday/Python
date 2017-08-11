# Generators in Python are iterators and basically they are functions and use of keyword yield is necessary atleast once in generators

def gen123():
	yield 1
	yield 2
	yield 3

g = gen123() # it is equivalent to iter(iteration) .

print(g)

# We can use built in next() function to get next value in iteration

for i in range(3):
	print(next(g))

for v in gen123():
	print(v)


h = gen123()

print(h is g) # returns false and h and g both have different addresses and can be iterated independently


# Using generatros to print fibonacci series

def fibonacci():
	yield 1
	a = 0
	b = 1

	while True:
		a = b
		b = a+b
		print(a , " " ,b)


fibonacci()

# Genertor Comprehension

million_Squares = (len(str(x*x)) for x in range(1,1000001)) # Here instead of [] for list we are using () for list

g = million_Squares

for i in million_Squares:
	print(next(g))
