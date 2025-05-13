'''
Create a class MathOperation with two data member X and Y to
store the operand and third data member R to store result of
operation.
Create method members
1. init - to input X and Y from user
2. add - to add X and Y and store in R
3. multiply - to multiply X and Y and store in R
4. power - to calculate X Y and store in R
5. display- to display Result R
'''

class MathOperation:
    def __init__(self):
        self.X = 0
        self.Y = 0
        self.R = 0

    def init(self):
        self.X = float(input("Enter value for X: "))
        self.Y = float(input("Enter value for Y: "))

    def add(self):
        self.R = self.X + self.Y

    def multiply(self):
        self.R = self.X * self.Y

    def power(self):
        self.R = self.X ** self.Y

    def display(self):
        print("Result (R):", self.R)


if __name__ == "__main__":
    op = MathOperation()
    op.init()
    
    op.add()
    op.display()
    
    op.multiply()
    op.display()
    
    op.power()
    op.display()
