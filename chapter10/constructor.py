# class Employee:
#     language = "Python"
#     salary = 1200000

#     def __init__(self):    #dunder method which is automatically called
#         print("I am creating an object")


#     def getInfo(self):
#         print(f"The language is {self.language}. The salary is {self.salary}")
#     @staticmethod
#     def greet():
#         print("Good Morning")

# harry = Employee()
# harry.name = "Harry"
# print(harry.name, harry.salary)

# # Employee.getInfo(harry)
# rohan = Employee()





class Employee:
    language = "Python"
    salary = 1200000

    def __init__(self,name,salary,language): 
        self.name = name           #dunder method which is automatically called
        self.salary =salary
        self.language = language
        print("I am creating an object")


    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good Morning")

harry = Employee("Harry",1300000, "JavaScript")

print(harry.name, harry.salary,harry.language)

# rohan = Employee()
