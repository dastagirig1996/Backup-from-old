##1. Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument,
##   also create a lambda function that multiplies argument x with argument y and print the result.
##Sample Output:
##25
##48

'''
add=lambda x:x+15
print(add(25))


multiply=lambda x,y:x*y
print(multiply(2,8))

'''


##Output:
##40
##16

##2. Write a Python program to create a function that takes one argument, and that argument will be multiplied
##   with an unknown given number. Go to the editor
##Sample Output:
##Double the number of 15 = 30
##Triple the number of 15 = 45
##Quadruple the number of 15 = 60
##Quintuple the number 15 = 75


'''
double=lambda x:x*2
print(double(15))
triple=lambda x:x*3
print(triple(15))
quadruple=lambda x:x*4
print(quadruple(15))
quintuple=lambda x:x*5
print(quintuple(15))
'''

##Output:
##30
##45
##60
##75

##3. Write a Python program to sort a list of tuples using Lambda.
##Original list of tuples:
##[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
##Sorting the List of Tuples:
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

'''
marks =[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]

marks.sort(key=lambda x:x[1])
print(marks)
'''

##Output:
##[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]


##4.Write a Python program to sort a list of dictionaries using Lambda. Go to the editor
##Original list of dictionaries :
##[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
##Sorting the List of dictionaries :
##[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]
'''
sort_model=[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]

sort_model.sort(key=lambda x:x['color'])
print(sort_model)

new_list=sorted(sort_model,key=lambda x:x['color'])

print(new_list)
'''

##Output:
##[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]
##[{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}]


##5. Write a Python program to filter a list of integers using Lambda. Go to the editor
##Original list of integers:
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##Even numbers from the said list:
##[2, 4, 6, 8, 10]
##Odd numbers from the said list:
##[1, 3, 5, 7, 9]

'''
ls=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even=list(filter(lambda x:x%2==0,ls))
print(even)

odd=list(filter(lambda x:x%2!=0,ls))
print(odd)
'''

##Output:
##[2, 4, 6, 8, 10]
##[1, 3, 5, 7, 9]

#6.  Write a Python program to square and cube every number in a given list of integers using Lambda.
##Original list of integers:
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##Square every number of the said list:
##[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
##Cube every number of the said list:
##[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]

'''
lst=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqr=list(map(lambda x:x*x,lst))
print(sqr)

cub=list(map(lambda x:x**3,lst))
print(cub)
'''

##Output:
##[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
##[1, 8, 27, 64, 125, 216, 343, 512, 729, 1000]


##7.Write a Python program to find if a given string starts with a given character using Lambda.
##Sample Output:
##True
##False

'''
st="environment"
find=lambda x:True if x.startswith('e') else False
print(find(st))

find=lambda x:True if x.startswith('k') else False
print(find(st))
'''


##Output:
##True
##False

##8. Write a Python program to extract year, month, date and time using Lambda. Go to the editor
##Sample Output:
##2020-01-15 09:03:32.744178
##2020
##1
##15
##09:03:32.744178

'''
import datetime
now=datetime.datetime.now()

year= lambda x:x.year
month= lambda x:x.month
day=lambda x:x.day
time=lambda x:x.time()
print(now)
print(year(now))
print(month(now))
print(day(now))
print(time(now))
'''


##Output:
##2022-08-25 15:37:02.563248
##2022
##8
##25
##15:37:02.563248

        
##9. Write a Python program to check whether a given string is number or not using Lambda.
##Sample Output:
##True
##True
##False
##True
##False
##True
##Print checking numbers:
##True
##True

'''
numb=lambda x: x.replace(".","").isdigit()
print(numb("522"))
print(numb("5.25"))
print(numb("-585"))
print(numb("f522"))
# for negative numbers
numb1=lambda r: numb(r[1:]) if r[0]=='-' else numb(r)  
print(numb1("-585"))
'''


##Output:
##True
##True
##False
##False
##True

##10. Write a Python program to create Fibonacci series upto n using Lambda.
##Fibonacci series upto 2:
##[0, 1]
##Fibonacci series upto 5:
##[0, 1, 1, 2, 3]
##Fibonacci series upto 6:
##[0, 1, 1, 2, 3, 5]
##Fibonacci series upto 9:
##[0, 1, 1, 2, 3, 5, 8, 13, 21]

'''
from functools import reduce
 
fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
 
print("Fibonacci series upto 2:")
print(fib_series(2))
print("\nFibonacci series upto 5:")
print(fib_series(5))
print("\nFibonacci series upto 6:")
print(fib_series(6))
print("\nFibonacci series upto 9:")
print(fib_series(9))
'''

#Output:

##Fibonacci series upto 2:
##[0, 1]
##
##Fibonacci series upto 5:
##[0, 1, 1, 2, 3]
##
##Fibonacci series upto 6:
##[0, 1, 1, 2, 3, 5]
##
##Fibonacci series upto 9:
##[0, 1, 1, 2, 3, 5, 8, 13, 21]


##11. Write a Python program to find intersection of two given arrays using
#     Lambda.
##Original arrays:
##[1, 2, 3, 5, 7, 8, 9, 10]
##[1, 2, 4, 8, 9]
##Intersection of the said arrays: [1, 2, 8, 9]

'''
ls =[1, 2, 3, 5, 7, 8, 9, 10]
ls1=[1, 2, 4, 8, 9]

intersec=list(filter(lambda x: x in ls,ls1))
print(intersec)
'''


##Output:
##[1, 2, 8, 9]


##12. Write a Python program to rearrange positive and negative numbers in a given array using Lambda.
##Original arrays:
##[-1, 2, -3, 5, 7, 8, 9, -10]
##Rearrange positive and negative numbers of the said array:
##[2, 5, 7, 8, 9, -10, -3, -1]

'''
array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
print("Original arrays:")
print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
print("\nRearrange positive and negative numbers of the said array:")
print(result)
'''


##Output:
##Original arrays:
##[-1, 2, -3, 5, 7, 8, 9, -10]
##
##Rearrange positive and negative numbers of the said array:
##[2, 5, 7, 8, 9, -10, -3, -1]


##13. Write a Python program to count the even, odd numbers in a given array of integers using Lambda.
##Original arrays:
##[1, 2, 3, 5, 7, 8, 9, 10]
##Number of even numbers in the above array: 3
##Number of odd numbers in the above array: 5

'''
num=[1, 2, 3, 5, 7, 8, 9, 10]
even_lt=len(list(filter(lambda n: (n%2==0),num)))
odd_lt=len(list(filter(lambda n: (n%2!=0),num)))

print("Number of even numbers in the above array:",even_lt)
print("Number of odd numbers in the above array:",odd_lt)
'''


##Output:
##Number of even numbers in the above array: 3
##Number of odd numbers in the above array: 5


##14. Write a Python program to find the values of length six in a given list using Lambda.
##Sample Output:
##Monday
##Friday
##Sunday

'''
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
  print(d)
'''

##Output:
##Monday
##Friday
##Sunday

##15. Write a Python program to add two given lists using map and lambda.
##Original list:
##[1, 2, 3]
##[4, 5, 6]
##Result: after adding two list
##[5, 7, 9]

'''
a=[1, 2, 3]
b=[4, 5, 6]

c=list(map(lambda x,y:x+y,a,b))
print(c)
'''


##Output:
##[5, 7, 9]

##16. Write a Python program to find the second lowest grade of any student(s) from the given names and
##grades of each student using lists and lambda. Input number of students, names and grades of each student.
##Input number of students: 5
##Name: S ROY
##Grade: 1
##Name: B BOSE
##Grade: 3
##Name: N KAR
##Grade: 2
##Name: C DUTTA
##Grade: 1
##Name: G GHOSH
##Grade: 1
##Names and Grades of all students:
##[['S ROY', 1.0], ['B BOSE', 3.0], ['N KAR', 2.0], ['C DUTTA', 1.0], ['G GHOSH', 1.0]]
##Second lowest grade: 2.0
##Names:
##N KAR

'''
students = []
sec_name = []
second_low = 0
n = int(input("Input number of students: "))
for _ in range(n):
   s_name = input("Name: ")
   score = float(input("Grade: "))
   students.append([s_name,score])
print("\nNames and Grades of all students:")
print(students)
order =sorted(students, key = lambda x: int(x[1]))
for i in range(n):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
print("\nSecond lowest grade: ",second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
print("\nNames:")
for s_name in sec_student_name:
   print(s_name)
'''

##Output:
##Input number of students: 5
##Name: somu
##Grade: 5
##Name: kiran
##Grade: 2
##Name: ramu
##Grade: 4
##Name: suresh
##Grade: 6
##Name: manish
##Grade: 7
##
##Names and Grades of all students:
##[['somu', 5.0], ['kiran', 2.0], ['ramu', 4.0], ['suresh', 6.0], ['manish', 7.0]]
##
##Second lowest grade:  4.0
##
##Names:
##ramu


##17. Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda. 
##Orginal list:
##[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
##Numbers of the above list divisible by nineteen or thirteen:
##[19, 65, 57, 39, 152, 190]

'''
ls=[19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

filt=list(filter(lambda x:(x%19==0 or x%13==0),ls))
print(filt)
'''


##Output:
##[19, 65, 57, 39, 152, 190]


##18. Write a Python program to find palindromes in a given list of strings using Lambda.

##Orginal list of strings:
##['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']
##List of palindromes:
##['php', 'aaa']

'''
ls=['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palin=list(filter(lambda x: (x=="".join(reversed(x))),ls))
print(palin)
'''

##Output:
##['php', 'aaa']


##19. Write a Python program to find all anagrams of a string in a given list of strings using lambda. Go to the editor
##Orginal list of strings:
##['bcda', 'abce', 'cbda', 'cbea', 'adcb']
##Anagrams of 'abcd' in the above string:
##['bcda', 'cbda', 'adcb']


'''
from collections import Counter  
texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
str = "abcd"
print("Orginal list of strings:")
print(texts) 
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
print("\nAnagrams of 'abcd' in the above string: ")
print(result)
'''


##Output:
##Orginal list of strings:
##['bcda', 'abce', 'cbda', 'cbea', 'adcb']
##
##Anagrams of 'abcd' in the above string: 
##['bcda', 'cbda', 'adcb']


##20. Write a Python program to find the numbers of a given string and store them in a list,
##display the numbers which are bigger than the length of the list in sorted form.
##Use lambda function to solve the problem.
##Original string: sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
##Numbers in sorted form:
##20 23 56

'''
str1 = "sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5"
print("Original string: ",str1)
str_num=[i for i in str1.split(' ')]
lenght=len(str_num)
numbers=sorted([int(x) for x in str_num if x.isdigit()])
print('Numbers in sorted form:')
for i in ((filter(lambda x:x>lenght,numbers))):
    print(i,end=' ')
'''


##Output:
##Original string:  sdf 23 safs8 5 sdfsd8 sdfs 56 21sfs 20 5
##Numbers in sorted form:
##20 23 56 


##21. Write a Python program that multiply each number of given list with a given number using lambda function.
##    Original list: [2, 4, 6, 9, 11]
##Given number: 2
##Result:
##4 8 12 18 22

'''
ls =[2, 4, 6, 9, 11]
n=2
multiply= list(map(lambda x:x*n,ls))

print(multiply)
'''

##OUtput:
##[4, 8, 12, 18, 22]

#22.Write a Python program that sum the length of the names of a given list of names after removing the names
##  that starts with an lowercase letter. Use lambda function
##Result:
##16

'''
sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
print("Result:")
print(len(''.join(sample_names)))
'''

##output
##Result:
##16


##23. Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers
##using lambda function. Go to the editor
##Original list: [2, 4, -6, -9, 11, -12, 14, -5, 17]
##Sum of the positive numbers: -32
##Sum of the negative numbers: 48
##Click me to see the sample solution

'''
ls=[2, 4, -6, -9, 11, -12, 14, -5, 17]

pos_numb=list(filter(lambda x: x>0,ls))
neg_numb=list(filter(lambda x: x<0,ls))

print(sum(pos_numb))
print(sum(neg_numb))
'''


##Output:
##48
##-32


##24. Write a Python program to find numbers within a given range where every number is divisible by every digit it contains. Go to the editor
##Sample Output:
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]

'''
def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
print(divisible_by_digits(1,22))
'''

##Output:
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]


#25.Write a Python program to create the next bigger number by rearranging the digits of a given number.
##Original number: 12
##Next bigger number: 21
##Original number: 10
##Next bigger number: False
##Original number: 201
##Next bigger number: 210
##Original number: 102
##Next bigger number: 120
##Original number: 445
##Next bigger number: 454

'''
def rearrange_bigger(n):
    #Break the number into digits and store in a list
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
n = 12
print("Original number:",n)
print("Next bigger number:",rearrange_bigger(n))

n = 10
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
      
n = 201
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 102
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
n = 445
print("\nOriginal number:",n)
print("Next bigger number:",rearrange_bigger(n))
'''


##Output:
##Original number: 12
##Next bigger number: 21
##
##Original number: 10
##Next bigger number: False
##
##Original number: 201
##Next bigger number: 210
##
##Original number: 102
##Next bigger number: 120
##
##Original number: 445
##Next bigger number: 454

#26. Write a Python program to find the list with maximum and minimum length using lambda.

##Original list:
##[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
##List with maximum length of lists:
##(3, [13, 15, 17])
##List with minimum length of lists:
##(1, [0])

'''
def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)
    
def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)
      
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("\nList with maximum length of lists:")
print(max_length_list(list1))
print("\nList with minimum length of lists:")
print(min_length_list(list1))
'''


#Output:
##Original list:
##[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
##
##List with maximum length of lists:
##(3, [13, 15, 17])
##
##List with minimum length of lists:
##(1, [0])

##27. Write a Python program to sort each sublist of strings in a given list of lists using lambda.
##Original list:
##[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
##After sorting each sublist of the said list of lists:
##[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]

'''
def sort_sublists(input_list):
    result = [sorted(x, key = lambda x:x[0]) for x in input_list] 
    return result
color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
print("\nOriginal list:")
print(color1)  
print("\nAfter sorting each sublist of the said list of lists:")
print(sort_sublists(color1))
'''

#Output:

##Original list:
##[['green', 'orange'], ['black', 'white'], ['white', 'black', 'orange']]
##
##After sorting each sublist of the said list of lists:
##[['green', 'orange'], ['black', 'white'], ['black', 'orange', 'white']]


##28. Write a Python program to sort a given list of lists by length and value using lambda.
##Original list:
##[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
##Sort the list of lists by length and value:
##[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

'''
def sort_sublists(input_list):
    result = sorted(input_list, key=lambda l: (len(l), l))
    return result
list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
print("Original list:")
print(list1)
print("\nSort the list of lists by length and value:")
print(sort_sublists(list1))
'''

##Output:
##Original list:
##[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
##
##Sort the list of lists by length and value:
##[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

#29. Write a Python program to find the maximum value in a given heterogeneous list using lambda.
##Original list:
##['Python', 3, 2, 4, 5, 'version']
##Maximum values in the said list using lambda:
##5

'''
def max_val(list_val):
     max_val = max(list_val, key = lambda i: (isinstance(i, int), i))  
     return(max_val)

list_val = ['Python', 3, 2, 4, 5, 'version'] 
print("Original list:")
print(list_val)
print("\nMaximum values in the said list using lambda:")
print(max_val(list_val))
'''

##Output:
##Original list:
##['Python', 3, 2, 4, 5, 'version']
##
##Maximum values in the said list using lambda:
##5


##30. Write a Python program to sort a given matrix in ascending order according to the sum of its rows using lambda.
##Original Matrix:
##[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
##Sort the said matrix in ascending order according to the sum of its rows
##[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
##Original Matrix:
##[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
##Sort the said matrix in ascending order according to the sum of its rows
##[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]
'''
def sort_matrix(M):
    result = sorted(M, key=lambda matrix_row: sum(matrix_row)) 
    return result

matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

print("Original Matrix:")
print(matrix1)
print("\nSort the said matrix in ascending order according to the sum of its rows") 
print(sort_matrix(matrix1))
print("\nOriginal Matrix:")
print(matrix2) 
print("\nSort the said matrix in ascending order according to the sum of its rows") 
print(sort_matrix(matrix2))
'''


##Output:
##Original Matrix:
##[[1, 2, 3], [2, 4, 5], [1, 1, 1]]
##
##Sort the said matrix in ascending order according to the sum of its rows
##[[1, 1, 1], [1, 2, 3], [2, 4, 5]]
##
##Original Matrix:
##[[1, 2, 3], [-2, 4, -5], [1, -1, 1]]
##
##Sort the said matrix in ascending order according to the sum of its rows
##[[-2, 4, -5], [1, -1, 1], [1, 2, 3]]



