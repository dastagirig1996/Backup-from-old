##1.Python Program to Print the Natural Numbers Summation Pattern
##
##Python Program to Print the Natural Numbers Summation Pattern
##
##Output:
##
##Case 1:
##Enter a number: 4
##1 = 1
##1 + 2 = 3
##1 + 2 + 3 = 6
##1 + 2 + 3 + 4 = 10
## 
##Output:
##
##Case 2:
##Enter a number: 5
##1 = 1
##1 + 2 = 3
##1 + 2 + 3 = 6
##1 + 2 + 3 + 4 = 10
##1 + 2 + 3 + 4 + 5 = 15

'''
n=int(input("Enter a number: "))
for j in range(1,n+1):
    a=[]
    for i in range(1,j+1):
        print(i,sep=" ",end=" ")
        if(i<j):
            print("+",sep=" ",end=" ")
        a.append(i)
    print("=",sum(a))
 
print()
'''
##Output:
##Enter a number: 5
##1 = 1
##1 + 2 = 3
##1 + 2 + 3 = 6
##1 + 2 + 3 + 4 = 10
##1 + 2 + 3 + 4 + 5 = 15












































