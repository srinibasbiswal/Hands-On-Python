# Function is a group of related statements that perform a specific task.

# Syntax :
'''
def function_name(parameters):
  """docstring"""
  statement(s) 
'''

# Funtion to add two numbers : 

# Predefined
def addNumbers() :
  result = 10 + 20
  return result

# Add any two numbers :
def addAnyNumbers(x,y):
  result = x + y
  return result

ans1 = addNumbers()
print("The sum of 10 and 20 is : ", ans1)

num1 = int(input("Enter First Number : "))
num2 = int(input("Enter Second Number : "))
ans2 = addAnyNumbers(num1,num2)
print("The sum of ",num1," and ",num2, " is : ",ans2)