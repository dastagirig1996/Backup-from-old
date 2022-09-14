##1. Write a program to print the following Patterns
##  1 2 3 4 5 
##  1 2 3 4 5  
##  1 2 3 4 5 
##  1 2 3 4 5 
##  1 2 3 4 5
'''
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()'''

##Output:
##1 2 3 4 5 
##1 2 3 4 5 
##1 2 3 4 5 
##1 2 3 4 5 
##1 2 3 4 5

##2.Write a program to print the following Pattern
##  5 4 3 2 1 
##  5 4 3 2 1
##  5 4 3 2 1
##  5 4 3 2 1
##  5 4 3 2 1 
'''
for i in range(1,6):
    for j in range(5,0,-1):
        print(j,end=" ")
    print()
    '''
##Output:
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1

##3.Write a program to print the following Pattern
##  5 5 5 5 5 
##  4 4 4 4 4 
##  3 3 3 3 3 
##  2 2 2 2 2 
##  1 1 1 1 1
'''
for i in range(5):
    for j in range(5,0,-1):
        print(j,end=" ")
    print()
''' 
#Output:
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1 
##5 4 3 2 1

##4.Write a program to print the following Pattern
##  1
##  1 2
##  1 2 3
##  1 2 3 4
##  1 2 3 4 5
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()'''

##Output:
##1 
##1 2 
##1 2 3 
##1 2 3 4 
##1 2 3 4 5

##5.Write a program to print the following Pattern
##  1 
##  2 2 
##  3 3 3 
##  4 4 4 4 
##  5 5 5 5 5
'''
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()'''
##Output:
##1 
##2 2 
##3 3 3 
##4 4 4 4 
##5 5 5 5 5

##6.Write a program to print the following Pattern
##  1 
##  2 3  
##  4 5 6 
##  7 8 9 10 
##  11 12 13 14 15
'''
t=1
for i in range(1,6):
    for j in range(1,i+1):       
        print(t,end=" ")
        t=t+1
    print()
'''
##Output:
##1 
##2 3 
##4 5 6 
##7 8 9 10 
##11 12 13 14 15

##7.Write a program to print the following Pattern

##5 
##4 4 
##3 3 3 
##2 2 2 2 
##1 1 1 1 1
'''
t=5
for i in range(1,6):
    for j in range(1,i+1):
        print(t,end=" ")
    print()
    t=t-1'''
    
##Output:
##5 
##4 4 
##3 3 3 
##2 2 2 2 
##1 1 1 1 1 
    
##8.Write a program to print the following Pattern
##  1 
##  2 3 
##  3 4 5 
##  4 5 6 7 
##  5 6 7 8 9
'''
t=1
for i in range(1,6):
    for j in range(1,i+1):
        print(t,end=" ")
        t=t+1
    print()
    t=t-1'''
    
##Output:
##1 
##1 2 
##2 3 4 
##4 5 6 7 
##7 8 9 10 11 

##
##9.Write a program to print the following Pattern
##  A 
##  B C
##  D E F
##  G H I J
##  K L M N O
'''
c=65
for i in range(5):
    for j in range(i+1):
        print(chr(c),end=" ")
        c=c+1
    print()'''
    
##Output:
##A 
##B C 
##D E F 
##G H I J 
##K L M N O 

##10.Write a program to print the following Pattern
##   * * * * * 
##   * * * * * 
##   * * * * * 
##   * * * * * 
##   * * * * *
'''
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()'''

##Output:
##* * * * * 
##* * * * * 
##* * * * * 
##* * * * * 
##* * * * * 

##11.Write a program to print the following Pattern
##   * 
##   * * 
##   * * * 
##   * * * * 
##   * * * * *
'''
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
'''

##Output:
##* 
##* * 
##* * * 
##* * * * 
##* * * * *

##12.Write a program to print the following Pattern
##    * * * * * 
##    *       * 
##    *       * 
##    *       * 
##    * * * * * 
'''n=5
for i in range(0,n):
    for j in range(0,n):
        if i==0 or i==n-1:
            print("*",end=" ")
        elif j==0 or j==n-1:
            print("*",n*" ",end=" ")
    print()'''

##Output:
##* * * * * 
##*       *       
##*       *       
##*       *       
##* * * * *

##13.Write a program to print the following Pattern
##          * 
##        * * * 
##      * * * * * 
##    * * * * * * *
'''
a=1
for i in range(5,0,-1):
    print(' '*i,end='')
    for j in range(1,5+1):
        print("* "*a,end=' ')
        a=a+1
        break
    print()'''
##Output:
##     *  
##    * *  
##   * * *  
##  * * * *  
## * * * * *

#14.Display Multiplication Table in given range using Nested for loops
'''for i in range(1,2+1):
    for j in range(1,10+1):
        print(i,"*",j,"=",i*j)
    print()'''
##Output:
##1 * 1 = 1
##1 * 2 = 2
##1 * 3 = 3
##1 * 4 = 4
##1 * 5 = 5
##1 * 6 = 6
##1 * 7 = 7
##1 * 8 = 8
##1 * 9 = 9
##1 * 10 = 10
##
##2 * 1 = 2
##2 * 2 = 4
##2 * 3 = 6
##2 * 4 = 8
##2 * 5 = 10
##2 * 6 = 12
##2 * 7 = 14
##2 * 8 = 16
##2 * 9 = 18
##2 * 10 = 20

#15.Display Prime Numbers in the given range using nested for loops 
'''
for i in range(2,100):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=' ')'''
##Output:
#2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97 

###16.Write a program to print the following Pattern
##	      1
##        3   2
##    6   5   4
##10  9   8   7
'''
t=1
s=3

for i in range(1,5):
    print(' '*s**2,end=' ')
    l=[]
    for j in range(1,i+1):
        #print(t,end=' ')
        l.append(t)
        t=t+1
    for i in range(len(l)-1,-1,-1):
        print(l[i],end=" ")
        
    s=s-1
    
    print() 
'''
##17.Write a program to print the following Pattern
##10  9  8   7
##      6   5  4
##           3  2
##               1
'''
t=10
s=0
for i in range(4,0,-1):
    print(' '*s**2,end=' ')
    for j in range(1,i+1):
        print(t,end=' ')
        t-=1
    s=s+1
    print()'''

##Output:
##10 9 8 7 
##  6 5 4 
##     3 2 
##       1











  

