x = input("Enter the string\n")
start,end = 0, len(x)-1
flag = 0
while(start<=end):
	if(x[start]!=x[end]):
		flag = 1
		break
	start+=1
	end-=1
if(flag ==0):
	print("Yeah\n")
else:
	print("Nah\n")
	