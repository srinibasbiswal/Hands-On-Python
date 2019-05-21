'''
Class − A user-defined prototype for an object that defines a set of attributes that characterize any object of the class. 
The attributes are data members (class variables and instance variables) and methods, accessed via dot notation.

Object − A unique instance of a data structure that's defined by its class. 
An object comprises both data members (class variables and instance variables) and methods.
'''

class Employee:
   'Common base class for all employees'
   empCount = 0

   # constructor : runs when a new object is created
   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      self.empCount += 1
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % self.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)

class csec:
   sec = "c"
   branch = "cse"
   cllg = "NIT"
   
   def printdetails(self):
      print("My class is CSE-C")

"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

#Displat details of emp1
emp1.displayEmployee()
#Displat details of emp2
emp2.displayEmployee()
emp1.displayCount()
emp2.displayCount()
print ("Total Employee %d" % Employee.empCount)


stud1 = csec() # create an object of csec
print(stud1.cllg) # print cllg of object stud1
stud1.printdetails() # print details of stud1

stud2 = csec() # create an onject of csec
stud2.printdetails() # print details of object stud2