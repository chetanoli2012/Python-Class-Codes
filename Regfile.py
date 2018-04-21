from sys import argv
import re

def find():
	script,filename = argv
	with open(filename,"r") as f:
		mat2 = re.findall(r'([\w\.-]+)+(@[\w\.]+)',f.read())
		print(mat2)
	
find()