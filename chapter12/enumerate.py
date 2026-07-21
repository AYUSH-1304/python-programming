l = [3,432,654,54,45]

# index = 0 
# for item in l:
#     print(f"The item number {index} is {item}")
#     index += 1

#This can be simplified using enumerate function

for index, item in enumerate(l):
    print(f"The item number {index} is {item}")