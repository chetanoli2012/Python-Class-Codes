class employee:
    companyname = "University"
    def __init__(self,eid,ename):
        self.eid = eid
        self.ename = ename
        
    def displayname(self):
        print(" ",self.ename)

    def displayid(self):
        print(" ",self.eid)

e1 = employee(123,"Chetan")
e1.displayname()
e1.displayid()
e2 = employee(456,"Manil")
e2.companyname = "Chitkara"
print(e1.companyname)
print(e2.companyname)

