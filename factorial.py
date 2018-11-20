def factorials(x):
	i=1
	fact=1
	for m in range(x):
		fact=fact*i
		i=i+1
	print ("Factorial Value:" +str(fact))	
x=int(raw_input("Enter x: "))
factorials(x)
