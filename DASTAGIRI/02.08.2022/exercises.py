#1.Calculate income tax for the given income by adhering to the below rules
""" Taxable Income    Rate (in %)
    First $10,000     0
    Next $10,000      10
    The remaining     20
    
Expected Output:

For example, suppose the taxable income is 45000 the income tax payable is

10000*0% + 10000*10%  + 25000*20% = $6000. ? """

'''
while True:
    n=int(input("Enter amount:"))
    if (n>0) and (n<=10000):
        print("not tax to pay:0")
    elif (n>10000) and (n<=20000):
        r=(n-10000)
        print("your tax will be :",int((10/100)*r))
    elif (n>20000):
        r=(n-10000)
        p=10000
        t=(r-10000)
        t1=int((10/100)*p)
        
        t2=int((20/100)*t)
        
        print("tax will be:",t1+t2)'''

##Output:
##
##Enter amount:10000
##not tax to pay:0
##
##Enter amount:20000
##your tax will be : 1000
##
##Enter amount:35000
##tax will be: 4000
##
##Enter amount:45000
##tax will be: 6000





#2.Count the length of list with out using any inbuilt function.?

ls=[int(x) for x in input().split()]
c=0
for i in ls:
    c=c+1
print("length:",c)

##Output:
##454466
##length: 1


#3.Write a Python program to create a histogram from a given list of integers.?

##4. Take input from user and if input is string print String
##if input is integer/float print integer
##if input is mix of string and integer print Error
##HINT Can be done using ASCII code

'''inpt=input("Enter the string ")
int_counter=0
str_counter=0
for i in inpt:
    if ord(i)>48 and ord(i)<57:
        int_counter+=1
    elif (ord(i)>97 and ord(i)<122) or (ord(i)>65 and ord(i)<90) :
        str_counter+=1

if int_counter >0 and str_counter ==0:
    print("Integer")
elif int_counter == 0 and str_counter >0:
    print("String")
else:
    print("Error")'''
    
##Output:
##Enter the string ghbgbdRF
##String

#5.Python program to check if a string is palindrome or not?
'''
ip=input("enter word:")
r=ip[::-1]
if r==ip:
    print("palindrome")
else:
    print("not palindrome")
    '''
##Output:
##palindrome

