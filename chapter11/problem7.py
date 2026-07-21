class Vector:
    def __init__(self, l):
        self.l =l 
    def __len__(self):
        return len(self.l)

#Test the implementaton
v1 = Vector([1,2,3,5,4])
print(len(v1))


