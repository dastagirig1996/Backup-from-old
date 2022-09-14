##def fibonacci(n):
##    if n<=1:
##        return n
##    else:
##        return(fibonacci(n-1)+fibonacci(n-2))
##
##num=int(input("Enter Number"))
##if num<0:
##    print("Invalid number")
##elif num==0:
##    print("fibonacci of num is 0")
##else:    
##    for i in range(num):
##        print(fibonacci(i))


##class Employee:
##    @staticmethod
##    def sample(self,x):
##        print('Inside static method', x)
##
### call static method
##Employee.sample(10)
##
### can be called using object
##emp = Employee()
##emp.sample(10)

'''
class Employee(object):
    def __init__(self, name, salary, project_name):
        self.name = name
        self.salary = salary
        self.project_name = project_name

    @staticmethod
    def gather_requirement(project_name):
        if project_name == 'ABC Project':
            requirement = ['task_1', 'task_2', 'task_3']
        else:
            requirement = ['task_1']
        return requirement

    # instance method
    def work(self):
        # call static method from instance method
        requirement = self.gather_requirement(self.project_name)
        for task in requirement:
            print('Completed', task)

emp = Employee('Kelly', 12000, 'ABC Project')
emp.work()

'''       




# Print the technologies which the person have?

##class Engineer:
##    def __init__(self,name,sal,techno):
##        self.name=name
##        self.sal=sal
##        self.techno=techno
##    @staticmethod
##    def gather_technologies(techno):
##        if techno=="python":
##            ls="python","Django","Sql"
##        else:
##            ls=["javascript"]
##        return ls
##    def show(self):
##        print("name :",self.name)
##        # calling static method from instance method
##        ls=self.gather_technologies(self.techno)
##        for i in ls:
##            print(i,end=",")
##        print(type(ls))
##E1=Engineer("kiran",25000,"python")
##E1.show()
##
##E2=Engineer("Ramesh",42000,"perl")
##E2.show()            


class TemperatureConverter:
    KEVIN = 'K',
    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9*c/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5*(f-32)/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5*(f+459.67)/9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9*k/5 - 459.67

    @staticmethod
    def format(value, unit):
        symbol = ''
        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = '°F'
        elif unit == TemperatureConverter.CELSIUS:
            symbol = '°C'
        elif unit == TemperatureConverter.KEVIN:
            symbol = '°K'

        return f'{value}{symbol}'


f = TemperatureConverter.celsius_to_fahrenheit(65)
print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))








































































































































































