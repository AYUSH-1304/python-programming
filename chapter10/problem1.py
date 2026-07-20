class Programmer:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name =name
        self.salary =salary
        self.pin = pin

p = Programmer("Harry", 1200000, 2347789)
print(p.name, p.pin, p.company ,p.salary)

r = Programmer("Karry", 1203000, 2547789)
print(r.name, r.pin, r.salary, r.company)