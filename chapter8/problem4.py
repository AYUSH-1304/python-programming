'''
sum(1) = 1
sum(2) =1+2
sum(n) = 1+2+3+....+n
sum(n) =sum(n-1)+n1
'''

def sum(n):
    if(n==1):
        return 1
    return sum(n-1)+n

n= int(input("Enter the value:"))
print(sum(n))