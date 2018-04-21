def cList(x,y):
	c = []
	for i in x:
		if i in y:
			c.append(i)
	return c
				
def dList(x,y):
	c =[]
	for i in x:
		if i not in y:
			c.append(i)
	return c

	
x = [1,2,3,4,5]
y = [4,5,6,7,8]

print(cList(x,y))
print(dList(x,y))