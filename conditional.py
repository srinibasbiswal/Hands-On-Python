# Conditional statements help in control flow of the code

number = int(input("Enter a number : "))

#if statement
if(number%2 == 0):
  print(number," is an even number")

#if-else statement
if (number%2 == 0):
  print (number," is an Even number")
else:
  print(number," is an odd number")

#nested-if
if (number%2 == 0):
  if (number%3 == 0):
    print(number," is divisible by 6")
  else:
    print(number," is not divisible by 6")
else:
  print(number," is not divisible by 6")

#if-elif-else statement
grade = input("Enter a grade ( \"A\" , \"B\" or \"C\" ) : ")
if (grade == "A"):
  print("Your Grade is ",grade)
elif (grade == "B"):
  print("Your Grade is ",grade)
else:
  print("Your Grade is ",grade)



