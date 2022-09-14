#1.Python Program to Check Whether a Given Number is Even or Odd using Recursion

'''
def check(n):
    if (n < 2):
        return (n % 2 == 0)
    return (check(n - 2))
n=int(input("Enter number:"))
if(check(n)==True):
      print("Number is even!")
else:
      print("Number is odd!")


Output:

Enter number:6
Number is even!


'''

#2.Python Program to Find Sum of Digit of a Number using Recursion

'''
l=[]
def sum_digits(b):
    if(b==0):
        return l
    dig=b%10
    l.append(dig)
    sum_digits(b//10)
n=int(input("Enter a number: "))
sum_digits(n)
print(sum(l))

Output:

Enter a number: 123
6
'''

#3.Python Program to Calculate the Power using Recursion

'''
def power(base,exp):
    if(exp==1):
        return(base)
    if(exp!=1):
        return(base*power(base,exp-1))
base=int(input("Enter base: "))
exp=int(input("Enter exponential value: "))
print("Result:",power(base,exp))

Output:

Enter base: 25
Enter exponential value: 2
Result: 625
