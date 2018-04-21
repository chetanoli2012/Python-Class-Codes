from sys import argv
import re

def find():
	script,filename = argv
	with open(filename,"r") as f:
		#mat2 = re.findall(r'[\d]{10}',f.read())
		mat = re.findall(r'\b[a-z,A-Z]+\b',f.read())
		
		#print(mat2)
		print(mat)
		#print(mat3)
	
find()