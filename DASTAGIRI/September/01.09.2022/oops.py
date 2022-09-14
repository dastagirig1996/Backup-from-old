##1. Create a Class with instance attributes 
'''
class employee:
    def __init__(self,name,sal):
        self.name=name
        self.sal=sal
'''        


##2. Write a Program to create a class by name Students, and initialize attributes like
        ## name, age, and grade while creating an object. 
'''
class students:
    def __init__(self,name,age,grade):
        self.name=name
        self.age=age
        self.grade=grade
    def display(self):
        print("name : ",self.name,"Age : ",self.age,"grade : ", self.grade)
s1=students("Sai",25,"C")
s1.display()
'''
##Output:
##name :  Sai Age :  25 grade :  C



##3. Write a Program to create an empty valid class by name Students, with no properties 

'''
class students:
    pass
s1=students()
s1.name="somu"
print("Name",s1.name)
'''


##4. Write a program that prints the class name using its object. 





##5.Write a program, to create a child class Teacher that will inherit the properties of Parent class Staff 

'''
class staff:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class teacher(staff):
    def __init__(self,name,age,sal):
        self.sal=sal
        super().__init__(name,age)

    def Show(self):
        print("name :",self.name)
        print("age :",self.age)
        print("salary :",self.sal)
        
t1=teacher("ramu",25,25000)
t1.Show()
'''

##Output:
##name : ramu
##age : 25
##salary : 25000


##6. Create a Vehicle class without any variables and methods 

class vehicle:
    pass



##7.Create a child class Bus that will inherit all of the variables and methods of the Vehicle class 
'''
class vehicle:
    def __init__(self,fuel,wheels):
        self.fuel=fuel
        self.wheels=wheels
    def drive(self):
        print("Fuel used :",self.fuel)
        print("wheels have :",self.wheels)
class Bus(vehicle):
    def __init__(self,fuel,wheels):
        super().__init__(fuel,wheels)
    def show(self):
        super().drive()

b1=vehicle("petrol",2)
b1.drive()

b2=Bus("Diesel",4)
b2.show()
b2.drive()
'''


##Output:
##Fuel used : petrol
##wheels have : 2
##Fuel used : Diesel
##wheels have : 4
##Fuel used : Diesel
##wheels have : 4

##8. Define a property that must have the same value for every class instance (object) 
'''
class admin:
    company="Ojas"
    def __init__(self,name,grade):
        self.name=name
        self.grade=grade
s1=admin("Kiran","B")

print(s1.name,s1.grade,admin.company)
print(s1.name,s1.grade,s1.company)

'''
##Output:
##Kiran B Ojas
##Kiran B Ojas

##9. Check type of an object 

'''
class staff:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class teacher(staff):
    def __init__(self,name,age,sal):
        self.sal=sal
        super().__init__(name,age)

    def Show(self):
        print("name :",self.name)
        print("age :",self.age)
        print("salary :",self.sal)
        
t1=teacher("ramu",25,25000)
t1.Show()
print(type(t1))
'''

##Output:
##name : ramu
##age : 25
##salary : 25000
##<class '__main__.teacher'>



##10. Write a Python program that checks if one class is a subclass of another? 


'''
class vehicles:
    def __init__(self):
        print("all vehicles")

class bus(vehicles):
    def __init__(self):
        vehicles.__init__()
    
    
print(issubclass(bus,vehicles))
print(issubclass(vehicles,bus))
print(issubclass(bus,list))
print(issubclass(bus,(list,vehicles)))
print(issubclass(bus,bus))
'''


##Output:
##True
##False
##False
##True
##True



##11. Determine if School_bus is also an instance of the Vehicle class 
'''
class vehicles:
    def __init__(self,name,milage,capacity):
        self.name=name
        self.milage=milage
        self.capacity=capacity
class bus(vehicles):
    pass

school_bus=bus("school_volvo",25,100)
print(isinstance(school_bus,vehicles))
'''

##Output:
##True


##12. Write a program to build a simple Student Management System using Python which can perform the following operations: 

##Accept – This method takes details from the user like name, roll number, and marks for two different subjects 
##
##Display – This method displays the details of every student. 
##
##Search – This method searches for a particular student from the list of students. This method will ask the user for roll number and then search according to the roll number 
##
##This method deletes the record of a particular student with a matching roll number 
##
##Update – This method updates the roll number of the student.
##This method will ask for the old roll number and new roll number.
##It will replace the old roll number with a new roll number. 



# This is simplest Student data management program in python
 
# Create class "Student"
class Student:
 
  # Constructor
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2
 
    # Function to create and append new student
    def accept(self, Name, Rollno, marks1, marks2):
   
  # use ' int(input()) ' method to take input from user
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)
 
    # Function to display student details
    def display(self, ob):
        print("Name : ", ob.name)
        print("RollNo : ", ob.rollno)
        print("Marks1 : ", ob.m1)
        print("Marks2 : ", ob.m2)
        print("\n")
 
    # Search Function
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i
 
    # Delete Function
    def delete(self, rn):
        i = obj.search(rn)
        del ls[i]
 
    # Update Function
    def update(self, rn, No):
        i = obj.search(rn)
        roll = No
        ls[i].rollno = roll
 
 
# Create a list to add Students
ls = []
# an object of Student class
obj = Student('', 0, 0, 0)
 

print("\n1.Accept Student details\n2.Display Student Details\n3.Search Details of a Student\n4.Delete Details of Student\n5.Update Student Details\n6.Exit")
 
# ch = int(input("Enter choice:"))
# if(ch == 1):
obj.accept("A", 1, 100, 100)
obj.accept("B", 2, 90, 90)
obj.accept("C", 3, 80, 80)
 
# elif(ch == 2):
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):
    obj.display(ls[i])
 
# elif(ch == 3):
print("\n Student Found, ")
s = obj.search(2)
obj.display(ls[s])
 
# elif(ch == 4):
obj.delete(2)
print(ls.__len__())
print("List after deletion")
for i in range(ls.__len__()):
    obj.display(ls[i])
 
# elif(ch == 5):
obj.update(3, 2)
print(ls.__len__())
print("List after updation")
for i in range(ls.__len__()):
    obj.display(ls[i])
 
# else:
print("Thank You !")
















##How to create a list of object in Python class 
##
##Python Program to Get the Class Name of an Instance 
##
 

 
