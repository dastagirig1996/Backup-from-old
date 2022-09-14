#1. Write a Python program to triple all numbers of a given list of integers. Use Python map.

'''
ls=[1,2,5,3,4,6]

new_list=list(map(lambda x:x**3,ls))
print(new_list)

'''



#2. Write a Python program to add three given lists using Python map and lambda.
'''
ls1=[2,5,4,7]
ls2=[4,7,8,5]
ls3=[7,4,78,5]
print(list(map(lambda x,y,z:x+y+z,ls1,ls2,ls3)))
'''


##Output:
##[13, 16, 90, 17]

#3. Write a Python program to listify the list of given strings individually using Python map

'''
color = ['Red', 'Blue', 'Black', 'White', 'Pink'] 
print("Original list: ")
print(color) 
print("\nAfter listify the list of strings are:") 
color2=list(map(list,color))
print(color2)
'''

##Output:
##After listify the list of strings are:
##[['R', 'e', 'd'], ['B', 'l', 'u', 'e'], ['B', 'l', 'a', 'c', 'k'], ['W', 'h', 'i', 't', 'e'], ['P', 'i', 'n', 'k']]

##4. Write a Python program to create a list containing the power of said number in bases raised to the
##   corresponding number in the index using Python map

'''
bases_num = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Base numbers abd index: ")
print(bases_num)
print(index)
result = list(map(pow, bases_num, index))
print("\nPower of said number in bases raised to the corresponding number in the index:")
print(result)
'''


##Output:
##Base numbers abd index: 
##[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
##[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##
##Power of said number in bases raised to the corresponding number in the index:
##[10, 400, 27000, 2560000, 312500000, 46656000000, 8235430000000, 1677721600000000, 387420489000000000, 100000000000000000000]


#5. Write a Python program to square the elements of a list using map() function

'''
ls=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sqr=list(map(lambda x:x*x,ls))
print(sqr)
'''


##Output:
##[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


##6. Write a Python program to convert all the characters in uppercase and lowercase and eliminate duplicate letters
##   from a given sequence. Use map() function.

'''
def change_cases(s):
  return str(s).upper(), str(s).lower()
 
chrars = {'a', 'b', 'E', 'f', 'a', 'i', 'o', 'U', 'a'}
print("Original Characters:\n",chrars)
 
result = map(change_cases, chrars)
print("\nAfter converting above characters in upper and lower cases\nand eliminating duplicate letters:")
print(set(result))
'''

##Output:
##After converting above characters in upper and lower cases
##and eliminating duplicate letters:
##{('F', 'f'), ('A', 'a'), ('U', 'u'), ('I', 'i'), ('O', 'o'), ('E', 'e'), ('B', 'b')}

#7. Write a Python program to add two given lists and find the difference between lists. Use map() function.

'''
def addition_subtrction(x, y):
    return x + y, x - y
 
nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]
print("Original lists:")
print(nums1)
print(nums2)
result = map(addition_subtrction, nums1, nums2)
print("\nResult:")
print(list(result))
'''

##Output:
##Result:
##[(6, 6), (6, 4), (10, -4), (16, 2)

#7. Write a Python program to add two given lists and find the difference between lists. Use map() function.

'''
def add_subscrib(x,y):
    return x+y,x-y

nums1 = [6, 5, 3, 9]
nums2 = [0, 1, 7, 7]

differ=map(add_subscrib,nums1,nums2)
print(list(differ))
'''


##Output:
##[(6, 6), (6, 4), (10, -4), (16, 2)]


#8. Write a Python program to convert a given list of integers and a tuple of integers in a list of strings

'''
nums1 = [6, 5, 3, 9]
nums2 = (0, 1, 7, 7)
res=list(map(str,nums1))
print(res)
res2=list(map(str,nums2))
print(res2)
'''

##Output:
##['6', '5', '3', '9']
##['0', '1', '7', '7']

#9. Write a Python program to create a new list taking specific elements from a tuple and convert a string value
##  to integer.

'''
student_data  = [('Alberto Franco','15/05/2002','35kg'), ('Gino Mcneill','17/05/2002','37kg'),
                 ('Ryan Parkes','16/02/1999', '39kg'), ('Eesha Hinton','25/09/1998', '35kg')]


stu_name=list(map(lambda x:x[0],student_data))
stu_bod=list(map(lambda x:x[1],student_data))
stu_weight=list(map(lambda x:int(x[2][:-2]),student_data))

print(stu_name)
print(stu_bod)
print(stu_weight)
'''

##Output:
##['Alberto Franco', 'Gino Mcneill', 'Ryan Parkes', 'Eesha Hinton']
##['15/05/2002', '17/05/2002', '16/02/1999', '25/09/1998']
##[35, 37, 39, 35]


#10. Write a Python program to compute the square of first N Fibonacci numbers, using map function and generate
##   a list of the numbers.

'''
import itertools
n = 10
def fibonacci_nums(x=0, y=1):
    yield x
    while True:
        yield y
        x, y = y, x + y
print("First 10 Fibonacci numbers:")
result = list(itertools.islice(fibonacci_nums(), n))
print(result)
square = lambda x: x * x 
print("\nAfter squaring said numbers of the list:")
print(list(map(square, result)))
'''


##Output:
##First 10 Fibonacci numbers:
##[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
##
##After squaring said numbers of the list:
##[0, 1, 1, 4, 9, 25, 64, 169, 441, 1156]

#11. Write a Python program to compute the sum of elements of a given array of integers, use map() function.

'''
from array import array
def array_sum(nums_arr):
    sum_n = 0
    for n in nums_arr:
        sum_n += n
    return sum_n

nums = array('i', [1, 2, 3, 4, 5, -15])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = array_sum(nums_arr)
print("Sum of all elements of the said array:")
print(result)
'''

##Output:
##Original array: array('i', [1, 2, 3, 4, 5, -15])
##Sum of all elements of the said array:
##0

#12. Write a Python program to find the ration of positive numbers, negative numbers and zeroes in an array of integers

'''
from array import array

def plusMinus(nums):
    n = len(nums)
    n1 = n2 = n3 = 0
    
    for x in nums:
        if x > 0:
            n1 += 1
        elif x < 0:
            n2 += 1
        else:
            n3 += 1
            
    return round(n1/n,2), round(n2/n,2), round(n3/n,2)

nums = array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
print("Original array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)
nums = array('i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
print("\nOriginal array:",nums)
nums_arr = list(map(int, nums))
result = plusMinus(nums_arr)
print("Ratio of positive numbers, negative numbers and zeroes:")
print(result)
'''


##Output:
##Original array: array('i', [0, 1, 2, -1, -5, 6, 0, -3, -2, 3, 4, 6, 8])
##Ratio of positive numbers, negative numbers and zeroes:
##(0.54, 0.31, 0.15)
##
##Original array: array('i', [2, 1, 2, -1, -5, 6, 4, -3, -2, 3, 4, 6, 8])
##Ratio of positive numbers, negative numbers and zeroes:
##(0.69, 0.31, 0.0)


#13. Write a Python program to count the same pair in two given lists. use map() function.

'''
from operator import eq
def count_same_pair(nums1, nums2):
    result = sum(map(eq, nums1, nums2))
    return result

nums1 = [1,2,3,4,5,6,7,8]
nums2 = [2,2,3,1,2,6,7,9]

print(nums1)
print(nums2)
print(count_same_pair(nums1, nums2))
'''


##Output:
##[1, 2, 3, 4, 5, 6, 7, 8]
##[2, 2, 3, 1, 2, 6, 7, 9]
##4


#14.Write a Python program to interleave two given list into another list randomly using map() function.

'''
import random
def randomly_interleave(nums1, nums2):
    result =  list(map(next, random.sample([iter(nums1)]*len(nums1) + [iter(nums2)]*len(nums2), len(nums1)+len(nums2))))
    return result
nums1 = [1,2,7,8,3,7]
nums2 = [4,3,8,9,4,3,8,9]
 
print(nums1)
print(nums2)
print(randomly_interleave(nums1, nums2))
'''

##Output:
##[1, 2, 7, 8, 3, 7]
##[4, 3, 8, 9, 4, 3, 8, 9]
##[4, 1, 3, 8, 2, 7, 9, 8, 3, 4, 3, 8, 9, 7]


#15. Write a Python program to split a given dictionary of lists into list of dictionaries using map function.


'''
def list_of_dicts(marks):
    result = map(dict, zip(*[[(key, val) for val in value] for key, value in marks.items()]))
    return list(result)
marks = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
print(marks)
print(list_of_dicts(marks))
'''


##Output:
##{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
##[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84},
##{'Science': 95, 'Language': 80}]


#16. Write a Python program to convert a given list of strings into list of lists using map function.

'''
def strings_to_listOflists(str):
    result = map(list, str)
    return list(result)

colors = ["Red", "Green", "Black", "Orange"]
print(colors)
print(strings_to_listOflists(colors))
'''

##OutputT:
##['Red', 'Green', 'Black', 'Orange']
##[['R', 'e', 'd'], ['G', 'r', 'e', 'e', 'n'], ['B', 'l', 'a', 'c', 'k'], ['O', 'r', 'a', 'n', 'g', 'e']]



#17. Write a Python program to convert a given list of tuples to a list of strings using map function

'''
def tuples_to_list_string(lst):
    result = list(map(' '.join, lst))
    return result   
colors = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
names = [('Sheridan','Gentry'), ('Laila','Mckee'), ('Ahsan','Rivas'), ('Conna','Gonzalez')]
print(tuples_to_list_string(names))
'''


##OUtput:
##['Sheridan Gentry', 'Laila Mckee', 'Ahsan Rivas', 'Conna Gonzalez']
##
































































