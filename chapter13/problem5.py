from functools import reduce
l = [1,2,34234,53,575,553,9996775,7647540]

def greater(a,b):
    if(a>b):
        return a
    return b

print(reduce(greater ,l))