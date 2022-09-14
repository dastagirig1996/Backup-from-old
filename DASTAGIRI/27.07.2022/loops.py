#1.Accept 10 numbers from the user and display their average.
'''
n=10
total=0
for i in range(n) :
    num=int(input("enter the num = "))
    total=total+num
    
average =total/n
print(average)
'''
##
##Output:
##enter the num = 5
##enter the num = 5
##enter the num = 1
##enter the num = 4
##enter the num = 47
##enter the num = 746
##enter the num = 47
##enter the num = 4
##enter the num = 4
##enter the num = 47
##91.0


#2.Write a program to display sum of odd numbers and even numbers that fall between 12 and 37(including both numbers)
'''
n1=10
n2=15
sum1=0
sum2=0
for i in range(n1,n2+1):
    if i%2==0 :
        sum1+=i
    else :
        sum2+=i

print(sum1)
print(sum2)
'''
##Output:
##36
##39
#3.Write a program to display all the numbers which are divisible by 11 but not by 2 between 100 and 500.
'''
for i in range(100,500):
    if i%11==0 and i%2!=0:
        print(i,end=" ")'''

##Output:
##121 143 165 187 209 231 253 275 297 319 341 363 385 407 429 451 473 495 

#4.Write a program to print numbers from 1 to 20 except multiple of 2 & 3
'''for i in range(1,21):
    if i%2!=0 and i%3!=0:
        print(i,end=" ")'''
##Output:
##1 5 7 11 13 17 19

#5.Write a program that keep on accepting number from the user until user enters Zero.
#  Display the sum and average of all the numbers. 
'''
n=1
count=1
sum_1=0
while n>0 :
    num=int(input("enter num = "))
    if num==0 :
        break
    else :
        sum_1+=num
        average=sum_1/count
    count+=1    
print(sum_1)
print(average)
'''
##Output:
##enter num = 5
##enter num = 5
##enter num = 84
##enter num = 25
##enter num = 0
##119
##29.75


#6.Write a program to accept decimal number and display its binary number. 
'''num=int(input("ENter:"))
st=''
while num>0:
    rem=num%2
    if rem==0:
        st=st+str(rem) 
    else:
        st=st+str(rem)
    num=num//2
binary_num=st[::-1]
print(binary_num)'''



##Output:
##ENter:36
##100100


#7.Convert the following loop into for loop : 

##x = 4 
##
##while(x<=8): 
##
##    print(x*10) 
##
##    x+=2
'''
x=4
for i in range(1,x+1):
    if x<=8:
        print(x*10)
    x=x+2
'''
##Output:
##40
##60
##80

#8.What is nested loop?

#A loop inside the loop is called nested loop     


#9.Write a program to convert temperature in Fahrenheit to Celsius.
'''
n=int(input("enter num of farheheit to celisuius = "))

formula=(n-32)*(5/9)
celsius=formula
print(celsius," celsius")
'''      
##Output:
##enter num of farheheit to celisuius = 42
##5.555555555555555  celsius
#10.Write a Python program to get the Fibonacci series between 0 to 50.
'''
list_a=[]

n1=0
n2=1
for i in range(50):
    nth=n1+n2
    print(n1)
    n1=n2
    n2=nth                      
    if n1 > 89 :
        break
'''
##Output:
##0
##1
##1
##2
##3
##5
##8
##13
##21
##34
##55
##89

#11.Write a Python program which iterates the integers from 1 to 50.
##For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz".
##For numbers which are multiples of both three and five print "Fizz Buzz". 
'''
for i in range(1,51):
    if i%3==0 and i%5!=0:
        print("Fizz")
    elif i%5==0 and i%3!=0:
        print("Buzz")
    elif i%3==0 and i%5==0:
        print("Fizz Buzz")
    else:
        print(i)
'''
##Output:
##1
##2
##Fizz
##4
##Buzz
##Fizz
##7
##8
##Fizz
##Buzz
##11
##Fizz
##13
##14
##Fizz Buzz
##16
##17
##Fizz
##19
##Buzz
##Fizz
##22
##23
##Fizz
##Buzz
##26
##Fizz
##28
##29
##Fizz Buzz
##31
##32
##Fizz
##34
##Buzz
##Fizz
##37
##38
##Fizz
##Buzz
##41
##Fizz
##43
##44
##Fizz Buzz
##46
##47
##Fizz
##49
##Buzz

##12.Write a Python program that prints all the numbers from 0 to 6 except 3 and 6. 
##Note : Use 'continue' statement. 
##Expected Output : 0 1 2 4 5
'''
for i in range(6+1):
    if i==3 or i==6:
        continue
    print(i)
'''
#Output:
##0
##1
##2
##4
##5












