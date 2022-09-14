#1. What about two asterisks (**)?

'''Ans: in functions (**)are used for accesing keyword arguments'''


##2.Write a function called fizz_buzz that takes a number.
##-If the number is divisible by 3, it should return “Fizz”.
##-If it is divisible by 5, it should return “Buzz”.
##-If it is divisible by both 3 and 5, it should return “FizzBuzz”.
##-Otherwise, it should return the same number.
'''
def fizz_buzz(a,b,i):
    if i%a==0 and i%b==0:
        return("FizzBuzz")
    elif i%a==0:
        return("Fizz")
    elif i%b==0:
        return("Buzz")
    else:
        return i
                   
print(fizz_buzz(3,5,15))
'''
##Output:
##FizzBuzz


##3.Write a function called showNumbers that takes a parameter called limit. It should print all the numbers
##  between 0 and limit with a label to identify the even and odd numbers.
##  For example, if the limit is 3, it should print:
##-0 EVEN
##-1 ODD
##-2 EVEN
##-3 ODD
'''
def shownumbers(limit):
    for i in range(0,limit):
        if i%2==0:
            print("{} - Even".format(i))
        else:
            print("{} - Odd".format(i))
x=5
shownumbers(x)
'''
##Output:
##0 - Even
##1 - Odd
##2 - Even
##3 - Odd
##4 - Even



##4.Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter).
##  For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
'''
def addition(limit):
    sums=0
    for num in range(1,limit+1):
        if num%3==0 or num%5==0:
            sums=sums+num
    return sums

result=addition(20)
print(result)
'''
##Output:98


##5.Write a function that prints all the prime numbers between 0 and limit where limit is a parameter.


'''
def Find_Prime(num):
    flag=True
    for i in range(2,num):
        if num%i==0:
            flag=False
    return flag
    
def list_prime(limit):
    for i in range(2,limit):
        if Find_Prime(i):
            print(i)

list_prime(20)
'''


##Output:
##2
##3
##5
##7
##11
##13
##17
##19


##6.Write a function for checking the speed of drivers. This function should have one parameter: speed.

##1.If speed is less than 70, it should print “Ok”.
##2.Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and
##  print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
##3.If the driver gets more than 12 points, the function should print: “License suspended”

'''
def status(p):
    points=p//5
    if points < 12:
        return "points :{}".format(points)
    else:
        return "License suspended"


def speed_of_driver(speed):
    if speed <= 70:
        return "ok"
    else:
        return status(speed-70)

print(speed_of_driver(int(input("Enter speed"))))
'''
    
##Output:
##Enter speed125
##points :11


##7. What is the result of “bag” > “apple”?
'''
print("bag">"apple")
'''
#Output:True

##8.What is the result of f“{2+2}+{10%3}”?
'''
print(f"{2+2}+{10%3}")
'''
#Output:4+1


##9.Write a function calculation() such that it can accept two variables and calculate the addition and
##  subtraction of it. And also it must return both addition and subtraction in a single return 
'''
def calculation(a,b):
    return a+b,a-b
print(calculation(20,30))
'''
#Output:(50, -10)


##10. Create an inner function to calculate the addition in the following way
##Create an outer function that will accept two parameters a and b
##Create an inner function inside an outer function that will calculate the addition of a and b
##At last, an outer function will add 5 into addition and return it.

'''
def calculate(a,b):
    def addition():
        return a+b
    return addition()+5
print(calculate(20,30))
'''

#Output:55

##11.Write a recursive function to calculate the sum of numbers from 0 to 10
'''
def sums(n):
    if n==1:
        return n
    else:
        return n + sums(n-1)
print(sums(10))
'''

#Output:55


##12. Assign a different name to function and call it through the new name
'''
def check(name="hello"):
    return name
xyz=check()
print(xyz)
'''
#output:hello


##13.Generate a Python list of all the even numbers between 4 to 30
'''
def even_list():
    return [i for i in range(4,31) if i%2==0]
print(even_list())
'''

##Output:[4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]

##14.Return the largest item from the given list
'''
def List(ls):
    return max(ls)
    
ls=[18, 20, 22, 24, 26, 28,6, 8, 10, 12]
print(List(ls))
'''
#Output:28


##15.Create a function showEmployee() in such a way that it should accept employee name,
##   and it’s salary and display both, and if the salary is missing in function call it should show it as 9000
'''
def showEmployee(name,salary=9000):
    print(name,"my salary is: ",salary)
showEmployee("Harish")
showEmployee("KIran",25000)
'''
##Output:
##Harish my salary is:  9000
##KIran my salary is:  25000



















