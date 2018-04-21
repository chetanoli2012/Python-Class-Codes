class shape:
    def __init__(self,n):
        self.n = n
        self.dimension =[int(input()) for i in range(n)]
    def printing(self):
        print(self.dimension)
        
class rect(shape):
    def __init__(self):
        super().__init__(2)
    def area(self):
        l = self.dimension[0]
        b = self.dimension[1]
        print(l*b)

class triangle(shape):
    def __init__(self):
        super().__init__(2)
    def area(self):
        l = self.dimension[0]
        b = self.dimension[1]
        print(l*b*0.5)

class square(shape):
    def __init__(self):
        super().__init__(1)
    def area(self):
        l = self.dimension[0]
        print(l*l)

r = triangle()
r.printing()
r.area()
