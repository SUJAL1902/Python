'''
Write a class Rectangle that uses constructor initialization lists
to set the values of width and height. The constructor should
initialize the dimensions of the rectangle, and then you can print
the area of the rectangle.
'''

class Area:
    def __init__(self):
        self.len = 0
        self.bre = 0
    def init (self) :
        self.len = float(input("Enter value of lenegth : "))
        self.bre = float(input("Enter value of breadth : "))

    def __calc__(self):
        self.area = self.len * self.bre

    def __display__(self):
        print(self.area)
A1 = Area()
A1.__init__()
A1.init()

A1.__calc__()
A1.__display__()