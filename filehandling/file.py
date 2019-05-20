'''
File is a named location on disk to store related information.
It is used to permanently store data in a non-volatile memory.
'''

# To open and read a file

# To read the whole file using read()
print("To open a file in Read mode and read whole file")
fp = open("myFile.txt","r")
line = fp.read()
print("The lines in the file are : ")
print(line)
fp.close()

# To read the file line by line
print("\nTo open a file in Read mode and read line by line")
fp = open("myFile.txt","r")
print("The lines in the file are : ")
line = fp.readline()
print(line)
while line:
  line = fp.readline()
  print(line)
fp.close()

# To read the file lby whole lines at a time
print("\nTo open a file in Read mode and read all lines")
fp = open("myFile.txt","r")
print("The lines in the file are : ")
lines = fp.readlines()
for line in lines:
  print(line)
fp.close()


# To open a file in append mode
print("\nTo open a file in Append mode and add lines at the end")
#read data before appending
print("Data before appending")
fp = open("myFile.txt","r")
lines = fp.read()
print(lines)
fp.close()

# Append data
fp = open("myFile.txt","a")
linesToAdd = ["First line appended","Second Line appended"]
for line in linesToAdd:
  fp.write(line)
fp.close()

# Read data after appending
print("Lines after appending")
fp = open("myFile.txt","r")
lines = fp.read()
print(lines)
fp.close()


# To open file in Write mode
print("\nTo open a file in Write mode and write data in the file")
#read data before writing
print("Data before Writing")
fp = open("myFile.txt","r")
lines = fp.read()
print(lines)
fp.close()

# write data in file
fp = open("myFile.txt","w")
linesToAdd = ["First line written","Second Line written"]
for line in linesToAdd:
  fp.write(line)
fp.close()

# Read data after writing
print("Lines after writing")
fp = open("myFile.txt","r")
lines = fp.read()
print(lines)
fp.close()





