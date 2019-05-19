'''
 Scope of a variable is the portion of a program where the variable is recognized.
 Lifetime of a variable is the period throughout which the variable exists in the memory. The lifetime of variables inside a function is as long as the function executes.
'''

def varLife(x):
  var1 = 10
  print("Value of x is ", x)

varLife(20)
print("Value of var1 is ",var1)

'''
We are able to print the value of x but not able to print the value of var1
'''