##1.what are literals?explain the types of literals?

'''
Literals in Python is defined as the raw data assigned to variables or constants while programming.
We mainly have five types of literals which includes string literals, numeric literals,
boolean literals, literal collections and a special literal None
'''


##2.Generate a Python list of all the even numbers between 4 to 30
'''
ls=[i for i in range(4,31) if i%2==0]
print(ls)
'''
##Output:[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]


##3..Create a function showEmployee() in such a way that it should accept employee name, and it’s salary
##and display both, and if the salary is missing in function call it should show it as 5000

class employee:
    def __init__(self,name,sal="5000"):
        self.name=name
        self.sal=sal
    def showemployee(self):
        print("Name : ",self.name)
        print("Salary : ",self.sal)
e1=employee("Kiran",25000)
e1.showemployee()
e2=employee("raju")
e2.showemployee()


##Output:
##Name :  Kiran
##Salary :  25000
##Name :  raju
##Salary :  5000
