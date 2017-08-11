def factorial():
	x = Number(input("Enter a number"))
	if(x==1):
		return x
	else:
		return x*factorial(x-1)

print("Factorial is " , factorial())
