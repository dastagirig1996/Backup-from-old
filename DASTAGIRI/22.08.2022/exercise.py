#1.With a given integral number n, write a program to generate a dictionary that contains (i, i**3)
#  such that is an integral number between 1 and n (both included).
# and then the program should print the dictionary.
#output: 1:1  2:8 3:27... depends on the given number
'''
dic={x:x**3 for x in range(1,int(input("enter"))+1)}
for k,v in dic.items():
    print(k,':',v,end="  ")
'''

##OUTPUT:
## 1 : 1  2 : 8  3 : 27  4 : 64  5 : 125

#2. WAP to find hexa format of decimal number, the decimal number is taken from the user

##ex:- input: 25
##     output: 19
##          and
##     input:5
##     output: 5
'''
Hexa_number=hex(int(input("enter number")))
print(Hexa_number)
'''
##Output:
    
##enter number25
##0x19

##enter number5
##0x5

#3.Write a program to merge two string, two string elements taken from the user?
## input: str1=abr
##        str2=ka
##    output: akbar
'''
str1='abr'
str2='ka'
str3=""

c=0
l1=len(str1)
l2=len(str2)

if l2>l1:
    str1,str2=str2,str1

while c<l1:
    str3=str3+str1[c]
    if c<l2:
        str3=str3+str2[c]
    c=c+1
print(str3)
'''

##Output:
##akbar





















               
   
