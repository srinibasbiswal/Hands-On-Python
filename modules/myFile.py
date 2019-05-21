# Modules refer to a file containing Python statements and definitions.
# This is the main file where module is imported

import myModule

input = input("Enter your Name : ")
myModule.printName(input)

print("The value of var1 from the module is : ",myModule.var1)
print("The value of var2 from the module is : ",myModule.var2)