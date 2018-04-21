'''from functools import reduce
print(reduce(lambda x,y: x*y, [1,2,3,4,5,6,7,8,9,10]))'''

import functools
print(functools.reduce(lambda x,y: x*y, [1,2,3,4,5,6,7,8,9,10]))
print(functools.reduce(lambda x,y: (x**2) + (y**2), [1,2,3,4]))
print(functools.reduce(lambda x,y: x+y,["hey","there"]))

