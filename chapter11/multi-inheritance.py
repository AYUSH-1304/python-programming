class Employee:
    company = "ITC"
    name = "Default name"
    def show(self):
        print(f"The name is the Employee is {self.name} and the company is {self.company}")

class Coder:
    language = "Python"
    def printLanguage(self):
        print(f"Out of all the language here is your language: {self.language}")

class Programmer(Employee, Coder):
    company = "ITC Infotech"
    def showLanguage(self):
        print(f"The name is{self.name} and he is good with {self.language} language")




a = Employee()
b = Programmer()

b.show()
b.printLanguage()
b.showLanguage()

print(a.company,b.company)