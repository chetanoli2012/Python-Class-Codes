def name(**kwargs):
    '''sname=""
    for i in kwargs.keys():
        sname+= kwargs[i];
    return sname'''
    
    '''for i in kwargs.keys():
        print(kwargs[i])'''
    for key,value in kwargs.items():
        print(key + "->" + value)
    
#print(name(fname = "Chetan",lname= " Oli"))
#print(name(fname="Chetan",mname=" Charles",lname=" Oli"))

#print(name(fname = "Chetan",lname= " Oli",fname2="Chetan",mname2=" Kumar",lname2=" Kumar"))

name(fname = "Chetan",lname= "Oli")
name(fname="Chetan",mname="Charles",lname="Oli")
