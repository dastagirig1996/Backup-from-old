##1.Python Program to Return the Length of the Longest Word from the List of Words
##
##Problem Description:
##
##The program takes a list of words and returns the word with the longest length.
##
##Runtime Test Cases:
##
##Case 1:
##Enter the number of elements in list:4
##Enter element1:"Apple"
##Enter element2:"Ball"
##Enter element3:"Cat"
##Enter element4:"Dinosaur"
##The word with the longest length is:
##Dinosaur
## 
##Case 2:
##Enter the number of elements in list:3
##Enter element1:"Bangalore"
##Enter element2:"Mumbai"
##Enter element3:"Delhi"
##The word with the longest length is:
##Bangalore



'''
count_of_elements=int(input("enter number"))
ls=[]
lst=[]
temp=0
for i in range(count_of_elements):
    element=input("Enter")
    ls.append(element)
for j in ls:
    if len(j)>temp:
        temp=len(j)
        lst.append(j)
        print(lst[-1])

'''

##Output:
##enter number4
##Enterapple
##Enterbanana
##Enterorange
##Enterfinaapple
##finaapple






























