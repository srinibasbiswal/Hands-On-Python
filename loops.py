'''
Iteration is a process wherein a set of instructions or structures are repeated in a 
sequence a specified number of times or until a condition is met. 

A loop is used for iterating over a sequence.

'''
#for-loop
print("For loop for range from 1 - given and finding the sum")
n = int(input("Enter the range : "))
sum = 0
for i in range(1,n+1):
  print ("The value of i is",i)  
  sum = sum + i
print ("The value of sum is",sum)

print("\nFor loop for Range [1-9] with increment of 2")
for i in  range (1,10,2):
  print("The value of i is: ",i)

print("\nFor loop for Range [10-1] with decrement of 2")
for i in  range (10,0,-2):
  print("The value of i is: ",i)

#while-loop
print("\nFinding the sum from 1-5 using while loop")
i = 1
sum =0
while (i<=5):
  print ("The value of i is", i)
  sum=sum+i
  i=i+1
print("the value of sum is" ,sum)

print("\n To show the user input using while loop\n To exit type 0")
inp = int(input("Enter the input : "))
while (inp != 0):
  print("You have entered : ",inp)
  inp = int(input("Enter the value : "))
print("Exiting from loop . . .")




























