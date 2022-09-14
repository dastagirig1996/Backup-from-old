#1. WAP to find the target value of 5 in the given list of 1,5,7,8,90,6,and 23 elements?
'''ls=[1,5,7,8,90,6,23,]
target=int(input("Enyer:"))
for i in range(len(ls)):
    if target == ls[i]:
        print(ls[i],i," position")'''
##Output:
##Enyer:5
##5 1  position

#2.WAP to sort the given list of elements 1,5,7,8,90,6,and 23, without using sort() function?
'''ls=[1,5,7,8,90,6,23]
print("Before Sorting",ls)

for i in range(len(ls)-1):
    for j in range(i+1,len(ls)):
        if ls[i]>ls[j]:
            temp=0
            temp=ls[i]   
            ls[i]=ls[j]
            ls[j]=temp
            
print("After Sorting",ls)'''

##Output:
##Before Sorting [1, 5, 7, 8, 90, 6, 23]
##After Sorting [1, 5, 6, 7, 8, 23, 90]

#3. WAP to calcalte the compound interest of 3 years with the priciple amount of RS:10000 and
#   rate of return is 5 percentage for annum.
#   and display the total amount to pay on  the end of the year.?
'''Formula
A = P(1 + \(r/n))^nt
A	=	final amount
P	=	initial principal balance
r	=	interest rate
n	=	number of times interest applied per time period
t	=	number of time periods elapsed

t=3
p = 10000
r = 5
c=0
while c<t:
    c=c+1
    CI =p*((1+5/100)**c)
    print(CI)'''

##Output:
##10500.0
##11025.0
##11576.25000000000

#Q4.WAP in python remove all characters from a string except
#integers(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )
'''
STR="H56U1E9JIG3l4w2"
for i in STR:
    if i.isdigit():
        print(i,end='')'''
##Output:
##5619342

#5. WAP to take a list and find the possition of the item .(eg=  [45,12,66,2,33] if i take 66 then it shows the index 2)
'''
ls=[45,12,66,2,33]
num=int(input("enter number"))
for i in range(len(ls)-1):
    if num==ls[i]:
        print("index is : ",i)'''

##enter number66
##index is :  2






















        
