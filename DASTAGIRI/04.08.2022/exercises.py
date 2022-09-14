##1.write a python program to print the pattern
##        * 
##       * * 
##      * * * 
##     * * * * 
##    * * * * * 
##   * * * * * * 
##    * * * * * 
##     * * * * 
##      * * * 
##       * * 
##        *

n = int(input("enter number: "))
for i in range(1,n+1):
    spaces = " " * (n- i)
    stars = "* " * i
    print(spaces + stars)

k = n -1
for i in range(1, k+1):
    spaces = " " * i
    stars = "* " * (n - i)
    print(spaces + stars)

##Output:
##enter number: 5
##    * 
##   * * 
##  * * * 
## * * * * 
##* * * * * 
## * * * * 
##  * * * 
##   * * 
##    * 




#2.How would you check if each word in a string begins with a capital letter?
'''
st="The expression Can also contain Conditions, not like A filter, but as a Way to manipulate The Outcome"

ls=st.split(" ")
for ch in ls:
    if ch.istitle():
        print(ch)
'''
##Output:
##The
##Can
##Conditions,
##A
##Way
##The
##Outcome

#3.Write a Python program that prints all the numbers from 0 to 6 except 4 and 5.
'''for i in range(0,7):
    if i==4 or i==5:
        continue
    else:
        print(i)
'''
##Output:
##0
##1
##2
##3
##6

#4.Print list of elements and store in a another list and print  reverse order of list 
'''
ls=[1,2,3,4,5,6]
ls1=ls.copy()
print(ls1)
print(ls1[::-1])
'''
##Output:
##[1, 2, 3, 4, 5, 6]
##[6, 5, 4, 3, 2, 1]

#5.write a python program to print the pattern
##            A  
##           B C  
##          D E F  
##         G H I J  
##        K L M N O  
##       P Q R S T U

a = int(input("enter the number: "))
count = 65
k = 2*(a)-2
for i in range(0,a):
    for j in range(0,k):
        print(end = " ")
    k = k-1
    for j in range(0,i+1):
        alpha = chr(count)
        print(alpha,end =" ")
        count += 1
    print(" ")


#output:
##enter the number: 6
##          A  
##         B C  
##        D E F  
##       G H I J  
##      K L M N O  
##     P Q R S T U  




