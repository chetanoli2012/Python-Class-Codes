def findratio(a,b):
    j = 0
    c = []
    for i in a:
        try:
            val = i/b[j]
            j=j+1
            c.append(val)
        except ZeroDivisionError:
            c.append("nan")
            j=j+1
    return c
            
a = [2,4,6,8]
b = [2,0,3,4]
print(findratio(a,b))
