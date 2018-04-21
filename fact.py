import sys

def fact(n):
	if(n==1):
		return 1
	return n*fact(n-1)

n = int(sys.argv[1])
print(fact(n))