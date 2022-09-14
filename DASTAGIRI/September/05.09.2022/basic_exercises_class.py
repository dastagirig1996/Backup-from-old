#1.Python Program to Convert Bytes to a String

#Main Program
"""
class Bytes_to_String():
    def __init__(self):
        self.bt=b"Lets eat Pizza \xf0\x9f\x8d\x95!"
        print("Types:",type(self.bt))
    def convert(self):
        str1=self.bt.decode()
        print(str1)
        print("Types:",type(str1))
#calling
obj=Bytes_to_String()
obj.convert()
#Output:
Types: <class 'bytes'>
Lets eat Pizza 🍕!
Types: <class 'str'>
"""

#2.Python Program to Remove Duplicate Element From a List


#Main Program
"""
class Duplicate_Element():
    @classmethod   
    def show(cls):
        cls.lst=[int(x) for x in input("enter your element:").split(',')]
        cls.set1=set(cls.lst)
        return list(cls.set1)
#Calling
obj=Duplicate_Element()
print(obj.show())

#output:
enter your element:4,5,6,7,4,3,5
[3, 4, 5, 6, 7]
"""




#3.Python Program to Check If Two Strings are Anagram

#Main Program
"""
s1 =input("enter first word:")
s2 =input("enter second word:")
class Anagram():
    def check(self,s1,s2):
        if(sorted(s1)== sorted(s2)):
            print("The strings are anagrams.")
            print(s1,"==>",s2)
        else:
            print("The strings aren't anagrams.")
            print(s1,"==>",s2)
#calling
obj=Anagram()
obj.check(s1, s2)

#output:
enter first word:silent
enter second word:lise
The strings aren't anagrams
silent ==> lise

enter first word:license
enter second word:silence
The strings are anagrams
license ==> silence
"""


#4.Python Program to Count the Number of Digits Present In a Number

#Main Program
"""
class Count_Number():
    num=int(input("enter your number:"))
    @classmethod
    def show(cls):
        l=len(str(cls.num))
        print("Number of digit of {} is {}".format(cls.num,l))
#calling
obj=Count_Number()
obj.show()

#Output:
enter your number:546
Number of digit of 546 is 3
"""
    
#5.Python Program to Trim Whitespace From a String

#Main Program
"""
class Trim_white_space():
    def __init__(self):
        self.str1=input("enter your sentence:")
    def show(self):
        for i in self.str1:
            if i == " ":
                continue
            else:
                print(i,end="")
    @staticmethod
    def display():
        print("\nTrim Whitespaces are removed...")
    
#calling
obj=Trim_white_space()
obj.show()
obj.display()

#output:
enter your sentence:This is python programming
Thisispythonprogramming
"""




#6.Python Program to Differentiate Between type() and isinstance()

#Main Program
"""
class Convert():
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
#calling
obj=Convert("Ramesh",24)
print(type(obj))
print(isinstance(obj,Convert))

#output:

Ramesh 24
<class '__main__.Convert'>
True"""



#7.Python Program to Delete an Element From a Dictionary

#Main Program
"""
class delete_Element():
    def display(self):
        dict1={3:"Ram",5:"Ramesh",7:"Ramu"}
        dict1.popitem()
        print(dict1)
#calling
obj=delete_Element()()
obj.display()

#output:
{3: 'Ram', 5: 'Ramesh'}
"""





#8.Python Program to Count the Occurrence of an Item in a List

#Main Program
"""
class Occurence():
    def show(self):
        lst=[int(x) for x in input("enter your number:").split(',')]
        for i in lst:
            x=lst.count(i)
            print(i,"=",x)
#calling
obj=Occurence()
obj.show()


#output:
enter your number:45,67,45,2,78,4,3,90,1,2,67
45 = 2
67 = 2
45 = 2
2 = 2
78 = 1
4 = 1
3 = 1
90 = 1
1 = 1
2 = 2
67 = 2
"""



#9.Python Program to Randomly Select an Element From the List

#Main Program
"""
import random

class Rand_Element():
    def show(self):
        lst = [x for x in input("enter your number:").split(',')]
        item = random.choice(lst)
        print(item)
#calling
obj=Rand_Element()
obj.show()  #4
#output:
enter your number:3,4,5,6"ramesh",56.6,"python",34
3
"""

##10.Python Program to Get the Last Element of the List

#Main Program
"""
lst = [45,24,56,35,12,45]
class Last_Element():
    @classmethod
    def details(cls,lst):
        cls.lst=lst
    @classmethod   
    def show(cls):
        print("last element is : ",cls.lst[-1])

#calling
obj=Last_Element()
obj.details(lst)
obj.show()

#output:
last element is :  45
"""


#11.Python Program to Check if a Key is Already Present in a Dictionary

#Main Program
"""
class Key_present():
    def __init__(self,dct):
        self.dct=dct
    def show(self):
        key=int(input("enter the key : "))
        if key in self.dct.keys():
            print("present")
        else:
            print("not present")

#calling
dict1={22:"Ram",67:"Ramesh",45:"Ramu"}
ob=Key_present(dict1)
ob.show()

#output:

enter the key : 67
present
enter the key : 23
not present
"""



#12.Python Program to Iterate Over Dictionaries Using for Loop


#Main Program
"""
class iter_dict:
    def __init__(self,dt):
        self.dt=dt
    def show(self):
        for i,j in dt.items():
            print(i,j)
#calling
            
dt={22:"Ram",67:"Ramesh",45:"Ramu"}
ob=iter_dict(dt)
ob.show()

#Output:
22 Ram
67 Ramesh
45 Ramu
"""




##13.Python Program to Flatten a Nested List

#Main Program
"""
class Nested_List():
    def __init__(self,lst):
        self.lst=lst
    def show(self):
        for i in lst:
            for j in i:
                print(j,end=" ")

#calling
lst = [[1], [2, 3], [4, 5, 6, 7]]
ob=Nested_List(lst)
ob.show()
        
#Output:
1 2 3 4 5 6 7
"""





#14.Python Program to Sort Words in Alphabetic Order

#Main Program
"""
class Sort():
    def __init__(self,word):
        self.word=word
    def display(self):
        word.sort()
        print(word)
#calling
word=["Abc","Tiger","Elephant","Rabbit"]
obj=Sort(word)
obj.display()

#Output:

['Abc', 'Elephant', 'Rabbit', 'Tiger']
"""




##15.Python Program to Remove Punctuations From a String

#Main Program
"""
class pun():
    def __init__(self,str1):
        self.str1=str1
    def show(self):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        res = ""
        for i in str1:
           if i not in punctuations:
               res = res + i
        print(res)

str1 = input("Enter your string : ")
obj=pun(str1)
obj.show()

#output:

Enter your string : Ramesh@@##)(&*&^!! is for}}][ py$#thon
Ramesh is for python
"""



#16. Python Program to Convert Decimal to Binary Using Recursion?
'''
dec=10
def one(dec):
    if dec==0:
        return True
    else:
        t=dec%2
        return one(t)
print(one(dec))

'''   




#17. Python Program to Find Sum of Natural Numbers Using Recursion

"""
n=3
def one(n):
    if n==0:
        return False
    else:
        return n+one(n-1)
print(one(n))  #6
"""




#18. Python Program to Display Fibonacci Sequence Using Recursion

#Main Program
"""
fib=int(input("enter your number:"))
def one(fib):
    if fib<=1:
        return fib
    else:
        return (one(fib-1)+one(fib-2))
    
for i in range(fib+1):
    print(one(i),end=' ')  #0 1 1 2 3 5
"""


#19. Python Program to Find the Factors of a Number

#Main Program
"""
class Factors():
    def __init__(self):
        self.n=int(input("Enter your number:"))
        self.s=1
    def cal(self):
        for i in range(1,self.n+1):
            self.s*=i
        return self.s
#calling
obj=Factors()
print(obj.cal())
#Output:
Enter your number:5
120
"""




#20. Python Program to Find the Sum of Natural Numbers

#Main Program
"""
class sum_natural():
    def __init__(self):
        self.n=int(input("enter number:"))
        self.s=0
    def cal(self):
        for i in range(1,self.n+1):
            self.s+=i
        print(self.s) #15
obj=sum_natural()
obj.cal()

#output:
enter number:5
15
"""

#21. Python Program to Check Armstrong Number

#Main Program
"""  
class Armstrong():
    def __init__(self):
        self.num=int(input("enter number:"))
        self.tr=self.num
        self.l=len(str(self.num))
        self.t=0
    def cal(self):
        while 0<self.num:
            r=self.num%10
            self.t=self.t+(r**self.l)
            self.num=self.num//10
        if self.tr==self.t:
            print("Armstrong:",self.t)
        else:
            print("not Armstrong:",self.t)
t=Armstrong()
t.cal()

#output:
enter number:153
Armstrong: 153

enter number:345
not Armstrong: 216
"""
#22. Python Program to Print the Fibonacci sequence

#Main Program
"""
class Fibo():
    def __init__(self):
        self.fib=int(input("enter number:"))
        self.t1=0
        self.t2=1
        print(self.t1,end=' ')
        print(self.t2,end=' ')
    def cal(self):
        while self.fib>0:
            t3=self.t1+self.t2
            if t3<=self.fib:
                print(t3,end=' ')
            self.t1=self.t2
            self.t2=t3
            self.fib-=1
obj=Fibo()
obj.cal()
#output:

enter number:5
0 1 1 2 3
"""

#23. Python Program to Find the Largest Among Three Numbers

#Main Program
"""
class Large():
    def __init__(self):
        self.a=int(input("first:"))
        self.b=int(input("second:"))
        self.c=int(input("third:"))
    def great(self):
        if (self.a>self.b) and (self.a>self.c):
            print("largest:",self.a)
        elif (self.b>self.a) and (self.b>self.c):
            print("largest:",self.b)
        else:
            print("largest:",self.c)
obj=Large()
obj.great()
#output:

first:4
second:6
third:2
largest: 6
"""

#24. Python Program to Generate a Random Number
#Main Program
"""
import random

class number():
    def __init__(self):
        self.n=int(input("enter max of range number:"))
    
        r=random.randint(0,self.n+1)
        print(r)
obj=number()
#output:
enter max of range number:10000000
1350123
"""

#Python Program to Check Whether a Number is Palindrome or Not?

#Main program
"""
n=int(input("enter number:"))
t=n
p=0
class Palindrome():
    def __init__(self,n,t,p):
        self.n=n
        self.t=t
        self.p=p
    def cal(self):
        while self.n>0:
            r=self.n%10
            self.p=(self.p*10)+r  
            self.n=self.n//10
        if self.t==self.p:
            print("palindrome:",self.p)
        else:
            print("not palindrome:",self.p)
obj=Palindrome(n,t,p)
obj.cal()

#output:
enter number:121
palindrome: 121
enter number:123
not palindrome: 321
"""

