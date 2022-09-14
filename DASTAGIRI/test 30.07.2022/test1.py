#1. Write a program to swap given two numbers without temporary variable.
'''p=20
q=30
p=p+q
q=p-q
p=p-q
print("After swapping p:{},q:{}".format(p,q))'''

#2. Write a program to accept 4 numbers from command prompt add them using two variables. 

'''ls= [int(x) for x in input("enter four numbers with comma...").split(",")]
sums=0
for num in ls:
    sums=sums+num
print(sums)'''

##Output:
##enter four numbers with comma...1,2,3,4
##10


##Output:
##    After swapping p:30,q:20


##3. Write a program which accepts an int values as command line argument and    print the next multiple of 100. 
##
##    Ex: Input: 35 
##
##    Output: 100 
##
##    Input: 435 
##
##    Output: 500

##num=int(input("Enter number"))
##original=num
##addition=0
##size=len(str(num))
##while num>(size-1):
##    rem=num%10
##    addition=addition*10+rem
##    num=num//10
##size1=len(str(addition))
##print(addition)
##store=0
##while addition>size1:
##    rem1=addition%10
##    store=store*10+rem1
##    addition=addition//10
##print(store)
##print(original)
##differ=original-store
##print(differ)
##result=differ+original
##print(result)

##st=str(num).split(",")
##print(st)



## 4.Write a program ThreeDPalindrome 
## In this program accept a 3 digit integer as a command line argument and return the String true
## if the integer is a Palindrome or the String false otherwise
'''num=int(input("Enter number"))
original=num
reverse=0
while num>0:
    rem=num%10
    reverse=reverse*10+rem
    num=num//10
if original==reverse:
    print("true")
else:
    print("false")'''

##Output:
##Enter number525
##true

#5.Write a python program for printing Fibonacci series.
'''n=10
frist=1
second=2
count=0
while count<n:
    print(frist)
    nextelemt=frist+second
    frist=second
    second=nextelemt
    count=count+1'''

#6.Python Program to Find Armstrong Number in an Interval 
'''start=int(input("Enter number"))
end=int(input("Enter number"))
list_of_numbers=[]
for num in range(start,end+1):
    original=num
    addition=0
    size=len(str(num))
    while(num>0):
        rem=num%10
        mul=rem**size
        addition=addition+mul
        num=num//10
    if original==addition:
        list_of_numbers.append(original)    
print(list_of_numbers)'''

##Output:
##Enter number100
##Enter number1000
##[153, 370, 371, 407]

##7. Write a python  program on SumOfDigits, which accepts a two digit number
##   as command line argument and prints the sum of its digits.  
##
##Ex: Input: 35  
##
##Output: 8  
##
##Input: 88  
##
##Output: 16 
'''num=int(input("Enter number"))
addition=0
while(num>0):
        rem=num%10
        addition=addition+rem
        num=num//10
print(addition)'''

##Output:
##Enter number35
##8

#8. Write a python program EvenOrOdd, which accepts a whole number as command line argument and prints “Even Number”
#  if the number is Even and prints “Odd Number” if the number is Odd. If the input
'''num=int(input("Enter number"))
if num%2==0:
    print('Even Number')
else:
    print('Odd Number')'''
    
##Output:
##Enter number5
##Odd Number

#
#9. Write a python program Rounder, which accepts a whole number as command line argument and prints the same number
# if the input is Odd. If the input is even, it should print the next multiple of ten.
# If the input is not a number or is negative, print the string:“Error”.  
#Input: 44, output: 50 
#Input: 45, output: 45
'''num=int(input("Enter number"))
if num>0:
    if num%2==0:
        rem=num%10
        addition=10-rem
        result=num+addition
        print(result)
    else:
        print(num)
else:
    print("Error")'''

##Output:
##Enter number62
##70

#10. Write a python program DigitChecker, which accepts a two digit number as command line argument and prints Zero
#    if the digits are same and if the two digits are different, it prints their difference.  
#Ex: Input:52  
#Output:3  
#Input:88  
#O
'''original=num
addition=0
ls=[]
while(num>0):
        rem=num%10
        ls.append(rem)
        num=num//10

if ls[0]==ls[1]:
    print("0")
elif ls[0]>ls[1]:
    differ1=ls[0]-ls[1]
    print(differ1)
elif ls[0]<ls[1]:
    differ2=ls[1]-ls[0]
    print(differ2)'''

##Output:
##Enter number63
##3

#12.  Write a python program StarPattern, which accepts a number as command line argument and prints the following output:  

##Input: 4 
##Output:  
##
##*   
##
##*  *   
##
##*  *  *   
##
##*  *  *  * 
'''import sys
rows=int(input("Enter rows"))
if rows>0:
    for rows in range(1,rows+1):
        for columns in range(1,rows+1):
            print("*",end=" ")
        print()
else:
    print("error")
    sys.exit'''

##Output:
##Enter rows4
##* 
##* * 
##* * * 
##* * * * 

#14.Write a python  program on Prime numbers
num=int(input("Enter number"))
ls=[]
for i in range(1,num+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        ls.append(i)
print(ls)
##
##Output:
##Enter number100
##[1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

