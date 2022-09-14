#1.Create a class named Person, with firstname and lastname properties,and a printname method


'''
class Person:
    def __init__(self,fname,lname):
        self.fname=fname
        self.lname=lname
    def disp(self):
        print("Frist Name :",self.fname)
        print("Last Name :",self.lname)
p1=Person("Dastagiri","Goguvala")
p1.disp()
'''
##Output:
##Frist Name : Dastagiri
##Last Name : Goguvala


#2.Write a Python program to extract year, month, date and time using Lambda.
'''

import datetime
now=datetime.datetime.now()
year=lambda x:x.year
month=lambda x:x.month
day=lambda x:x.day
time=lambda x:x.time()
print(year(now))
print(month(now))
print(day(now))
print(time(now))

'''

##Output:
##2022
##9
##12
##16:53:52.488946

#3.Write a Python program to triple all numbers of a given list of integers.
## Use Python map.    
'''

ls=list(map(lambda x:x**3,[1,2,3,4,5]))
print(ls)

'''
##Output:
##[1, 8, 27, 64, 125]





















