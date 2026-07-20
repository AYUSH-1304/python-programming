class Employee:      #This is a class attributes
    language = "python"
    salary = 122000

harry = Employee()
harry.name = "Harry"  #This is an object attribute
print(harry.name,harry.language,harry.salary)

Rohan = Employee()
Rohan.name = "Rohan"
print(Rohan.name,Rohan.language,Rohan.salary)

#Here name is object attribute and salary and language are class attributes as they directly belong to the class
