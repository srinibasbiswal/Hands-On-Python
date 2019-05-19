# An argument of a function is a specific input to the function.

# Funtion for Required Arguments :
def reqargsAdd(x , y):
  print("\n Default Required Function")
  print ("the value of x  : ",x)
  print ("the value of y  : ",y)
  result = x + y
  return (result)

# Funtion for Keyword Arguments :
def keywordargsAdd(x , y):
  print("\n Default Keyword Function")
  print ("the value of x  : ",x)
  print ("the value of y  : ",y)
  result = x + y
  return (result)

# Funtion for Default Arguments :
def defaultargsAdd(x = 10 , y = 20):
  print("\n Default Argument Function")
  print ("the value of x  : ",x)
  print ("the value of y  : ",y)
  result = x + y
  return (result)

# Funtion for Arbitary Arguments :
def arbitaryargsAdd(*args):
  print("\n Arbitary Argument Funtion \n values : ")
  result = 0
  for i in args:
    print(i)
    result = result + i
  return result

input1 = int(input("Enter the first number : "))
input2 = int(input("Enter the second number : "))

# For Required Arguments :
answer = reqargsAdd(input1 , input2) # Try giving 1 argument instead of 2
print ("The result of Required Argument function is : ",answer)

# For KeyWord Arguments : 
answer = keywordargsAdd(x = input2 , y = input1) # Try changing the value of x and y
print ("The result of keyword argument funtion is : ",answer)

#For Default arguments : 
answer = defaultargsAdd(input1) # If no value of given for arg then the default value will be taken
print ("The result of Default argument funtion is : ",answer)

# For Arbitary Arguments : 
answer = arbitaryargsAdd(input1, input2, 12, 20) # You can give any number of arguments (It must be minimum 1)
print("the result of Arbitary argument function is : ",answer)

