'''class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary)


e1 = Employee("Prateek",10000000)
e1.displayCount()
e1.displayEmployee()'''

class PartyAnimal:
   x= 0
   name =""

   def __init__(self , name):
      self.name = name 
      print(self.name , " constructed") 
   def party(self) :
      self.x +=1
      print(self.name," party count ", self.x)

s= PartyAnimal("Prateek")
s.party() 

j = PartyAnimal("Kritika")
j.party()
s.party()