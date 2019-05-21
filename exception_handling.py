'''
An exception is an error that happens during execution of a program. When that error occurs, 
Python generate an exception that can be handled, which avoids your program to crash.
'''

# If we print the value of x without declaring it then we will get error.
# This error is handled by exception handling

#uncomment the below line to see the error
# print(x)

# try-except
print("The result of try-except")
try:
  print(x)
except:
  print("Some Error Occured")

print("\nThe result of try-except with specific error")
try:
  print (x)
except NameError:
  print("Declare the variable first")

# try-except-else
print("\nThe result of try-except-else with error")
try:
  print (x)
except:
  print("Error Occured")
else:
  print("No Error Occured")

print("\nThe result of try-except with no error")
try:
  print ("Hello")
except:
  print("Error Occured")
else:
  print("No Error Occured")

# try-except-finally
print("\nThe result of try-except-finally with error")
try:
  print(x)
except:
  print("Error Occured")
finally:
  print("this is the final statement after error occured")

print("\nThe result of try-except-finally with no error")
try:
  print("Hello world")
except:
  print("Error Occured")
finally:
  print("this is the final statement after no error occured")