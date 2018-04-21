def intersect(x,y):
	a = ()
	'''for i in x:
		if i in y:
			a+=(i,)'''
	for i in x:
		for j in y:
			if i == j:
				a+=(i,)
	return a


x = (1,2,3,4)
y = (3,4,5,6)
print(intersect(x,y))