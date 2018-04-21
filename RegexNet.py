import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com
321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
pat
bat
'''

sentence = 'Start a sentence and then bring it to an end'
#print("\tTab")
#print(r"\tTab")
##pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
##pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')
##pattern = re.compile(r'[89]00[-.]\d\d\d[.-]\d\d\d\d')
##pattern = re.compile(r'[a-zA-z][a-zA-Z]')
##pattern = re.compile(r'[^a-zA-Z]')
##pattern = re.compile(r'[^b][a][t]')
##pattern = re.compile(r'\d{3}.\d{3}.\d{4}')
##pattern = re.compile(r'M[r]?[s]?\.?\s[A-Z]\w*')
##pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')

pattern = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*')
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)

##print(text_to_search[1:4])
##
##with open('RegData.txt','r') as f:
##    contents = f.read()
##    matches = pattern.finditer(contents)
##    for match in matches:
##        print(match)



