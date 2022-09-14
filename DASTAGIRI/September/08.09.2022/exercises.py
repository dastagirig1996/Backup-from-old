##1.create the class to display person name and age?
'''
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def show(self):
        print("Name : ",self.name)
        print("Age : ",self.age)
s1=Student("kiran",25)
s1.show()
'''
##Output:
##Name :  kiran
##Age :  25

##2.Write a Python class to reverse a string word by word. 
##Input string : 'hello .py'
##Expected Output : '.py hello'
'''
st="hello .py"
ls=st.split()
st1=" ".join(reversed(ls))

print(st1)
'''
##Output:
##.py hello


##3.write a program for multilevel inhertance.

class Grand_Parent():
    def m1(self):
        print("Iam in grand parent method")

class Parent(Grand_Parent):
    def m2(self):
        print("Iam in Parent method")
class Child(Parent):
    def m3(self):
        print("Iam in child method")
        
c1=Child()
c1.m3()
c1.m2()
c1.m1()
p1=Parent()
p1.m2()
p1.m1()
GP1=Grand_Parent()
GP1.m1()
Gp1.m2()


##Output:
##Iam in child method
##Iam in Parent method
##Iam in grand parent method
##Iam in Parent method
##Iam in grand parent method
##Iam in grand parent method
##Traceback (most recent call last):
##  File "D:/DASTAGIRI/September/08.09.2022/exercises.py", line 53, in <module>
##    Gp1.m2()
##NameError: name 'Gp1' is not defined



















