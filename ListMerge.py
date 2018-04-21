def merge(x,y):
	c = []
	for i in x:
		c.append(i)
	for j in y:
		if(j not in c):
			c.append(j)
	return c

def mergex(x,y):
	c = []
	for i in x:
		for j in y:
			if(i not in c):
				c.append(i)
			elif (j not in c):
				c.append(j)
	return c

x = [1,1,2,3]
y = [2,3,4]
print(merge(x,y))
print(mergex(x,y))