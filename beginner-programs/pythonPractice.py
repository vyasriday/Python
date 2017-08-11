''' In this module we will be writing some functions and importing them in other modules

	List of Functions in this module

	1. isPrime()  
		
		Arguments : takes exactly one argument
		return : returns whether a no is prime or not

	2. isEven_Odd() 

		Arguments : takes exactly one argument
  		return : returns if a no is even or odd

  	3. square()
		
		prints the squar of a given value

	4. generate()
		
		shows the use of yield keyword in generat functions

	5. comprehend_list()

		shows the use of list comprehension

	6. iterator()

		iterates over a list and shows the use of iter() and next() function

	7. set_comprehension()

		which shows the use of comprehension in sets	
	
	8. dict_comprehension 

	9. random_generate
'''
from math import sqrt
from random import randrange

class functions:

	def isPrime(x):
		for i in range(2,int(sqrt(x))+1):
			if(x%i==0):
				return print(x , " is non Prime ")
		return print(x , " is Prime ")


	def isEven_Odd(x):

		if x%2==0:
			return print(x , " is even integer")

		else:
			return print(x ," is odd integer")


	def square(x):

		return print(x**2 ," is square of " , x)


	def generate():

		print(" This is first round ")
		yield 1

		print(" This is second round")
		yield 2



	def comprehend_list():

		y = [x**3 for x in range(1,25)]
		print(y)


	def iterator(l):
		g = iter(l)

		for i in range(len(l)):
			print(next(g))



	def set_comprehension():
		set_s = set([1,2,34,5,6])

		g = iter(set_s)

		for i in range(len(set_s)):
			print(next(g))


	def dict_comprehnsion():

		d = {x[0]:x for x in ['Hello','This','is','Eminem']}
		print(d)

		g = {value : key for key,value in d.items()}

		f = iter(g)

		for i in range(len(d.keys())):
			print(next(f))


	def random_generate():

	# in this  function we will generate some random numbers between a given pair of numbers
		for i in range(1,100,3):

			g = randrange(1,501)
			print(g)



