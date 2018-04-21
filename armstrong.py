x = int(input())
temp = x
sum = 0
while(temp!=0):
	sum+= (temp%10)**3
	temp //= 10
if(sum == x):
	print("Armstrong\n")
else:
	 print("Nope! \n")