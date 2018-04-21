def duplicates(a):
	c=[]
	for e in a:
		if e not in c:
			c.append(e)
	return c
	

a=[2,3,3,3,3,4]
print(duplicates(a))