def area():
	a =()
	r = int(input())
	a+=(r,)
	area = (22/7)*r*r
	format(area,'.2f')
	a+=(area,)
	return a

for i in range(1,3):
	print(area())
	#x = area()
	#print(x,"{0:.2f}".format(x))
	
