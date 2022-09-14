##1.Extend nested list by adding the sublist 
##
## 
##
##list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
##
## 
##
### sub list to add 
##
##sub_list = ["h", "i", "j"] 
##
##Expected Output: 
##
##['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


'''
list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]
sub_list = ["h", "i", "j"]

#list1[2][1][2].extend(sub_list)
print(list1)
k=2
for i in sub_list:  
    list1[2][1][2].insert(k,i)
    k=k+1
print(list1)

'''
##Output:
##['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


##2. write  a program to find the quadratic equation ax2 + bx + c = 0 by using functions:
##    given inputs a=20,b=6,c=4.
##    hint: [-b ± √(b2 - 4ac)]/2a.

'''
def quadratic(a,b,c):
    #[-b ± √(b2 - 4ac)]/2a
    pos=(-b+(b**2-4*a*c)**0.5)/2*a
    neg=(-b-(b**2-4*a*c)**0.5)/2*a
    return pos,neg
print(quadratic(20,6,4))
'''


#Output:
##((-59.99999999999999+168.5229954635272j), (-60.00000000000001-168.5229954635272j))



##3.explain about list comprehension?with syntax.
'''
* List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list

* [expression for element in iterable if condition]
'''


##4.Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
##  The element value in the i-th row and
##j-th column of the array should be i*j.

##Example
##Suppose the following inputs are given to the program:
##3,5
##Then, the output of the program should be:
##[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

'''
def matrix(n,m):
    ls=[]
    for i in range(n):
        ls1=[]
        for j in range(m):
            ls1.append(i*j)
        ls.append(ls1)
    return ls
print(matrix(3,5))
'''           

##Output:
##[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

            

##5.explain about the four user define funtion?with an example for each?
'''
There can be 4 different types of user-defined functions, they are:

1.Function with no arguments and no return value
2.Function with no arguments and a return value
3.Function with arguments and no return value
4.Function with arguments and a return value



def mul():
    a=2
    b=5
    print(a*b)

mul()


def mul():
    a=2
    b=5
    return a*b
print(mul())


def mul(a,b):
    print(a*b)

mul(2,5)    

def mul(a,b):
    return a*b
print(mul(2,5))

'''
##Output:
##10
##10
##10
##10






















