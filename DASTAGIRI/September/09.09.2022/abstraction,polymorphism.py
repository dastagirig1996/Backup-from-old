##1. write a 5 example programs on method overriding using constructor.

'''
#ex1
class school:
    def __init__(self,name):
        self.name=name
    def show(self):
        print("Name :",self.name)
        print("Iam in school")
class student(school):
    def __init__(self,name):
        self.name=name
    def show(self):
        super().show()  
        print("Name :",self.name )
        print("Iam in Student")
sc1=school("akshara")
sc1.show()



#Output:
##Name : akshara
##Iam in school

#ex2
class Addition:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def show(self):
        summ=self.n1+self.n2
        return summ
class Multiply(Addition):
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def show(self):
        mul=self.n1*self.n2
        return mul

m1=Multiply(5,3)
print(m1.show())

##Output:
##15

#ex3
class Is_Even:
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def show(self):
        if self.n1%2==0 and self.n2%2==0:
            return "even"
        else:
            return "odd"
class Substraction(Is_Even):
    def __init__(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def show(self):
        sub=self.n1-self.n2
        return sub

obj1=Is_Even(6,8)
print(obj1.show())

obj2=Substraction(6,8)
print(obj2.show())

#ex4
class Bike():
    def __init__(self,wheels,fuel):
         self.wheels=wheels
         self.fuel=fuel
    def disp(self):
        return self.wheels,self.fuel

    
class Car(Bike):
    def __init__(self,wheels,fuel):
         self.wheels=wheels
         self.fuel=fuel
    def disp(self):
        return self.wheels,self.fuel

obj=Bike(2,"petrol")
obj.disp()


#ex5
class City():
    def __init__(self,name):
         self.name=name
    def disp(self):
        return self.name

    
class Village(City):
    def __init__(self,name):
         self.name=name
    def disp(self):
        return self.name

obj=City("Hyd")
print(obj.disp())


obj2=Village("kottur")
print(obj2.disp())
'''




##2. write 5 different example program showing polymorphism using functions   (with 3 instance variables and 2 class variables)
#Example:1 Duck Typing
'''
class Duck:  
   def swim(self):  
         print("I m a duck, and I can swim.")  
   
class Sparrow:  
     def swim(self):  
         print("I m a sparrow, and I can swim.")  
   
class Crocodile:  
     def swim(self):  
         print("I m a Crocodile, and I can swim, but not quack.")  
   
def duck_testing(animal):  
     animal.swim()  
       
       
duck_testing(Duck())  
duck_testing(Sparrow())  
duck_testing(Crocodile())

#output:
I m a duck, and I can swim.
I m a sparrow, and I can swim.
I m a Crocodile, and I can swim, but not quack.
'''
#Example:2 overriding
'''
class Rbi:
    x = 10
    def min_balance(self):
        minbal = 0
        print("minbal:",minbal)
class HDFC(Rbi):
    x = 20
    def min_balance(self):
        minbal = 1000
        print("HDFC Min Balance:",minbal)
class ICICI(Rbi):
    x = 30
    def min_balance(self):
        minbal = 1500
        print("ICICI Min Balance:",minbal)
class SBI(Rbi):
    x = 40
    def min_balance(self):
        minbal = 2000
        print("SBI Min Balance:",minbal)

obj = HDFC()
obj.min_balance()
print("X value is :",HDFC.x)
print('\n')
obj1 = SBI()
obj1.min_balance()
print("X Value is:",SBI.x)

#output:
HDFC Min Balance: 1000
X value is : 20

SBI Min Balance: 2000
X Value is: 40

'''
#Example:3 method overloading 
'''
class A:
    def add(self,x,*y):
        if x == 'int':
            result = 0
        if x == 'str':
            result = ' '
        for p in y:
            result = result + p
        print(result)

a= A()
a.add('int',10,20,30)
a.add('str','web','technology')
'''
#Example:4 operator overloading
'''
class A:
    def __init__(self, a):
        self.a = a
  
    def __add__(self, o):
        return self.a + o.a 
ob1 = A(1)
ob2 = A(2)
ob3 = A("VINAY")
ob4 = A("SAAME")
  
print(ob1 + ob2)
print(ob3 + ob4)

#output:
3
VINAYSAAME
'''
#Example:5
'''
class IDK:
    x1=100
    y1=1000
    def __init__(self,num1,x2,y2):
        self.num1=num1
        self.x2=x2
        self.y2=y2
    def factors(self):
        print("Factors")
        for i in range(1,  self.num1+ 1):
            if  self.num1 % i == 0:
                print(i)
    def distance(self):
        print(((self.x2-IDK.x1)+(self.y2-IDK.y1))**0.5)
idk=IDK(4,200,2000)
idk.factors()

#output:
Factors
1
2
4
'''
##3. Write 5 different example programs showing polymorphism using objects.(include class and instance variables)

#Ex:1
'''
class Square:
  x = 25
object = Square()
print(object.x**2)

output:
625
'''

#Example:2
'''
class Ferrari:
    def fuel_type(self):
        print("Petrol")

    def max_speed(self):
        print("Max speed is 350")

class BMW:
    def fuel_type(self):
        print("Diesel")

    def max_speed(self):
        print("Max speed is 240")

# normal function
def car_details(obj):
    obj.fuel_type()
    obj.max_speed()

ferrari = Ferrari()
bmw = BMW()

car_details(ferrari)
car_details(bmw)

output:
Petrol
Max speed is 350
Diesel
Max speed is 240
'''

#Example:3
'''
class Telugu_book:
    def price(self):
        print('price of telugu book is 340')
    def pages(self):
        print('total pages are 780')

class English_book:
    def price(self):
        print('price of telugu book is 280')
    def pages(self):
        print('total pages are 680')
def book_details(obj):
    obj.price()
    obj.pages()
    
t=Telugu_book()
e=English_book()

book_details(t)
book_details(e)

#output:
    
price of telugu book is 340
total pages are 780
price of telugu book is 280
total pages are 680
'''

#Example:4
'''
class vehicle():
	def name(self):
		print("bmw ")

	def model(self):
		print("zx123")

	def price(self):
		print("10,000,00")

class automobiles():
	def name(self):
		print("bike")

	def model(self):
		print("zmr 250")

	def price(self):
		print("2,00,000")

def func(obj):
	obj.name()
	obj.model()
	obj.price()


obj_vehicle = vehicle()
obj_automobiles = automobiles()

func(obj_vehicle)
func(obj_automobiles)

#output:
bmw 
zx123
10,000,00
bike
zmr 250
2,00,000
'''
#Example:5
'''
class Emp:
    def name(self):
        print('My name is vinay')
    def age(self):
        print('MY age is 23')
class Student():
    def name(self):
        print('My name is gopi')
    def age(self):
        print('My age is 24')

def fun(obj):
    obj.name()
    obj.age()

emp=Emp()
std=Student()

fun(emp)
fun(std)

output:
My name is vinay
MY age is 23
My name is gopi
My age is 24
'''
##4. write a python program showing method overloading
"""
class first():

    def result(self,a):
        self.a=a
        self.b=int(input("enter second number:"))
        print("Result:",a+self.b)
class second(first):
    def result(self,a=100):
        self.a=a
        self.b=int(input("enter second number:"))
        print("Result:",a-self.b)
a=10
t=second()
t.result()
t.result(a)
"""

##5. write a python program where u create a class with only abstract methods.
'''
from abc import ABC,abstractmethod
class first(ABC):
    @abstractmethod
    def add(self):
        pass
    def sub(self):
        pass
'''
    
        


#6. Write a python program where u create a class with both concrete and abstract methods?

"""
from abc import ABC,abstractmethod
class first(ABC):
    @abstractmethod
    def add(self):
        pass
    def sub(self):
        pass
"""
#7. write 5 different examples on abstraction (use both class and instance variables.)
'''
#ex1
from abc import ABC,abstarctmethod
class Car(ABC):
    @abstractmethod
    def engine(self):
        pass
    @abstarctmethod
    def structure(self):
        pass
    
#ex2
from abc import ABC,abstarctmethod
class Soap(ABC):
    @abstractmethod
    def formula(self):
        pass
    @abstractmethod
    def process(self):
        pass

#ex3
from abc import ABC,abstarctmethod
class Mobile(ABC):
    @abstractmethod
    def software(self):
        pass
    @abstractmethod
    def parts(self):
        pass

#ex4
from abc import ABC,abstarctmethod
class Bottle(ABC):
    @abstractmethod
    def materials(self):
        pass
    def shape(self):
        pass
#ex5
from abc import ABC,abstarctmethod
class Glass(ABC):
    @abstractmethod
    def Compostitions(self):
        pass
    @abstractmethod
    def Machines(self):
        pass
        

'''















