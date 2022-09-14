'''#(1) Write a program to find sum of number.
sum_num=0
while True:
    num=int(input("Enter the number..."))
    if num==0:
        break
    else:
        sum_num=sum_num+num
print(tot)
#Output:
Enter the number...4
Enter the number...56
Enter the number...12
Enter the number...84
Enter the number...11
Enter the number...0
167'''

'''#(2)WAP to find the number is strong number or not
num=int(input("enter the number"))
original_number=num
adding=0
while(num>0):125
    k=1
    s=num%10
    for i in range(1,s+1):
        k=k*i
    adding=adding+k
    num=num//10
if original_number==adding:
    print(original_number,"is a strong number")
else:
    print(original_number,"not a strong number")
    
#Output:
    enter the number145
    145 is a strong number'''

'''#(3) Python Program to Find the Square Root
number=int(input("Enter the number"))
square=number**2
print(square)'''

'''#(4) Python Program to Calculate the Area of a Triangle
base=int(input("Enter the base value"))
height=int(input("Enter the height value"))
Area=1/2*base*height
print("Area of the triangle:",Area)

#Output:
Enter the base value5
Enter the height value4
Area of the triangle: 10.0'''

'''#(5)Program to solve Quadratic Equation
a=int(input("Enter the a value...."))
b=int(input("Enter the b value...."))
c=int(input("Enter the c value...."))
l=(b**2)-(4*a*c)
m=l**0.5
x1=(-b+m)/2*a
x2=(-b-m)/2*a
print('x1 value:',x1)
print('x2 value:',x2)

#Output:
Enter the a value....5
Enter the b value....30
Enter the c value....2
x1 value: -1.6856085069241011
x2 value: -148.3143914930759'''

'''#(6) Python Program to Swap Two Variables
p=25
q=30

p=p+q
q=p-q
p=p-q
#After swap
print("p value:",p)
print("q value:",q)
#output:
p value: 30
q value: 25'''

'''#(7)Python Program to Convert Kilometres to Miles

km=float(input("Enter in km.."))
#mile=float(input("Enter in mile.."))
mile1=1.61
convert_to_miles =km*mile1
print(km,"km in",convert_to_miles,"miles")
#Output:
Enter in km..25
25.0 km in 40.25 miles'''

#8Python Program to Check Leap Year
year=int(input("Enter the year "))
if year%4==0:
    print(year,"is the leap year")
else:
    print(year,"not the leap year")

##Output:
##Enter the year 2012
##2012 is the leap year


'''#(9)Python Program to Check Prime Number
num=int(input("enter number.."))
for i in range(2,num//2):
    if num%i==0:
        print(num,"not a prime number")
        break
else:
    print(num,"prime number")
#Output:
enter number..13
13 prime number'''

'''#(10)Python Program to Find the Factorial of a Number
num=int(input("enter number.."))
mul=1
for i in range(1,num+1):
    mul=mul*i
print(mul)
#Output:
enter number..5
120
'''

'''#(11) Python Program to Print the Fibonacci sequence
num=int(input("ener number"))
c=0
a=1
b=2
while(c<num):
    print(a)
    nextele=a+b
    a=b
    b=nextele
    c=c+1
#Output:
ener number20
1
2
3
5
8
13
21
34
55
89
144
233
377
610
987
1597
2584
4181
6765
10946 '''


'''#(12) Python Program to Check Armstrong Number
num=int(input("enter the number.."))
original=num
size=len(str(num))
summ=0
while(num>0):
    n=num%10
    power=n**size
    summ=summ+power
    num=num//10
if original==summ:
    print(original,"is the armstrong number")
else:
    print(original,"is not the armstrong number")
    
#Output:
enter the number..153
153 is the armstrong number'''

'''#(13)Python Program to Find Armstrong Number in an Interval
start=int(input("Enetr from.."))
end=int(input("Enter to.."))
ls=[]
for num in range(start,end+1):
    original=num
    size=len(str(num))
    summ=0
    while(num>0):
        n=num%10
        power=n**size
        summ=summ+power
        num=num//10
    if original==summ:
        ls.append(summ)
print(ls)
Output:
Enetr from..100
Enter to..2000
[153, 370, 371, 407, 1634]'''

'''#(14)Python Program to Find the Sum of Natural Numbers
start=int(input("Enter from.."))
end=int(input("Enter to.."))
summ=0
for i in range(start,end+1):
    summ=summ+i
print("sum of natural number {} to {} is {}".format(start,end,summ))
#Output:
Enter from..1
Enter to..100
sum of natural number 1 to 100 is 5050'''

'''#(15) Python Program to Find the Factors of a Number
num=int(input("Enter number.."))
ls=[]
for i in range(1,num+1):
    if num%i==0:
        ls.append(i)
print(ls)
#Output:
Enter number..20
[1, 2, 4, 5, 10, 20]'''

'''#(16) Python Program to Convert Decimal to Binary, Octal and Hexadecimal 
#Decimal to Binary:
st=" "
num=int(input("Enter the number.."))
while(num>0):
    bina=2
    m=num % bina
    if m==0:
        st=st+str(m)
    elif m==1:
        st=st+str(m)
    num=num//2
reverse=st[::-1]
print(reverse)
#Output:
Enter the number..16
10000 '''

'''#octa to decimal
st=" "
num=int(input("Enter the number.."))
while(num>0):
    octa=8
    m=num % octa
    if m==0 or m==1 or m==2 or m==3 or m==4 or m==5 or m==6:
        st=st+str(m)
    else:
        st=str(m)
    num=num//8
reverse=st[::-1]
print(reverse)

#output:
Enter the number..16
20 '''

'''#hexa to decimal
st=" "
num=int(input("Enter the number.."))
while(num>0):
    octa=16
    m=num % octa
    if m==0 or m==1 or m==2 or m==3 or m==4 or m==5 or m==6 or m==7 or m==8 or m==9:
        st=st+str(m)
    elif m==10:
        st=st+'A'
    elif m==11:
        st=st+'B'
    elif m==12:
        st=st+'C'
    elif m==13:
        st=st+'D'
    elif m==14:
        st=st+'E'
    elif m==15:
        st=st+'F'
    num=num//16
reverse=st[::-1]
print(reverse)

#output:
Enter the number..1256
4E8 '''

'''#(17) Python Program to Find LCM
def lcm(e,f):
    if e>f:
        z=e
    else:
        z=f
    while True:
        if z%e==0 and z%f==0:
            break
        z=z+1
    return z
e=12
f=14

print("Lcm of{},{} numbers is {}".format(e,f,lcm(12,14)))

#output:
Lcm of12,14 numbers is84'''

'''#(18) Python Program to Find HCF
def calculate_hcf(m,n):
    if m>n:
        small=n
    else:
        small=m
    for i in range(1,small+1):
        if m%i==0 and n%i==0:
            store=i
    return store
num1=54
num2=24
print("H.C.F of two {},{} numbers is {}".format(num1,num2,calculate_hcf(num1,num2)))

#Output:
H.C.F of two 54,24 numbers is 6'''





    
    











        
        
    
