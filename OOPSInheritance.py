class parent:
    def abc(self):
        print("Hello")

class child(parent):
    def abc(self):
        print("World!")
        super().abc()
        

a = parent()
b = child()
a.abc()
b.abc()

