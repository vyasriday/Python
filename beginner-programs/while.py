h = 5
while h>0:

	print("This is a fucking loop")
	h-=1



while True:
	response = int(input("Enter a number"))
	if response%5==0:
		print("Number is divisible by 5")

	elif response%2==0:
		print("Number is divisible by 2")

	else:
		break
