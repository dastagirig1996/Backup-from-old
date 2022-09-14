##1.Write a Python program find a list of integers with exactly two occurrences of nineteen
##   and at least three occurrences of five.
##Input: 
##
##[19, 19, 15, 5, 3, 5, 5, 2] 
##
##Output: 
##
##True

'''
ls=[19, 19, 15, 5, 3, 5, 5, 2]
for i in ls:
    if ls.count(19)==2 and ls.count(5)>=3:
        print("True")
        break
'''
##Output:True

#2.WAPP to check a given list of integers where the sum of the integers is equal to length of list. 
'''
ls=[int(x) for x in input("ENTER NUMBERS").split()]
if len(ls)==sum(ls):
    print("True")
else:
    print("False")
'''
##ENTER NUMBERS1 -1 3
##True

#3.WAPP to add two integers without using arithmetic operator 
'''
a=5
b=10
c=0
for i in range(a):
    c=c+1
for j in range(b):
    c=c+1

print(c)
'''
#Output:15





























