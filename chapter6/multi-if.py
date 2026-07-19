a = int(input("Enter your Age:")) 

#If statement no.1
if(a%2 == 0):
    print("a is even")
#if statement end1

#if statement no 2

if(a>=18):
    print("You are above the age of content")
    print("Good for you")
elif(a<0):
    print("You are entering an invalid negative age")
elif(a==0):
    print("You are entering 0 which is not a valid age")
else:
    print("You are below the age of content")

#end of 2 ifS

print("End of Program")