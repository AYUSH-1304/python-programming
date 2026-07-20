class Employee:
    language = "Python"
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee()
# harry.language = "Javascript" #This is an instance attribute
harry.greet()
harry.getInfo()

# Employee.getInfo(harry)