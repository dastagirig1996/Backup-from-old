##1.Use a list comprehension to square each odd number in a list. The list is input by a sequence of
##comma-separated numbers.
##Suppose the following input is supplied to the program:
##1,2,3,4,5,6,7,8,9
##Then, the output should be:
##1,3,5,7,9

'''
ls=[i for i in list(map(int,input().split(","))) if i%2!=0]
print(ls)
'''

##Output:
##1,2,3,4,5,6,7,8,9
##[1, 3, 5, 7, 9]

##2.Write a program that computes the net amount of a bank account based a transaction log from console input.
##  The transaction log format is shown as following:
##D 100
##W 200
##D means deposit while W means withdrawal.
##Suppose the following input is supplied to the program:
##D 300
##D 300
##W 200
##D 100
##Then, the output should be:
##500
'''
def transaction_inputs():
    number_of_trans=int(input("Enter number of trnsactions"))
    list_trans=[]
    for trans in range (number_of_trans):
        trans=input("Enter the transaction details ")
        list_trans.append(trans)
    return list_trans

def account():
    account_balance=0
    for i in transaction_inputs():
        if i[0]=="W":
            account_balance-=int(i[1:])
        elif i[0]=="D":
            account_balance+=int(i[1:])
    return account_balance
print(account())
'''
##Output:
##Enter number of trnsactions4
##Enter the transaction details D 500
##Enter the transaction details D 300
##Enter the transaction details W 600
##Enter the transaction details D 1000
##1200


##3.You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string,
##  age and height are numbers. The tuples are input by console. The sort criteria is:

##1: Sort based on name;
##2: Then sort based on age;
##3: Then sort by score.

##The priority is that name > age > score.
##If the following tuples are given as input to the program:
##Tom,19,80
##John,20,90
##Jony,17,91
##Jony,17,93
##Json,21,85

##Then, the output of the program should be:
##[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]

'''
people_info = []
while True:
    individual_info = input()

    if individual_info == "":
        break
    else:
        people_info.append(tuple((individual_info.split(","))))

people_info.sort(key =  itemgetter(0, 1, 2))       
print(people_info)
'''

##Output:
##Tom,19,80
##John,20,90
##Jony,17,91
##Jony,17,93
##Json,21,85
##
##[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]
##


##4.Define a function that can receive two integral numbers in string form and compute their sum and then
##  print it in console.
'''
def sum(a,b):
    c=int(a)+int(b)
    return c
a=input("enter")
b=input("enter")
print(sum(a,b))
'''


##Output:
##enter5
##enter6
##11


    
##5.Define a function that can convert a integer into a string and print it in console.
'''
def convert(number):
    return str(number)

print(convert(5),type(convert(5)))
'''
##Output:
##5 <class 'str'>


##6.Define a function that can accept two strings as input and print the string with maximum length in console.
##  If two strings have the same length, then the function should print all strings line by line.

'''
def max_length(s1,s2):
    if len(s1)>len(s2):
        print(s1)
    elif len(s2)>len(s1):
        print(s2)
    else:
        print(s1,"\n",s2,)
        
s1=input("Enter")
s2=input("Enter")
        
max_length(s1,s2)

'''

##Output:
##Enterhello
##Enterworld
##hello 
## world


##7.Define a function that can accept an integer number as input and print the "It is an even number"
##  if the number is even, otherwise print "It is an odd number".

'''
def type_of_number(n):
    if n%2==0:
        print("It is an even number")
    else:
        print("It is an odd number")
        
type_of_number(int(input("enter number")))
'''

##Output:
##enter number6
##It is an even number


##8.Define a function which can print a dictionary where the keys are numbers between 1 and 20 (both included)
##  and the values are square of keys.

'''
def square():
    dic={i:i**2 for i in range(1,21)}
    return dic
print(square())
'''

##Output:
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225,
## 16: 256, 17: 289, 18: 324, 19: 361, 20: 400}


##9.Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
##  and the values are square of keys. The function should just print the values only.
'''
def square():
    dic={i:i**2 for i in range(1,21)}
    return dic.values()
print(square())
'''

##Output:
##dict_values([1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400])


##10.Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
##   and the values are square of keys. The function should just print the keys only.
'''
def square():
    dic={i:i**2 for i in range(1,21)}
    return dic.keys()
print(square())
'''
##Output:
##dict_keys([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])



##11.Define a function which can generate and print a list where the values are square of numbers between 1 and 20
##  (both included).

'''
def square():
    ls=[i**2 for i in range(1,21)]
    return ls
print(square())
'''


##Output:
##[1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400]



##12.Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included)
#    Then the function needs to print the first 5 elements in the list.
'''
def square():
    ls=[i**2 for i in range(1,21)]
    return ls[:5]
print(square())
'''
##Output:
##[1, 4, 9, 16, 25]


##13.Define a function which can generate and print a tuple where the value are square of numbers between 1 and 20
#    (both included).
'''
def square():
    ls=[i**2 for i in range(1,21)]
    return tuple(ls)
print(square())
'''
##Output:
##(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400)


##14.With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program to print the first half values in one line and
##   the last half values in one line.

'''
def Tuple(tp):
    print(tp[:len(tp)//2],"\n",tp[len(tp)//2:])
tp=(1,2,3,4,5,6,7,8,9,10)
Tuple(tp)
'''
##Output:
##(1, 2, 3, 4, 5) 
## (6, 7, 8, 9, 10)


##15.Write a program to generate and print another tuple whose values are even numbers in the given
##  tuple (1,2,3,4,5,6,7,8,9,10).

'''
def Tuple(tp):
    ls=[x for x in list(tp) if x%2==0]
    return tuple(ls)
tp=(1,2,3,4,5,6,7,8,9,10)
print(Tuple(tp))
'''

##Output:
##(2, 4, 6, 8, 10)


##16.Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes",
##   otherwise print "No".

'''
def Define(st):
    if st.isupper() or st.islower() or st.istitle():
        print("Yes")
    else:
        print("No")
st=input()
Define(st)
'''

##Output:
##Hello
##Yes
##HELLO
##Yes
##hello
##Yes
##HEllo
##No



##17.Write a program to solve a classic ancient Chinese puzzle: 
##We count 35 heads and 94 legs among the chickens and rabbits in a farm.
# How many rabbits and how many chickens do we have?

'''
def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    
    if(heads>=legs):
        print(error_msg)
    elif(legs%2!=0):
        print(error_msg)
    else:
        rabbit_count=(legs-2*heads)/2
        chicken_count=heads-rabbit_count
        print(int(chicken_count),int(rabbit_count))

solve(35,94)
'''

##Output:
##23 12






























