def maxx(x):
	max = x[0]
	for i in x:
		if(i>max):
			max = i
	return max

def minx(x):
	min = x[0]
	for i in x:
		if(i<min):
			min = i
	return min

def sumx(x):
	sum = 0
	for i in x:
		sum+= i
	return sum

x =[1,2,3,4]
print(maxx(x))
print(minx(x))
print(sumx(x))
