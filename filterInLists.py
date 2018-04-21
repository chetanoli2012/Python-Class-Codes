l1 = [1,2,3,4,5]
l2 = [4,5,6,7,8]

l3 = list(filter(lambda x:x in l1,l2))
print(l3)

l4 = list(filter(lambda x:x not in l2, l1))
print(l4)

l5 = l1 + list(filter(lambda x:x not in l1, l2))
print(l5)

'''l0 = [];
l6 = list(filter(lambda x,y: x not in l0,l1, y not in l0,l2))
print(l6)'''