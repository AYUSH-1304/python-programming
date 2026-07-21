from typing import List,Tuple, Dict,Union
n : int =5

name: str ="Harry"
# list of integer
number: List[int] =[1,2,3,4,5]

#tuple of a string and an integer
person: Tuple[str,int] = ("alice",30)

#dictionary with string key and integer value
scores: Dict[str, int] = {"Alice" :90, "Bob":50}

# union type for variable that can hold multiple value
identifier : Union[int ,str]= "ID123"
identifier = 12345 #also valid
def sum(a: int,b: int) -> int:
    return a+b


c= sum(5,6)
print(c)