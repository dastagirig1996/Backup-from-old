#1.Write a program to get all vowels from given string
'''st="aeiou"
string=input("enter: ")
for vowels in st:
  if vowels in string:
    print(vowels)'''

##Output:
##enter: hello good morning
##e
##i
##o

#2.Write a program to calculate the simple interest
'''p=int(input("enter principal amount:"))
t=int(input("enter yeras:"))
r=int(input("enter intrest"))
s=(p*t*r)/100
print(s)'''

##Output:
##enter principal amount:50000
##enter yeras:2
##enter intrest24
##24000.0

#3.Python Program to Find Sum of Series 1 + 1/2 + 1/3 + 1/4 + ……. + 1/N
'''num=int(input("Enter:"))
sums=1
for i in range(2,num+1):
  denom=1
  sums=sums+(denom/i)
print(sums)'''

##Output:
##Enter:5
##2.283333333333333

#4.Python Program to Find the Sum of the Series 1/1!+1/2!+1/3!+…1/N!
'''num=int(input("Enter:"))
sums=1
for i in range(2,num+1):
  denom=1
  mul=1
  for fact in range(1,i+1):
    mul=mul*fact
  sums=sums+(denom/mul)
print(sums)'''
##Output:
##Enter:5
##1.7166666666666668

#5.Python Program to Replace All Occurrences of ‘a’ with $ in a String
st='programing language'
for i in st:
  updat=i.replace("a","$")
  print(updat,end="")
##Output:
##progr$ming l$ngu$ge
