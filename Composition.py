class calc1:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def add(self):
        return self.x + self.y

    def sub(self):
        return self.x-self.y

class calc2:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def multiply(self):
        return self.x*self.y

    def divide(self):
        return self.x/self.y

class calc3:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.c1 = calc1(x,y)
        self.c2 = calc2(x,y)

    def power(self):
        return self.x**self.y

    def multiply(self):
        return self.c2.multiply()

    def divide(self):
        return self.c2.divide()

    def add(self):
        return self.c1.add()

    def sub(self):
        return self.c1.sub()

c = calc3(4,5)
print(c.multiply())
print(c.divide())
print(c.add())
print(c.sub())

        
