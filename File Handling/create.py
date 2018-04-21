with open("first.txt","w+") as f:
    f.write("Hey there, this is the test file file.\n")
    f.write("Hey there, this is the test file file.\n")
    f.write("Hey there, this is the test file file.\n")
    f.write("Hey there, this is the test file file.\n")
    f.seek(0)
    #print(f.read())
    #print(s)
    #f.append("\nThis is the second line bro!")
    #f.seek(0)
    #print(f.read())
    #print(s)
    f.close()
    

with open("first.txt","r") as f2:
    '''z = f2.read()
    s = z.split('\n')
    print(s)'''
    count = 0
    for line in f2.readlines():
        count += 1
        print(line)
    print("Number of lines = ", count)

    count2 = 0
    f2.seek(0)
    z = f2.readlines()

    q=[]
    for a in z:
        q = q + a.split()
    
    print(len(q))    
    print(q)

    f2.seek(0)
    temp = f2.read()
    count3 = 0;
    for item in temp:
        if(item!=" " and item!="\n" and item!="." and item!=","):
            count3+=1
    print(count3)

    f2.seek(0)
    temp2 = f2.read()
    d={}
    for char in temp2:
        if(char!=" " and char!="\n" and char!="." and char!=","):
            if char in d:
                d[char]+=1
            else:
                d[char] = 1
    for k,v in d.items():
        print(k,"--->",v)
    print(d)
            



    
    
