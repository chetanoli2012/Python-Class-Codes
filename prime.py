import math

def prime(n):
	if(n == 0 or n==1):
		return 0
	flag = 0
	for i in range(2,n//2+1):
		if(n%i == 0):
			flag =1
			break
	if(flag == 0):
		return 1
	else:
		return 0
		
for a in range(100,500):
	if(prime(a)):
		print(a)