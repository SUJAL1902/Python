'''
Define a class Student with data members name and age.
Implement both a default constructor and a parameterized
constructor. Also, define a destructor that prints a message when an
object is destroyed.
'''

class student:
    def __init__(self):
        self.name = "Vivek"
        self.age = 18
    
    def __details__(self , name , age):
        self.name = name
        self.age = age

    def display (self):
        print("Name : ",self.name)
        print("Age : ", self.age)

s = student()
print('==================================================')
s.__init__()
s.display()
print('==================================================')
s.__details__('Sujal',21)
s.display()

