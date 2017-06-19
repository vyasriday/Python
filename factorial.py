def factorial(x):
	if(x==0):
		return 1

	else:
		return (x*factorial(x-1))


def factorial_better(x):
	if(x>0):
		return x*factorial_better(x-1)

	else:
		return 1

y = int(input("Enter any number"))

print(factorial(y))
#print(factorial_better(y))