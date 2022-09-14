#1)Python Program to Print an Inverted Star Pattern.?
"""
Case 1:
Enter number of rows: 5
*****
 ****
  ***
   **
    *
 
Case 2:
Enter number of rows: 10
**********
 *********
  ********
   *******
    ******
     *****
      ****
       ***
        **
         *
"""

#Main Program
"""
number=int(input("Enter your number:"))
s=0
for i in range(number,0,-1):
    print(" "*s,end=' ')
    s+=1
    print("*"*i)"""




#2)Python Program to Print an Identity Matrix.?

#Main Program
"""
dim=int(input("Enter your 2/2 matrix size:"))
lst=[]
for i in range(dim):
    lst1=[]
    for j in range(dim):
        if i==j:
            lst1.append(1)
        else:
            lst1.append(0)
    lst.append(lst1)
#matrix display
for i in lst:
    for j in i:
        print(j,end=' ')
    print()
"""
  
#output:
"""
Enter your 2/2 matrix size:3
1 0 0 
0 1 0 
0 0 1
"""



#3)String Palindrome Program in Python.?

#Main program
"""
str1=input("Enter your word:")
rev=str1[-1::-1]
if str1==rev:
    print("palindrom:",rev)
else:
    print("Not a palindrom:",rev)
"""

#output:
"""
Enter your word:madam
palindrom: madam


Enter your word:ramesh
Not a palindrom: hsemar
"""



