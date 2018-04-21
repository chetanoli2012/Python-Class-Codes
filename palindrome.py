def palindrome(x,start,end):
	if(start>=end):
		return 1
	if(x[start] == x[end]):
		return palindrome(x, start+1, end-1)
	else:
		return 0


x = input("Enter the string\n")
if(palindrome(x, 0, len(x)-1)):
	print("Palindrome\n")
else:
	print("No\n")
