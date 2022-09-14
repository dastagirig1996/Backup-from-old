'''Problem statement

Python Program to accept three distinct digits and print all possible combinations from the digits
Case 1:
Enter first number:1
Enter second number:2
Enter third number:3
1 2 3
1 3 2
2 1 3
2 3 1
3 1 2
3 2 1

Case 2:
Enter first number:5
Enter second number:7
Enter third number:3
5 7 3
5 3 7
7 5 3
7 3 5
3 5 7
3 7 5'''

num1=int(input("Enter numer1:"))
num2=int(input("Enter numer2:"))
num3=int(input("Enter numer3:"))
ls=[]
ls.append(num1)
ls.append(num2)
ls.append(num3)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            if (i!=j and j!=k and k!=i):
                print(ls[i],ls[j],ls[k])
##Output:
##Enter numer1:5
##Enter numer2:8
##Enter numer3:3
##5 8 3
##5 3 8
##8 5 3
##8 3 5
##3 5 8
##3 8 5
