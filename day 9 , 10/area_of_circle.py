'''
Create a class to calculate Area of circle with one data member
to store the radius and another to store area value.
Create method members
1. init - to input radius from user
2. calc - to calculate area
3. display- to display area
'''

class Area:
    def __init__(self,a):
        self.a=a
    def __calc__(self):
        self.area=2*3.14*self.a
    def __display__(self):
        print(self.area)
A1=Area(3)
A1.__calc__()
A1.__display__()