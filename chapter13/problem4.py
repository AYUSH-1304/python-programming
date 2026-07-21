def divisibles5(n):
    if(n%5 == 0):
        return True
    return False
a = [1,2,34234,53,575,553,6775,7647540]

f = list(filter(divisibles5, a))
print(f)