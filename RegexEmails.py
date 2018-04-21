import re

emails = '''
CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net
'''

##pattern = re.compile(r'(C|c)\w+([A-Z][A-Z]|\.|-)(\w+|\d{3})[-]?\w+?@\w+[-]?\w+?.\w{3}')
##pattern = re.compile(r'[a-zA-Z0-9.-]+@[a-zA-Z-]+\.\w{3}')
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(emails)

for match in matches:
    print(match)
