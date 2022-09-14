'''#1)print frist 10 number using while loop:
n=10
while n>0:
    print(n)
    n=n-1
Output:
10
9
8
7
6
5
4
3
2
1'''
'''#2)calculalate sum of all numbers from 1 to given number
n=int(input("Enter number.."))
summ=0
for i in range(1,n+1):
    summ=summ+i
print(summ)

Output:
    
Enter number..10
55'''

'''#3)WAP to print multiplication table of given number
table=int(input("Enter:"))
for i in range(1,11):
    print(table,"*",i,'=',i*table)
Enter:6
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
6 * 6 = 36
6 * 7 = 42
6 * 8 = 48
6 * 9 = 54
6 * 10 = 60'''

'''#4.display numbers from using list
ls=[5,8,7,5,6,4]
for i in ls:
    print(i)
Output:
5
8
7
5
6
4
'''
'''#5.count total numbers of digits in a number
num=646456
print(len(str(num)))
Output:
6'''

'''#6.print list in reverse order using loop
ls=[5,8,4,6,8,2]
ls1=[]
for i in range(len(ls)-1,-1,-1):
    ls1.append (ls[i])
print(ls1)

Output:
[2, 8, 6, 4, 8, 5]'''

'''#7. numbers from -10 to -1 for loop display
for i in range(-10,0,1):
    print(i,end=',')
Output:
-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,'''

''''#8.use else block to display message of "done" after successful execution of for loop
for i in range(1,10):
    print(i)
else:
    print("done")
Output:
1
2
3
4
5
6
7
8
9
done'''

'''#9 write a program to print all prime numbers within range
for i in range(2,20):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i)
Output:
2
3
5
7
11
13
17
19'''

'''#10.dispaly fibonacci series upto es
s=10
a=1
b=2
c=0
while(c<s):
    print(a)
    nextelem=a+b
    a=b
    b=nextelem
    c=c+1

#Output:
    1
2
3
5
8
13
21
34
55
89'''

'''#11)Find the factorial of a given number
n=int(input("ENTER:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#Output:
ENTER:5
120'''

'''#12) Reverse a given integer number
num=int(input("Enter"))
reverse=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
print(reverse)

#Output:
Enter259
952'''

'''#13) Find the sum of the series upto n terms
n=10
sums=0
for i in range(1,n+1):
    sums=sums+i
    print(sums)
#Output:
 1
3
6
10
15
21
28
36
45
55   '''

'''#14) Calculate the cube of all numbers from 1 to a given number
num=int(input("Enter:"))
for i in range(1,num+1):
    print(i**3)

#output:
Enter:5
1
8
27
64
125'''

'''#15) Use a loop to display elements from a given list present at odd index positions
ls=[5,7,8,4,5,4,5,4,6,9,8,2,1]
for i in range(0,len(ls),2):
    print(ls[i])

#Output:
5
8
5
5
6
8
1'''

#16) Name the keyword which helps in writing code involves condition.
'''#17)Write the syntax of simple if statement.
n=5
if n>=3:
    print("true")
#Output:
true'''

#18) Is there any limit of statement that can appear under an if block.
'''Ans:"YES"'''

'''#19)Write a program to check whether a person is eligible for voting or not. (accept age from user)
age=int(input("enter age:"))
if age>=18:
    print("eligible for voting")
else:
    print("not eligible for voting")

#Output:
enter age:17
not eligible for voting'''

'''#20)Write a program to check whether a number entered by user is even or odd.

num=int(input("Enter:"))
if num%2==0:
    print(num,"its even number")
else:
    print(num,"its odd number")

#Output:
Enter:8
8 its even number
'''

'''#21)a program Write to check whether a number is divisible by 7 or not.
num=int(input("Enter:"))
if num%7==0:
    print(num,"divisable")
else:
    print(num,"not divisable")
    
#Output:
Enter:49
49 divisable'''

'''#22)Write a program to display "Hello" if a number entered by user is a multiple of five ,otherwise print "Bye". 
num=int(input("Enter:"))
if num%5==0:
    print('Hello')
else:
    print('Bye')
    
#Output:
Enter:12
Bye'''

##23)Write a program to calculate the electricity bill (accept number of unit from user)
##   according to the following criteria : 
##
##            Unit                                                     Price   
##
##First 100 units                                               no charge 
##
##Next 100 units                                              Rs 5 per unit 
##
##After 200 units                                             Rs 10 per unit

'''units=int(input("ENter no units:"))
temp=units
if units<=100:
    print("no charge")
else:
    unitprice1=5
    costof200=100*unitprice1
    if units>100 and units<=200:
        costupto200=(units-100)*unitprice1
        print("units:",units,"\nprice:",costupto200)
    else:
        unitprice2=10
        costabove200=costof200+((temp-200)*unitprice2)
        print("price:",costabove200)
    
#Output:
ENter no units:350
price: 2000'''

'''#24)Write a program to display the last digit of a number.
num=259
print(num%10)
#Output:9'''

'''#25)Write a program to check whether the last digit of a number( entered by user ) is divisible by 3 or not. 
num=int(input("Enter:"))
last=num%10
if last%3==0:
    print(num,"last number divisable with 3")
else:
    print(num,"last number not divisable with 3")

#Output:
Enter:876
876 last number divisable with 3'''

##26) Write a program to accept percentage from the user and display the grade according to the following criteria: 
##        Marks                                    Grade 
##         > 90                                 A 
##         > 80 and <= 90                       B 
##        >= 60 and <= 80                       C 
##         below 60                             D 

'''marks=int(input("Enter:"))
if marks>90:
    print("A")
elif marks >80 and marks <= 90:
    print("B")
elif marks >=60 and marks <= 80:
    print("C")
else:
    print("D")
#Output:
Enter:72
C'''

'''##27) Write a program to accept the cost price of a bike and display the road tax to be paid
##    according to the following criteria : 
##        Cost price (in Rs)                                       Tax 
##        > 100000                                                  15 % 
##        > 50000 and <= 100000                          10% 
##        <= 50000                                                  5% 

price=int(input("Enter:"))
if price <= 50000:
    print("Tax :",price*0.05)
elif price > 50000 and price <= 100000:
    print("Tax :",price*0.1)
else:
    print("Tax :",price*0.15)
#Output:
    Enter:25000
Tax : 1250.0'''

#28 Write a program to check whether an years is leap year or not.

'''year=int(input("Enetr year"))
if year%4==0:
    print("Leaf Year")
else:
    print("no a leaf year")'''

##Output:
##Enetr year2020
##Leaf Year

#29)Write a program to accept a number from 1 to 7 and display the name of
#   the day like 1 for Sunday , 2 for Monday and so on.
'''
num=int(input("Enter:"))
if num==1:
    print("sunday")
elif num==2:
    print("monday")
elif num==3:
    print("tuesday")
elif num==4:
    print("wedday")
elif num==5:
    print("thursday")
elif num==6:
    print("friday")
elif num==7:
    print("saturday")
else:
    print("ener number between 1 to 7")
    '''
##Output:
##Enter:6
##friday
#30.Write a program to accept a number from 1 to 12 and display name of the month and days in that month like 1 for January and number of days 31 and so on 
'''

number=int(input("Enter your month:"))

if number==1:
    print("\tJanuary")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,32):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()

elif number==2:
    print("\tFebuary")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,29):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()
            
elif number==3:
    print("\tMarch")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,32):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()

elif number==4:
    print("\tApril")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,31):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()

elif number==5:
    print("\tMay")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,32):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()              
    
elif number==6:
    print("\tjune")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,31):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()


elif number==7:
    print("\tjuly")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,32):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()

elif number==8:
    print("\tAugust")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,32):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()
elif number==9:
    print("\tSeptember")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,31):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()

elif number==10:
    print("\tOctober")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,32):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()

elif number==11:
    print("\tNovember")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,32):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()

elif number==12:
    print("\tDecember")
    print("Sun \tMon \tTues \tWed \tThus \tFri \tSat")
    for i in range(1,32):
        print(i,end='\t')
        if i in (7,14,21,28):
            print()
else:
    print("ENTER VALUE IN 1  TO 12 ONLY")
'''
##OUTPUT:
##Enter your month:
##9
##	September
##Sun 	Mon 	Tues 	Wed 	Thus 	Fri 	Sat
##1	2	3	4	5	6	7	
##8	9	10	11	12	13	14	
##15	16	17	18	19	20	21	
##22	23	24	25	26	27	28	
##29	30

#31. What do you mean by statement?

Ans:A statement is a instruction that a python interpreter execute

#32. Write the logical expression for the following: A is greater than B and C is greater than D ?
'''
a=int(input("enter:"))
b=int(input("enter:"))
c=int(input("enter:"))
d=int(input("enter:"))

if (a>b) and (c>d):
    print("{} is > {} and {} > {}".format(a,b,c,d))
else:
    print("{} is > {} and {} > {}".format(b,a,d,c))
'''
###output:
##enter:5
##enter:1
##enter:2
##enter:5
##1 is > 5 and 5 > 2



#================================================================================================== 


##33. Accept any city from the user and display monument of that city. 
##
## City            Monument 
##
##    Delhi           Red Fort 
##
##    Agra            Taj Mahal 
##
##    Jaipur          Jal Mahal    

'''
name=input("enter your favorate city:")

if name=="Delhi":
    print("Red Fort")
elif name=="Agra":
    print("Taj Mahal")
elif name=="Jaipur":
    print("Jal Mahal")'''

##output:
##enter your favorate city:Delhi
##        Red Fort



#34. Write the output of the following if 
"""a = 7
if (a > 5 and a <=10):
    print("Hello")
else:     
    print("Bye") """

#output:
        # Hello
 

#35)Write a program to check whether a number entered is three digit number or not.
'''num=int(input("enter the data"))
store=0
c=0
while(num>0):
    rem=num%10
    store=rem+store*10
    num=num//10
    c=c+1
if c==3:
    print("3 digit number")
else:
    print("Not 3 digit number")'''
##Output
##enter the data569
##3 digit number


#36. Write a program to check whether a person is eligible for voting or not.(voting age >=18)?
'''
age=int(input("Enter age:"))

if age>=18:
    print("Eligible for vote")
else:
    print(" not eligible for vote")
'''
###output:
##enter age:69
##Eligible for vote


#37. Write a program to check whether a person is senior citizen or not?
'''       
age=int(input("Enter age:"))

if age>=60:
    print("senior citizen")
else:
    print(" not senior citizen")
'''
###output:
##enter age:19
##not senior citizen

       
#38. Write a program to find the lowest number out of two numbers excepted from user?
'''
a=int(input("enter  first number:"))
b=int(input("enter  second number:"))

if (a<b):
    print("lowest number  is {} out of two number {} and {}".format(a,a,b))
elif (b<a):
    print("lowest number  is {} out of two number {} and {}".format(b,a,b))
'''
##Output:
##enter  first number:15
##enter  second number:42
##lowest number  is 15 out of two number 15 and 42
        
#39. Write a program to find the largest number out of two numbers excepted from user?
'''
a=int(input("enter  first number:"))
b=int(input("enter  second number:"))

if (a>b):
    print("largest number  is {} out of two number {} and {}".format(a,a,b))
elif (b>a):
    print("largest number  is {} out of two number {} and {}".format(b,a,b))


enter  first number:15
enter  second number:42
largest number  is 42 out of two number 15 and 42
'''
##Output:
##enter  first number:154
##enter  second number:42
##largest number  is 154 out of two number 154 and 4
        


#40. Write a program to check whether a number (accepted from user) is positive or negative?
'''
a=int(input("enter number:"))

if a>0:
    print("Positive")
else:
    print("Negative")'''
##Output:
##enter number:5
##Positive


#41. Write a program to check whether a number is even or odd?
'''
a=int(input("enter  number:"))

if a%2==0:
    print("Even",a)
else:
    print("Odd",a)
'''
##Output:
##enter  number:6
##Even 6       

#42)Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.
'''num=int(input("enter the data"))
if num%2==0 and num%3==0:
    print(num,"divisable by 2 and 3")
else:
    print(num,"Not divisable by 2 and 3")'''
##Output:
##enter the data12
##12 divisable by 2 and 3


#43. Write a program to find the largest number out of three numbers excepted from user?
'''
a=int(input("enter number:"))
b=int(input("enter number:"))
c=int(input("enter number:"))

if (a>b) and (a>c):
    print("largest:",a)
elif (b>a) and (b>c):
    print("largest:",b)
else :
    print("largest:",c)'''

##Output:
##enter number:5
##enter number:9
##enter number:4
##largest: 9
        
#44. Accept the temperature in degree Celsius of water and check whether
#   it is boiling or not (boiling point of water in 100 oC?)
'''
temp=int(input("enter in celsius:"))

if temp>=100:
    print("boiling point of water in 100 oC")
else:
    print("water is not boiling ")
'''
##output:
##enter in celsius :85
##water  not boiling 

#45)the age of 4 people and display the youngest one and oldest one? Accept
'''ls=[int(x) for x in input().split(",")]
print(ls)
for i in range(0,len(ls)-1):
    temp=0
    for j in range(i,len(ls)):
        if ls[i]>ls[j]:
            temp=ls[i]
            ls[i]=ls[j]
            ls[j ]=temp
print("Yongest age:",ls[1])
print("Oldest age:",ls[-1])
'''
##Output:
##24,35,15,22
##[24, 35, 15, 22]
##Yongest age: 22
##Oldest age: 35

#46)Accept the following from the user and calculate the percentage of class attended: 
#   a.Total number of working days 
#   b.Total number of days for absent
#After calculating percentage show that, If the percentage is less than 75,
#than student will not be able to sit in exam.
'''
dic={}
workdays=int(input("Total working days"))
while True:
    student=input("student_name")
    if student == "":
        break
    else:
        absent=int(input("ENter absent days"))
        present_days=workdays-absent
        percent=(present_days/workdays)*100
        dic[student]=percent
print(dic)
for k,v in dic.items():
    if v < 75:
        print(k,"will not be able to sit in exam")'''
##Output:
##Total working days100
##student_namehari
##ENter absent days20
##student_nameramu
##ENter absent days30
##student_namesomu
##ENter absent days40
##student_namemannu
##ENter absent days45
##student_name
##{'hari': 80.0, 'ramu': 70.0, 'somu': 60.0, 'mannu': 55.00000000000001}
##ramu will not be able to sit in exam
##somu will not be able to sit in exam
##mannu will not be able to sit in exam

'''47)Accept three sides of a triangle and check whether it is an equilateral, isosceles or scalene triangle. 
Note : 
An equilateral triangle is a triangle in which all three sides are equal. 
A scalene triangle is a triangle that has three unequal sides. 
An isosceles triangle is a triangle with (at least) two equal sides.'''
side1=int(input("Enter side:"))
side2=int(input("Enter side:"))
side3=int(input("Enter side:"))

'''side=[int(x) for x in input().split(",")]
print(side)'''
if side1==side2==side3:
    print("equilateral triangle")
elif side1!=side2==side3:
    print("isosceles triangle")
elif side2!=side3==side1:
    print("isosceles triangle")
elif side3!=side1==side2:
    print("isosceles triangle")
else:
    print("scalene triangle")
##
##Output:
##Enter side:5
##Enter side:5
##Enter side:5
##equilateral triangle
    
    


    












    
    
























