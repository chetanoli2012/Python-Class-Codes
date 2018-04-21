def max(x):
	first,second = -99,-99
	for i in x:
		if i>first:
			first = i
			second=first
		if (i>second and i!= first):
			second = i
	print(first)
	print(second)

x= [1,1,1,1,2,1,1,1,5,5,5]
max(x)