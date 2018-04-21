x = int(input())
if(x%2 == 0):
	if(x%3==0):
		print("Two and Three\n")
	elif(x%3!=0):
		print("Two\n")
elif(x%3 == 0):
	print("Three")
else:
	print("invalid")