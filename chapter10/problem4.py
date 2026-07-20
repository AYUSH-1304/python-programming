class Calculator:
    def __init__(self, n):
        self.n = n
    def square(self):
        print(f"The square is {self.n*self.n}")
    def cube(self):
        print(f"The square is {self.n*self.n*self.n}")
    def squareroot(self):
        print(f"The square is {self.n**1/2}")
    @staticmethod
    def hello():
        print("Hello there!")

n = int(input("Enter the no:"))
a = Calculator(n)
a.hello()
a.square()
a.cube()
a.squareroot()