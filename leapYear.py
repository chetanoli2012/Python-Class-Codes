import sys
def leap(x):
	if(x%4 == 0):
		if(x%100!=0):
			return "Leap\n"
		else:
			return "Not a leap\n"
	else:
		return "Not a leap\n"


x = int(sys.argv[1])
print(leap(x))