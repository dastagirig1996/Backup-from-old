##1. Write a Python program to get the top three items in a shop. Go to the editor
##Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
##Expected Output:
##item4 55
##item1 45.5
##item3 41.3

'''
def dictionary(d):
    key_list=list(d.values())
    key_list.sort(reverse=True)
    key_list=key_list[:3]
    for i in key_list:
        for j in d.keys():
            if d[j]==i:
                print(j,i)

dic={'item1': 45.50,  'item3': 41.30, 'item4':55,'item2':35, 'item5': 24}
dictionary(dic)
'''
##Outout:
##item4 55
##item1 45.5
##item3 41.3



##2.Write a Python program to print a dictionary line by line
##if input   ===students = {'Anil':{'class':'ix',
##        'rolld_id':56},
##        'dasta':{'class':'x',
##        'roll_id':83}}
##
##op/=Anil                                                                                                           
##class : ix                                                                                                     
##rolld_id : 56                                                                                                  
##dasta                                                                                                         
##class : x                                                                                                     
##roll_id : 83 
'''
students = {'Anil':{'class':'ix','rolld_id':56},
           'dasta':{'class':'x','roll_id':83}}

for i,j in students.items():
    print(i)
    for k,l in j.items():
        print(str(k)+":"+str(l))
'''
#Output:
##Anil
##class:ix
##rolld_id:56
##dasta
##class:x
##roll_id:83



##3.Write a Python program to check multiple keys exists in a dictionary.?
'''
dic={'item1': 45.50,  'item3': 41.30, 'item4':55,'item2':35, 'item5': 24}


s=0
for i in dic.keys():
    s=s+1
    
    
if s<1:
    print("No data found")
elif s==1:
    print("1 key found")
else:
    print("Multiple keys found")
'''
##Output:
##Multiple keys found

##4.what is Abstraction in python give some example programetically.?

'''
from abc import ABC,abstractmethod

class Car(ABC):
    @abstractmethod
    def structure(self):
        pass

class Engine(Car):
    def structure(self):
        print("Engine was implemented")

e1=Engine()
e1.structure()
'''

#Output:
##Engine was implemented



##5.what is inheritance give an example(write fibonacci seriese example using constrocter).?

'''
class Solve:
    def __init__(self,n1,n2,le):
        self.le=le
        self.n1=n1
        self.n2=n2
class Fibb(Solve):
    def find(self):
        super().__init__(self.n1,self.n2,self.le)
        while self.le>0:
            print(self.n1)
            nexte=self.n1+self.n2
            self.n1=self.n2
            self.n2=nexte           
            self.le=self.le-1
f1=Fibb(0,1,8)
f1.find()

'''

#Output:
##0
##1
##1
##2
##3
##5
##8
##13




##6.take set of element and again take list of element then check how many element
##of list present in that set ?
'''

s={5,7,52,15,44,2,8}
ls=[9,7,8,2,6,11,96,15]
c=0
for i in ls:
    if i in s:
        c=c+1
print(c)

'''   
#Output:4


##7.take a list and find the third largest element from the list?
'''
ls=[9,7,8,2,6,11,96,15]
ls.sort(reverse=True)
print(ls[2])
'''
##Output:
##11









