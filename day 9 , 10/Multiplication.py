'''
Create a class MathOperation containing method ‘multiply’ to
calculate multiplication
of following arguments.
a. two numbers
b. three numbers
'''

class multiple :
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.r = 0
    def init (self):
        integer_list = list(map(int, input("Enter integers separated by spaces: ").split()))
        self.x = float(input("Enter value for X : "))
        self.y = float(input("Enter value for Y : "))
        self.z = float(input("Enter value for z : "))
    def multi(self) :
        self.r = self.x * self.y

    def multi2(self) :
        self.r = self.x * self.y * self.z 
    
    def display(self):
       print("Multi is ",self.r)

m = multiple()
m.__init__()
m.init()

m.multi()
m.display()

m.multi2()
m.display()