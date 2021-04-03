# Creating a simple calculator using Object Oriented Programming (OOPS)
class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print('Add:', self.a + self.b)
    def sub(self):
        print('Sub:', self.a - self.b)
    def mul(self):
        print('Mul:', self.a * self.b)
    def div(self):
        print('Div:', self.a / self.b)
    def mod(self):
        print('Mod:', self.a % self.b)
print("\033[0;32;40m|===================================|")
calc = calculator(int(input("Enter 1st Number: ")), int(input("Enter 2nd Number: ")))
print("|===================================|")
calc.add()
calc.sub()
calc.mul()
calc.div()
calc.mod()
print("\033[3;34;47m|===================================|")