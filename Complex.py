class complex:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def print(self):
        #print(self.x,"+",self.y,"i",sep='')
        print("{0}+{1}i".format(self.x,self.y))
        
c = complex(3,4)
c.print()
