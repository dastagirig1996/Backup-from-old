#1>Python Program to Convert Bytes to a String

'''
b='hyderabad'
print(b)
print(type(b))

b1=b'banglore'
print(type(b1))
b1=b1.decode()
print(type(b1))

Output:
hyderabad
<class 'str'>
<class 'bytes'>
<class 'str'>
'''


#2>Python Program to Remove Duplicate Element From a List 

'''
lst=[1,5,2,4,10,20,5,2,20,4]
lst1=[]
for i in lst:
    if i not in lst1:
        lst1.append(i)
print(lst1)

Output:
[1, 5, 2, 4, 10, 20]
'''


#3>Python Program to Check If Two Strings are Anagram

'''
st='listen'
st1='silent'

if sorted(st)==sorted(st1):
    print('{} and {} are Anagram'.format(st,st1))
else:
    print('{} and {} are Not Anagram'.format(st,st1))

Output:
listen and silent are Anagram
'''


#4>Python Program to Count the Number of Digits Present In a Number

'''
num=input('Enter any number: ')
count=0
for i in num:
    count=count+1
print(count)
    
'''

#OR

'''
num=input('Enter any number: ')
count=0
for i in num:
    if '0' in i:
        count=count+1
print(count)

Output:
Enter any number: 20304050
4
'''


#5>Python Program to Trim Whitespace From a String

'''
st='  string    '
print(st.strip())

Output:
string
'''

#6>Python Program to Differentiate Between type() and isinstance()

'''
num=1234
print(type(num))

st='Hello'
lst=[1,2,3,4]
print(isinstance(st,str))
print(isinstance(lst,set))

Output:
<class 'int'>
True
False
'''

#7>Python Program to Delete an Element From a Dictionary 

'''
d={'name':'sai','age':25,'id':22166}
d.popitem()
print(d)

d1={1:'sai',2:'Nani',3:'Raju'}
del d1[1]
print(d1)

d2={2:'sai',4:'Nani',6:'Raju'}
del d2[4]
print(d2)

Output:
{'name': 'sai', 'age': 25}
{2: 'Nani', 3: 'Raju'}
{2: 'sai', 6: 'Raju'}
'''

#8>Python Program to Count the Occurrence of an Item in a List 

'''
lst=[10,20,30,40,50,10,20,30,20]
count=0
for i in lst:
    if i==20:
        count=count+1
print(count)

'''
#OR
'''
print(lst.count(20))
'''

#9>Python Program to Randomly Select an Element From the List 

'''
import random
lst=[2,3,4,5,6,'sai','nani']
print(random.choice(lst))

Output:
nani
2
'''


#10>Python Program to Get the Last Element of the List 

'''
lst=[2,3,5,6,7,8,'Object',25,24]
print(lst[-1])

Output:
24
'''


#11>Python Program to Check if a Key is Already Present in a Dictionary 

'''
d={'name':'kamal','age':26,'add':'hyd'}
if 'age' in d:
    print('present in dict')
else:
    print('Not in dict')

Output:
present in dict
'''

#12>Python Program to Iterate Over Dictionaries Using for Loop 

'''
d={'name':'kamal','age':26,'address':'hyd','id':22166}
for i in d:
    print(i,d[i])
'''
#OR
'''    
d={'name':'kamal','age':26,'address':'hyd','id':22166}
d1=d.items()
for i in d1:
    print(i)
'''

#13>Python Program to Flatten a Nested List 
'''
lst=[[1], [2, 3], [4, 5, 6, 7],[8,9,10]]
lst1=[]
for i in lst:
    for j in i:
        lst1.append(j)
print(lst1)

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

#OR

'''
lst=[[1], [2, 3], [4, 5, 6, 7],[8,9,10]]
print(list(j for i in lst for j in i))

Output:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''


#14>Python Program to Sort Words in Alphabetic Order 

'''
st='hello hi Good Morning how are you doing'
st=st.lower()
st=st.split(' ')
st.sort()
for i in st:
    print(i)

Output:
are
doing
good
hello
hi
how
morning
you
'''

#15>Python Program to Remove Punctuations From a String 
'''
st='he@#llo^% $go}[]o{d mor)(n$*ing'
punctuations='!@#$%^&*(){]{}[-<>?\|/'
for i in st:
    if i not in punctuations:
        print(i, end='')

Output:
hello good morning
'''

#16>Python Program to Convert Decimal to Binary Using Recursion 

'''
def convertdectobin(n):
    if n>1:
        convertdectobin(n//2)
    print(n%2, end='')
n=int(input('Enter any number: '))
convertdectobin(n)

Output:
Enter any number: 35
100011
'''

#17>Python Program to Find Sum of Natural Numbers Using Recursion 

'''
def sumofnaturalnums(n):
    sum1=0
    for i in range(1,n+1):
        sum1=sum1+i
    print(sum1)
n=int(input('Enter any number: '))
sumofnaturalnums(n)

Output:
Enter any number: 10
55
'''

#Using recursion

'''
def sumofnaturalnums(n):
    if n<=1:
        return n
    else:
        return n + sumofnaturalnums(n-1)
n=int(input('Enter any number: '))
print(sumofnaturalnums(n))
'''

#18>Python Program to Display Fibonacci Sequence Using Recursion 

'''
n=int(input('Enter any number: '))
n1=0
n2=1
count=0
if n==0:
    print('Enter valid number')
elif n==1:
    print('The sequence number',n)
else:
    print('The fibonacci series')
while n>count:
    print(n1, end=',')
    n3=n1+n2
    n1=n2
    n2=n3
    count=count+1
Output:
Enter any number: 11
The fibonacci series
0,1,1,2,3,5,8,13,21,34,55,
'''

#Fibonacci using recursion
'''
def fibonaccirecursion(n):
    if n<=1:
        return 1
    else:
        return (fibonaccirecursion(n-1)+fibonaccirecursion(n-2))
n=int(input('Enter any number: '))
if n<=0:
    print('Enter valid number')
else:
    print('The fibonacci series is: ',)
    for i in range(n):
        print(fibonaccirecursion(i),end=',')

Output:
Enter any number: 10
The fibonacci series is: 
1,1,2,3,5,8,13,21,34,55,
'''

#19>Python Program to Find the Factors of a Number 

'''
n=int(input('Enter any number: '))
for i in range(1,n+1):
    if n%i==0:
        print(i)
'''
#OR
'''
def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(i)
n=int(input('Enter any number: '))
factors(n)

Output:
Enter any number: 100
1
2
4
5
10
20
25
50
100
'''
#20>Python Program to Find the Sum of Natural Numbers 

'''
n=int(input('Enter any number: '))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)

Output: 55
'''

#21>Python Program to Check Armstrong Number 

'''
num=int(input('Enter any number: '))
sum=0
temp=num
while temp>0:
    digit=temp%10
    sum=sum+digit**3
    temp=temp//10
if num==sum:
    print(num,'Armstrong')
else:
    print(num,'Not Armstrong')

Output:
Enter any number: 153
153 Armstrong
'''

#22>Python Program to Print the Fibonacci sequence 

'''
n=int(input('Enter any number: '))
n1=0
n2=1
count=0
if n==0:
    print('Enter valid number')
elif n==1:
    print('The sequence of number is',n)
else:
    print('The fibonacci series is: ')
while count<n:
    print(n1, end=',')
    n3=n1+n2
    n1=n2
    n2=n3
    count=count+1

Output:
Enter any number: 11
The fibonacci series is: 
0,1,1,2,3,5,8,13,21,34,55,
'''

#23>Python Program to Find the Largest Among Three Numbers 

'''
n1=int(input('Enter first number: '))
n2=int(input('Enter second number: '))
n3=int(input('Enter third number: '))
if n1>n2 and n1>n3:
    print('{} is greater than {} and {}'.format(n1,n2,n3))
elif n2>n3 and n2>n1:
    print('{} is grater than {} and {}'.format(n2,n1,n3))
elif n3>n1 and n3>n2:
    print('{} is greater than {} and {}'.format(n3,n1,n2))
else:
    print('Three numbers are equal')

Output:
Enter first number: 50
Enter second number: 90
Enter third number: 140
140 is greater than 50 and 90
'''

#24>Python Program to Generate a Random Number 

'''
import random
print(random.randint(0,25))
'''
##Output:
##17
##11


#25>Python Program to Check Whether a Number is Palindrome or Not 

'''
num=input('Enter any number: ')
num1=str(num)[::-1]
if num==num1:
    print('Palindrome number')
else:
    print('Not Plindrome number')

Output:
Enter any number: 9669
Palindrome number

Enter any number: 145
Not Plindrome number

Enter any number: 121
Palindrome number
'''

















