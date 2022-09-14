 #1.Write a Python class to convert an integer to a roman numeral
'''
class roman:
    def convert_integer_to_roman(self,number):
        val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        sym =  ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]
        roman_num =' '
        i=0
        while number>0:
            div = number//val[i]
            number = number%val[i]
            while div:
                roman_num+=sym[i]
                div = div-1
            i = i+1
        return roman_num
number = int(input("enter the value: "))
print(roman().convert_integer_to_roman(number))

#output:
enter the value: 78
 LXXVIII'''

#2. Write a Python class to convert a roman numeral to an integer.
'''class integer:
    def convert_roman_to_integer(self,roman):
        numerals ={'I':1,'v':5,'x':10,'L':50,'C':100,'D':500,'M':1000}
        value = 0
        for i in range(len(roman)):
            z= numerals[roman[i]]
            if (i+1)<len(roman)and numerals[roman[i+1]]>z:
                value -= z
            else:
                value += z
          val = [1000, 900, 500, 400,100, 90, 50, 40,10, 9, 5, 4,1]
        sym =  ["M", "CM", "D", "CD","C", "XC", "L", "XL","X", "IX", "V", "IV","I"]  
                
        return value
roman = input("enter the value: ")
print(integer().convert_roman_to_integer(roman))


#OUTPUT:enter the value: L
50'''

#3.Write a Python class to find validity of a string of parentheses, '(', ')', '{', '}', '[' and '].
#These brackets must be close in the correct order, for example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid.
'''class parantheses:
    def string_parantheses(self,str):
        b=[]
        para = {'(':')','[':']','{':'}'}
        for i in str:
            if i in para:
                b.append(i)
            elif(b == 0)or para[b.pop()]!=i:
                return false
        return len(b)==0
print(parantheses().string_parantheses("(){}[]"))

#output:True'''
#4.Write a Python class to get all possible unique subsets from a set of distinct integers.
#Input : [4, 5, 6]
#Output : [[], [6], [5], [5, 6], [4], [4, 6], [4, 5], [4, 5, 6]]

'''class subsets:
    def unique_subsets(self,numbers):
        result =[[]]
        for num in numbers:
            result += [i +[num] for i in result]
        return result
numbers = [4,5,6]
print(subsets().unique_subsets(numbers))

#output:[[], [4], [5], [4, 5], [6], [4, 6], [5, 6], [4, 5, 6]]'''

#5.Write a Python class to find a pair of elements (indices of the two numbers) from a given array
#whose sum equals a specific target number.
#Input: numbers= [10,20,10,40,50,60,70], target=50
#Output: 3, 4
'''
class TwoSum:  
    def __init__(self, list1, target):  
        self.list1 = list1  
        self.target = target  
          
    def solution(self):  
        length = len(list1)  
          
        for i in range(length-1):  
            for j in range(i+1, length):  
                if list1[i]+list1[j] == self.target:  
                    new_list = i, j  
                    return list(new_list)
        return -1
  
  
list1 = [10,20,10,40,50,60,70]  
target = 50 
obj = TwoSum(list1, target)  
print(obj.solution())  
                

#output:[0,3]'''

#6.Write a Python class to find the three elements that sum to zero from a set of n real numbers.
#Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
#Output : [[-10, 2, 8], [-7, -3, 10]]
'''class py_solution:
 def threeSum(self, nums):
        nums, result, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            j, k = i + 1, len(nums) - 1
            while j < k:
                if nums[i] + nums[j] + nums[k] < 0:
                    j += 1
                elif nums[i] + nums[j] + nums[k] > 0:
                    k -= 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j, k = j + 1, k - 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1
            i += 1
            while i < len(nums) - 2 and nums[i] == nums[i - 1]:
                i += 1
        return result

print(py_solution().threeSum([-25, -10, -7, -3, 2, 4, 8, 10]))

#output:[[-10, 2, 8], [-7, -3, 10]]'''


#7.Write a Python class to implement pow(x, n).
'''class py_solution:
   def pow(self, x, n):
        if x==0 or x==1 or n==1:
            return x 

        if x==-1:
            if n%2 ==0:
                return 1
            else:
                return -1
        if n==0:
            return 1
        if n<0:
            return 1/self.pow(x,-n)
        val = self.pow(x,n//2)
        if n%2 ==0:
            return val*val
        return val*val*x

print(py_solution().pow(2, -3));
print(py_solution().pow(3, 5));
print(py_solution().pow(100, 0));


#output:0.125
243
1 '''
#8.Write a Python class to reverse a string word by word.
#Input string : 'hello .py'
#Expected Output : '.py hello'
'''class py_solution:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))


print(py_solution().reverse_words('hello .py'))
        
#output:.py hello'''
#9.Write a Python class which has two methods get_String and print_String.
#get_String accept a string from the user and print_String print the string in upper case.
'''class IOString():
    def __init__(self):
        self.str1 = ""

    def get_String(self):
        self.str1 = input()

    def print_String(self):
        print(self.str1.upper())

str1 = IOString()
str1.get_String()
str1.print_String()

#output:supraja
SUPRAJA'''

#10.Write a Python class named Rectangle constructed by a length and width and a
#method which will compute the area of a rectangle.

'''class Rectangle():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def rectangle_area(self):
        return self.length*self.width

newRectangle = Rectangle(12, 10)
print(newRectangle.rectangle_area())

#output:120'''
































































