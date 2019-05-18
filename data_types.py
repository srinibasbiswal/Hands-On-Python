# Syntax to declare a variable : 
# var_name = value

x = 10 # here x is a variable and 10 is the value

# Types of Data Types :

# Numeric :
# integer
a = 10
print ("The value of a is ",a," and it is of type ",type(a))
# float
b = 10.5
print ("The value of b is ",b," and it is of type ",type(b))
# complex
c = 5 + 10j
print ("The value of c is ",c," and it is of type ",type(c))

# String :
str1 = "Python"
print ("The value of str1 is ",str1," and it is of type ",type(str1))
str2 = 'Python Programming'
print ("The value of str2 is ",str2," and it is of type ",type(str2))
str3 = '''Python
Programming is fun.'''
print ("The value of str3 is ",str3," and it is of type ",type(str3))

# List :
list1 = [1, 2, 3]
print("The value of list1 is ",list1," and it is of type ",type(list1))
list2 = [1, 5.0, "python"]
print("The value of list2 is ",list2," and it is of type ",type(list2))

# Tuple :
tuple1 = (4, 5, 6)
print("The value of tuple1 is ",tuple1," and it is of type ",type(tuple1))
tuple2 = (10, 15.0, "python programming")
print("The value of tuple2 is ",tuple2," and it is of type ",type(tuple2))

# Dictionary :
dict1 = {"key1" : "value1" , "key2" : "value2", "key3" : 3}
print("The values in dict are")
for i in dict1.keys():
  print("{ ",i," : ",dict1.get(i)," }")
print("the type of dict1 is : ",type(dict1))


