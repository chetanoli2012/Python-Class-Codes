import re

#s = "1234 3453 1343 hey there"
#match = re.search(r'\b\d\d\d\d\s\d\d\d\d\s\d\d\d\d\b',s)
#match2 = re.search(r'\b[\d]{4}\s[\d]{4}\s[\d]{4}\s\b',s)
#print(match2.group())
#print(match)
#print(match.group())

s2 = "h-ey@gmail.com ap-ple@yahoo.com aaaabbbb"
mat = re.findall(r'[\w\-+]+@[\w+]+.[\w+]',s2)
mat2 = re.findall(r'([\w\.-]+)+(@[\w\.]+)',s2)
print(mat)
print(mat2[0],mat2[1])
