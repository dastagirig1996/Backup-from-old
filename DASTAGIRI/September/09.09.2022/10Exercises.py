#1.  Create an application which manages an inventory of products. Create a product class which has a price, id, and quantity on hand. Then create an inventory class which keeps track of various products and can sum up the inventory value.
"""
class Product:
    obj=1
    def __init__(self,price,Id,quantity):
        self.price=price
        self.Id=Id
        self.quantity=quantity
    def display(self):
        pass
class Inventory(Product):
    @classmethod
    def show(cls):
        Product.obj=Product.obj+1
        return obj
        
    
    
p1=Product(15000,201,2)
Product.show()     

"""

#2. Create a reservation system which books airline seats or hotel rooms. It charges various rates for particular sections of the plane or hotel. Example, first class is going to cost more than coach. Hotel rooms have penthouse suites which cost more. Keep track of when rooms will be available and can be scheduled.
"""
class Revervation_System():
    def Airline(self):
        self.n=1
        self.opt=input("select your desired seat:")
        if self.opt=="Business":
            print("your seat is {} and seat number is {} bill 1000".format(self.opt,self.n))
            self.n+=1
        elif self.opt=="First":
            print("your seat is {} and seat number is {} bill 600".format(self.opt,self.n))
            self.n+=1
        elif self.opt=="General":
            print("your seat is {} and seat number is {} bill 400".format(self.opt,self.n))
            self.n+=1
        elif self.opt=="Available":
            print("your seat is {} and seat number is {} bill 400 schedule on 1st-sept-2022".format(self.opt,self.n))
            self.n+=1
            
    def Hotel_room(self):
        self.n=1
        self.opt=input("select your desired room:")
        if self.opt=="penthouse":
            print("your room type is {} and room number is {} bill 1000".format(self.opt,self.n))
            self.n+=1
        elif self.opt=="AC":
            print("your room type is {} and room number is {} bill 600".format(self.opt,self.n))
            self.n+=1
        elif self.opt=="General":
            print("your room type is {} and room number is {} bill 400".format(self.opt,self.n))
            self.n+=1
        elif self.opt=="Available":
            print("your seat is {} and seat number is {} bill 400 schedule on 1st-sept-2022".format(self.opt,self.n))
            self.n+=1
        
t=Revervation_System()
t.Airline()
t.Hotel_room()
"""

#output:

##select your desired seat:Business
##your seat is Business and seat number is 1 bill 1000
##select your desired room:General
##your room type is General and room number is 1 bill 400
##




#3. Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. Every one's pay is calculated differently, research a bit about it. After you've established an employee hierarchy, create a Company class that allows you to manage the employees. You should be able to hire, fire and raise employees.
from abc import ABC,abstractmethod
class Employee(ABC):
 
    def __init__(self, hr_emp_sal=1.1,sl_emp_sal=1.3,mgr_sal=1.5,exec_sal=1.8,bas_sal=5000,lst = [],x ='',y = '',z1=0,x1='',z = 0):
        self. hr_emp_sal =  hr_emp_sal
        self.sl_emp_sal= sl_emp_sal
        self.mgr_sal = mgr_sal
        self.exec_sal = exec_sal
        self.bas_sal = bas_sal
        self.lst =lst
        self.x  = ''
        self.y = y
        self.z1 = 0
        self.x1  =''
        self.z = 0
        
        super(Employee, self).__init__()
        
    @abstractmethod
    def execute(self):
        pass

class HourlyEmployee(Employee):
    def execute(self):
        pass
 
 
class SalariedEmployee(Employee):
    def execute(self):
        pass 
 
 
class Manager(Employee):
    def execute(self):
        pass 
 
 
class Executive(Employee):
    def execute(self):
        pass

class Company(Employee):
        def execute(self):
            pass
        
    
        def hire(self,x,y,z=1):
                if (x,y,z) not in self.lst:
                    if  y=='Hourly Employee':
                        z = self.hr_emp_sal*self.bas_sal
                        self.lst.append((self,x,y,z))
                        print(f'{x} hired for the position {y} with a salary of {z}')
                    elif y == 'Salaried Employee':
                        z = self.sl_emp_sal*self.bas_sal
                        self.lst.append((self,x,y,z))
                        print(f'{x} hired for the position {y} with a salary of {z}')
                    elif y=='Manager':
                        z=self.mgr_sal*self.bas_sal
                        self.lst.append((self,x,y,z))
                        print(f'{x} hired for the position {y} with a salary of {z}')
                    elif  y=='Executive':
                        z=self.exec_sal*self.bas_sal
                        self.lst.append((self,x,y,z))
                        print(f'{x} hired for the position {y} with a salary of {z}')
                    else:
                        print('try again.')
                else:
                    print('Employee already exists.')
        def fire(self,x,y,z):
                if (self,x,y,z) in self.lst:
                    self.lst.remove((self,x,y,z))
                    print(f'Employee {x} removed.')
                else:
                    print('Employee not found.')

        def se(self):
               print(self.lst)

        def promotion(self,x,y,z):
                x1=x
                if (self,x,y,z) in self.lst:
                    if y=='Hourly Employee':
                        y1='Salaried Employee'
                        print(f'{x1} was promoted to {y1}.')
                        z1=self.sl_emp_sal*self.bas_sal
                        self.lst.append((self,x1,y1,z1))
                        self.lst.remove((self,x,y,z))
                    elif y=='Salaried Employee':
                        y1='Manager'
                        print(f'{x1} was promoted to {y1}.')
                        z1=self.mgr_sal*self.bas_sal
                        self.lst.append((self,x1,y1,z1))
                        self.lst.remove((self,x,y,z))
                    elif y=='Manager':
                        y1='Executive'
                        print(f'{x1} was promoted to {y1}.')
                        z1=self.exec_sal*self.bas_sal
                        self.lst.append((self,x1,y1,z1))
                        self.lst.remove((self,x,y,z))
                    else:
                        print('No promotion available.')
                else:
                    print('Employee not found.')
    

c1=Company()
c1.hire("kiran",'Executive')
c2=Company()
c2.se()




#4. Create a class called Account which will be an abstract class for three other classes called CheckingAccount,
##  SavingsAccount and BusinessAccount. Manage credits and debits from these accounts through an ATM style program.
"""
from abc import ABC,abstractmethod

class Account:
    @abstractmethod
    def CheckingAccount(self):
        pass
    @abstractmethod
    def SavingAccount(self):
        pass
    def BusinessAccount(self):
        pass

class SavingAccount():
    def saving(self):
        self.tot=0
        self.amount=int(input("enter amount:"))
        print("Select menu:1. credit \n2.debit")
        self.ch=int(input("enter your choice:"))
        if self.ch==1:
            self.tot=self.tot+self.amount
        elif self.ch==2:
            self.tot=self.tot-self.amount
        print("The available balance is :",self.tot)
            
class BusinessAccount():
    def business(self):
        self.tot=0
        self.amount=int(input("enter amount:"))
        print("Select menu:1. credit \n2.debit")
        self.ch=int(input("enter your choice:"))
        if self.ch==1:
            self.tot=self.tot+self.amount
        elif self.ch==2:
            self.tot=self.tot-self.amount
        print("The available balance is :",self.tot)
class CheckingAccount(SavingAccount,BusinessAccount):
    def __init__(self,acn):
        self.acn=acn
        if self.acn==12345:
            print("Select your account  type:")
            print("1. saving \n2.business")
            self.type=int(input("enter your choice:"))
            if self.type==1:
                SavingAccount.saving(self)
            elif self.type==2:
                BusinessAccount().business(self)
            else:
                print("pls enter valid account type...")
        else:
            print("pls enter valid account number...")
acn=int(input("enter your account number:"))
t=CheckingAccount(acn)


#output:
enter your account number:12345
Select your account  type:
1. saving 
2.business
enter your choice:1
enter amount:200
Select menu:1. credit 
2.debit
enter your choice:1
The available balance is : 200
"""

#5. Create a patient class and a doctor class. Have a doctor that can handle multiple patients and setup a scheduling program where a doctor can only handle 16 patients during an 8 hr work day.

"""docs = {}
pats = {}

# create a list of days and times to facilitate booking
days = ["Monday","Tuesday","Wednesday","Thursday","Friday"]
times = ["8:00-8:30","8:30-9:00","9:00-9:30","9:30-10:00","10:00-10:30","10:30-11:00","11:00-11:30","11:30-12:00","13:00-13:30","13:30-14:00","14:00-14:30","14:30-15:00","15:00-15:30","15:30-16:00","16:00-16:30","16:30-17:00"]

# create patient class
class Patient():
    # allow patients to have bookings
    bookings = []

    def __init__(self,Name):
        self.Name = Name

    # have a string representation of the patient
    def __str__(self):
        return self.Name

# create doctor class
class Doctor():
    # create dictionary counting the number of patients the doctor has on each day
    n_patients = {"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0}
    # allow doctors to have bookings
    bookings = []
    
    def __init__(self,Name):
        self.Name = Name

    def add_patient(self,day):
        self.n_patients[day] += 1
        
    # have a string representation of the doctor
    def __str__(self):
        return self.Name

# define a method for a patient to choose a doctor
def choose_doc(chosen_doc):
    if chosen_doc in docs.keys():
        while True:
            day = str(input("Please enter your preferred day: "))
            if day.capitalize() in days:
                print("Thank you! Opening Doctor {}'s schedule...".format(chosen_doc))
                break
            else: 
                print("Sorry, please type one of 'Monday', 'Tuesday','Wednesday','Thursday' or 'Friday': ")
        return [docs[chosen_doc],day.capitalize()]
    else:
        print("Sorry, Doctor {} is not in the system. Please choose another doctor!".format(chosen_doc))

# define a method to make a booking for a given day. Make sure timeslots don't overlap between days
def make_booking(Doctor,Patient,day):
    if Doctor.n_patients[day] == 16:
        return "Sorry, Doctor {} is booking out on this day.".format(Doctor.Name)
    
    slots = {1:"8:00-8:30",2:"8:30-9:00",3:"9:00-9:30",4:"9:30-10:00",5:"10:00-10:30",6:"10:30-11:00",7:"11:00-11:30",8:"11:30-12:00",9:"13:00-13:30",10:"13:30-14:00",11:"14:00-14:30",12:"14:30-15:00",13:"15:00-15:30",14:"15:30-16:00",15:"16:00-16:30",16:"16:30-17:00"}
    # remove slots that are already booked by others for that day and time
    if len(Doctor.bookings) > 0:
        for booking in Doctor.bookings:
            for key,val in slots.items():
                if val in booking and booking[0] == day:
                    del slots[key]
                    break
    while True:
        try:
            time = int(input("Choose your slot (please enter the relevant corresponding number): {}\n".format(slots)))
            if time in slots:
                # append time to ease sorting when viewing schedules
                if Doctor.n_patients[day] < 16:
                    Patient.bookings.append([day,slots[time],Doctor.Name,time])
                    Doctor.bookings.append([day,slots[time],Patient.Name,time])
                    Doctor.add_patient(day)
                    print("Booking successfully made!")
                    break
                else:
                    print("Sorry, Doctor {} is booked out on this time and day.".format(Doctor.Name))
                    break
            else:
                print("Please enter a number in accordance with the available slots!")
                continue
        except:
            print("Please enter a number from 1 to 16, in accordance with the slots!")
            continue

# Python code to sort nested lists using fourth element  
# of sublist Inplace way to sort using sort() 
def Sort(sub_li): 
    # reverse = None (Sorts in Ascending order) 
    # key is set to sort using fourth element of  
    # sublist lambda has been used 
    sub_li.sort(key = lambda x: x[3]) 
    return sub_li 

# define a method for doctors and patients to view their bookings
# input schedule is type list
def view_booking(schedule):
    while True:
        see_bookings = str(input("Would you like to view your bookings? (Y or N): "))
        if see_bookings.capitalize() == "Y":
            if len(schedule) == 0:
                print("You have no bookings at the moment.")
                break
            else:
                # print bookings by day
                for day in days:
                    relevant_bookings = []
                    for booking in schedule:
                        if booking[0] == day:
                            relevant_bookings.append(booking)
                    # sort into chronological order
                    relevant_bookings = Sort(relevant_bookings)
                    if len(relevant_bookings) > 0:
                        print(day,": ")
                        for item in relevant_bookings:
                            print(item[1],": ",item[2])
                break
        elif see_bookings.capitalize() == "N":
            break
        else: 
            print("Please state whether you would like to view your bookings (Y) or not (N).")
            continue

# define method to register patients and doctors
def register(classtype, name):
    if classtype == "Doctor":
        name = Doctor(name)
        docs[name.Name] = name
    elif classtype == "Patient":
        name = Patient(name)
        pats[name.Name] = name

# run code!
system = True
while system:
    welcome = str(input("Welcome to the booking system! Please state you are a patient (1) or a doctor (2): "))
    # doctor
    if welcome == "2":
        introduce = str(input("Welcome! Please state your name: "))
        if introduce not in docs:
            print("Welcome Doctor {}! You have been registered to our doctors list.".format(introduce))
            register("Doctor",introduce)
            view_booking(docs[introduce].bookings)
        else:
            print("Welcome Doctor {}!".format(introduce))
            view_booking(docs[introduce].bookings)
        

    # patient
    elif welcome == "1":
        introduce = str(input("Welcome! Please state your name: "))
        if introduce not in pats:
            print("Welcome {}! You have been registered to our patient list.".format(introduce))
            register("Patient",introduce)
        else:
            print("Welcome {}!".format(introduce))

        asking = True
        while asking:
            ask_booking = str(input("Would you like to make a booking today? (Y or N)"))
            if ask_booking.capitalize() == "Y":
                # ask patient to choose a doctor to see
                processing = True
                while processing:
                    if len(docs) > 0:
                        chosen_doc = input("Please choose a doctor to see: {}".format(list(docs.keys())))
                        chosen = choose_doc(chosen_doc)
                        if chosen is None:
                            continue
                        # make one or more bookings
                        make_booking(chosen[0],pats[introduce],chosen[1])
                        again = ""
                        while again != "Y" and again != "N":
                            again = input("Would you like to make another booking? (Y or N): ")
                            if again.capitalize() == "Y":
                                continue
                            elif again.capitalize() == "N":
                                processing = False
                                asking = False
                            else:
                                print("Please confirm whether you would like to make another booking (Y) or not (N).")
                                continue
                    else:
                        print("Sorry, there are no doctors available at the moment. Please try again later.")
                        break
                break
            elif ask_booking.capitalize() == "N":
                break
            else:
                print("Please confirm whether you would like to make a booking (Y) or not (N).")
                continue

        view_booking(pats[introduce].bookings)
        
    else:
        print("Please confirm whether you are a patient (1) or a doctor (2)!")
        continue
  
    print("Thank you for using our system. Please come again!")
    system = False

"""

#6 Create a recipe class with ingredients and a put them in a recipe manager program that organizes them into categories like deserts, main courses or by ingredients like chicken, beef, soups, pies etc.
'''
class recipe:
    def deserts(self):
        print("Desert items")
        print("1.ice creams \n2. softdring") 
        print()
    def ingredients(self):
        print("Ingredients items")
        print("1.chicken \n2.beef \n3.soups \n4.pies")

    def main_course(self):
        print("Main course for ingredients:")
        self.deserts()
        self.ingredients()
t=recipe()
t.main_course()
'''    
#7. Create an image abstract class and then a class that inherits from it for each image type.
#  Put them in a program which displays them in a gallery style format for viewing.



#8. Create an abstract class called Shape and then inherit from it other shapes like diamond, rectangle,
#   circle, triangle etc. Then have each class override the area and perimeter functionality to handle each shape type.
"""
from abc import ABC,abstractmethod
class Shapes(ABC):
    @abstractmethod
    def diamond(self):
        pass
    def rectangle(self):
        pass
    def circle(self):
        pass
    def triangle(self):
        pass
class Diamond:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        a=self.a*self.b
        return a
    def perimeter(self):
        p=2*(self.a+self.b)
        return p

class Circle(Diamond):
    def __init__(self,pi,r):
        self.pi=pi
        self.r=r
    def area(self):
        a=self.pi*self.r**2
        return a
    def perimeter(self):
        p=2*self.pi+self.r
        return p
    
class Rectangle(Circle):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def area(self):
        a=self.a*self.b
        return a
    def perimeter(self):
        p=2*(self.a+self.b)
        return p
class Triangle(Rectangle):
    
    def __init__(self,a,b,c=5):
        self.a=a
        self.b=b
        self.c=c
    def area(self):
        a=(self.a*self.b)/2
        return a
    def perimeter(self):
        p=self.a+self.b+self.c
        return p

obj=Rectangle(5,9)
print(obj.area())
print(obj.perimeter())

obj2=Triangle(2,9)
print(obj2.area())
obj3=Triangle(8,2,9)
print(obj3.perimeter())
"""
##Output:
##45
##28
##9.0
##19


#9.Create a flower shop application which deals in flower objects and use those flower
# objects in a bouquet object which can then be sold. Keep track of the number
# of objects and when you may need to order more.

"""

from collections import defaultdict
from enum import Enum, auto


class FlowerType(Enum):
    Rose = auto()
    Carnation = auto()
    Tulip = auto()
    Lily = auto()
    Orchid = auto()


class Flower:

    def __init__(self, flower_type):
        self._flower_type = flower_type

    def __repr__(self):
        classname = self.__class__.__name__
        return f'<{classname}: {self._flower_type}>'

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return self._flower_type == other.flower_type

    @property
    def flower_type(self):
        return self._flower_type


class Bouquet:

    def __init__(self, name, price, flowers=None):
        self._name = name
        self.price = price

        # To each flower corresponds its quantity
        self.flowers = (defaultdict(int, flowers)
                        if flowers is not None
                        else defaultdict(int))

    def __repr__(self):
        classname = self.__class__.__name__
        return f'<{classname}: {self._name}>'

    def __hash__(self):
        return hash(repr(self))

    def __eq__(self, other):
        return self._name == other.name

    def __getitem__(self, key):
        return self.flowers[key]

    def __setitem__(self, key, value):
        self.flowers[key] = value

    def __delitem__(self, key):
        del self.flowers[key]

    @property
    def name(self):
        return self._name


class Shop:

    def __init__(self, name, bouquets=None):
        self._name = name

        # To each bouquet corresponds its quantity
        self.bouquets = (defaultdict(int, bouquets)
                         if bouquets is not None
                         else defaultdict(int))

    def __repr__(self):
        classname = self.__class__.__name__
        return f'<{classname}: {self._name}>'

    def __getitem__(self, key):
        return self.bouquets[key]

    def __setitem__(self, key, value):
        self.bouquets[key] = value

    def __delitem__(self, key):
        del self.bouquets[key]

    @property
    def name(self):
        return self._name

    def _has_enough_bouquets(self, bouquet, quantity):
        if quantity > self.bouquets[bouquet]:
            raise ValueError(
                f"{self} doesn't have enough {bouquet}"
            )

    def sell(self, bouquet, quantity=1):
        self._has_enough_bouquets(bouquet, quantity)
        self.bouquets[bouquet] -= quantity

    def order(self, bouquet, quantity=1):
        self.bouquets[bouquet] += quantity


if __name__ == '__main__':

    # Flowers

    rose = Flower(FlowerType.Rose)
    lily = Flower(FlowerType.Lily)
    orchid = Flower(FlowerType.Orchid)
    carnation = Flower(FlowerType.Carnation)

    # Bouquets

    romantic = Bouquet('Romantic', price=25.2, flowers={
        rose: 20
    })
    royal_love = Bouquet('Royal Love', price=10.5, flowers={
        orchid: 8
    })
    enchanted_bloom = Bouquet('Enchanted Bloom', price=30,
    flowers={
        lily: 2,
        rose: 5,
        carnation: 5})

    # Shop

    shop = Shop('Florists', bouquets={
        romantic: 5,
        royal_love: 2,
        enchanted_bloom: 3
    })

    shop.sell(romantic, quantity=5)
    shop.order(romantic, quantity=4)
    shop.sell(romantic, quantity=4)

"""















