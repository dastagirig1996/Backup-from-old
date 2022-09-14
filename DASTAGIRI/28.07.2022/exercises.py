#Q1.WAP in python arrange string characters such that lowercase letters should come first
'''name='PRoGraMInG'
lower=''
upper=''
for ch in name:
    if ch.islower():
        lower+=ch
    else:
        upper+=ch
add=lower+upper
print(add)'''

##Output:
##oranPRGMIG

#Q2.WAP to print sum of prime numbers in given list input :- 2 4 5 6 7 3 8 output :- 17
'''ls=[2,4,5,6,7,3,8]
sums=0
for i in ls:
    for j in range(2,i):
        if i%j==0:
            break
    else:
        sums=sums+i
print(sums)'''

##Output:
##17

#Q3.when do we use nested for loop.Write an example.
'''nested for loop is used when we are trying to iterate multiple arrays which are dependent on each other.
    neste[45,12,66,2,33]d loop took more time to execute 

for i in range(1,5):
    for j in range(1,5):
        print(i,"*",j,"=",i*j)
    print()'''

##Output:
##1 * 1 = 1
##1 * 2 = 2
##1 * 3 = 3
##1 * 4 = 4
##
##2 * 1 = 2
##2 * 2 = 4
##2 * 3 = 6
##2 * 4 = 8
##
##3 * 1 = 3
##3 * 2 = 6
##3 * 3 = 9
##3 * 4 = 12
##
##4 * 1 = 4
##4 * 2 = 8
##4 * 3 = 12
##4 * 4 = 16

#Q4.WAP in python remove all characters from a string except integers
#(ex:- STR="H56U1E9JIG3l4w2" ,o/p:-5619342(only display integers) )

'''numbers=("0123456789")
st="H56U1E9JIG3l4w2"
digits=''
for ch in st:
    if ch in numbers:
       print(int(ch),end="")'''

##Output:
##5619342

#Q5.WAP to take a list and find the possition of the item .
#(eg=  [45,12,66,2,33] if i take 66 then it shows the index 2)
'''
ls=[45,12,66,2,33]
num=int(input("Enter:"))
for i in range(len(ls)):
    if ls[i]==num:
        print(i)'''
        
##Output:
##Enter:33
##4
        
        



























    
    
