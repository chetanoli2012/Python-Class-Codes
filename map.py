def sqr(x):
	return x**2
	
def cube(x):
	return x**3
	
l = list(map(sqr,[2,3,4]))
l2 = list(map(pow,[10,100],[2,3]))
print(l)
print(l2)
print();
func = [sqr,cube]
for r in range(10):
	l3 = list(map(lambda x: x(r),func))
	print(l3)

# l4 = list(map([1,2,3],func))
# print(l4)



