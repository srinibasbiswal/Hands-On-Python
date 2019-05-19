# Index starts from 0
list1 = [1 ,5 ,10.0 , "python","ok"]
str = "python"
tuple1 = (10,50,"String1",100.0,"Hello")

# parsing and changing list
print("\nParsing and changing value of list")
for i in list1:
  print ("The value in list1 is : ",i)

print("The value of the 3rd index in the list is : ",list1[3])
print("The value of the -1 index in the list is : ",list1[-1])

print("Before Changing the value of list : ",list1)
list1[1] = 1212 #changed the value of 1st index of the list to 1212
print("After Changing the value of list : ",list1)



# Parsing and changing string
print("\nParsing and changing value of string")
for i in str:
  print ("The character of the string is ",i)
print("The value of the 3rd index in the string is : ",str[3])
print("Before Changing the value of string : ",str)
str = "Hello World"#changed the value of str to hello world
print("After Changing the value of string : ",str)


# Parsing the tuple
print("\nParsing the value of tuple")

for i in list1:
  print ("The value in tuple1 is : ",i)

print("The value of the 3rd index in the tulpe is : ",tuple1[3])
print("The value of the -1 index in the tuple is : ",tuple1[-1])
