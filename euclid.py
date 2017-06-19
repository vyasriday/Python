def euclid(m,n):
	if(m>n):
		
		if(m%n==0):

			return n

		else:

			euclid(n,m%n)
	elif(n>m):

		p= m
		m= n
		n= p
		euclid(m,n)

	else:
		return m


		

