#1.Take 10 integer inputs from user and store them in a list and print them on screen.
'''
ls=[int(x) for x in input().split(",")]
print(ls)

Output:
[5, 78, 8, 7, 4, 6, 89, 3]
'''

#2.Take 10 integer inputs from user and store them in a list. Again ask user to give a number.
#  Now, tell user whether that number is present in list or not.
#  ( Iterate over list using while loop ).
'''
ls=[int(x) for x in input().split(",")]
num=int(input("Enter"))
c=0
while c<len(ls):
    if ls[c]==num:
        print(num,"number present in list")
        break
    c=c+1
else:
    print(num,"number not found")
'''       
##Output:
##5,8,7,4,5,9,6,2,1
##Enter6
##6 number present in list
##
##5,8,7,4,5,9,6,2,1
##Enter12
##number not found

#3.Take 20 integer inputs from user and print the following:
##number of positive numbers
##number of negative numbers
##number of odd numbers
##number of even numbers
##number of 0s.
'''
ls=[int(x) for x in input().split(",")]
pos=[]
neg=[]
even=[]
odd=[]
for num in ls:
    if num>=0:
        pos.append(num)
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
    else:
        neg.append(num)
        if num%2==0:
            even.append(num)
        else:
            odd.append(num)
print("positive=",pos,"\nnegative",neg,"\neven",even,"\nodd",odd)
'''
##Output:
##5,-4,-3,0,5,3,2,-7,-5,2,-65,30,54,87,-52,15,78,23,-78,5
##positive= [5, 0, 5, 3, 2, 2, 30, 54, 87, 15, 78, 23, 5] 
##negative [-4, -3, -7, -5, -65, -52, -78] 
##even [-4, 0, 2, 2, 30, 54, -52, 78, -78] 
##odd [5, -3, 5, 3, -7, -5, -65, 87, 15, 23, 5]

#4. Take 10 integer inputs from user and store them in a list.
#   Now, copy all the elements in another list but in reverse order.
'''
ls=[int(x) for x in input().split(",")]
reverse=[]
for num in ls:
    reverse.insert(0,num)
print(reverse)
'''

##Output:
##5,8,7,4,5,9,6,2,1,6
##[6, 1, 2, 6, 9, 5, 4, 7, 8, 5]

#5.Write a program to find the sum of all elements of a list.
'''
ls=[5,8,7,4,5,9,6,2,1,6]
sums=0
for i in ls:
    sums=sums+i
print(sums)
'''
##Output:
##53

#6.Write a program to find the product of all elements of a list.
'''
ls=[5,8,7,4,5,9,6,2,1,6]
pro=1
for i in ls:
    pro=pro*i
print(pro)
'''
##Output:
##3628800

#7.Initialize and print each element in new line of a list inside list.
'''
ls=[1,8,5,4,6,8,6,4]
st=str(ls)
st1=st.split(",")
for i in st1:
    print(i,"\n")

Output:
[1 

 8 

 5 

 4 

 6 

 8 

 6 

 4] 
'''
#8.Find largest and smallest elements of a list.
'''
ls=[1,8,5,4,6,8,6,4]

for i in range(len(ls)-1):
    for j in range(i+1,len(ls)):
        if ls[i]>ls[j]:
            temp=0
            temp=ls[i]
            ls[i]=ls[j]
            ls[j]=temp
print("smallest value:",ls[0],"\nlargest value:",ls[-1])
'''
##Output:
##smallest value: 1 
##largest value: 8


#9.Write a program to print sum, average of all numbers, smallest and largest element of a list.
'''
a = [6,7,8,5,6,9,2]
sum = 0
avg = 0
print("min: ",min(a))
print("max: ",max(a))
for i in a:
    sum = sum +i
    avg = sum/5
print("sum: ",sum)
print("avg: ",avg)
'''
##Output:
##min:  2
##max:  9
##sum:  43
##avg:  8.6

#10. Write a program to check if elements of a list are same or not it read from front or back. E.g.-
#[2	3	15	15	3	2]
'''

l = [2,3,15,15,3,2]
rev = l[::-1]
if(l == rev):
    print("same")
else:
    print("not sls=[1,8,5,4,6,8,6,4]ame")
'''
##Output:
##same

#11.Take a list of 10 elements. Split it into middle and store the elements in two dfferent lists. E.g.-
#INITIAL list :
#58	24	13	15	63	9	8	81	1	78
'''
ls=[1,8,5,4,6,8,6,4]
a = ls[:(len(ls)//2)]
b =ls[len(ls)//2:]
print(a)
print(b)
'''
##Output:
##[1, 8, 5, 4]
##[6, 8, 6, 4]


#12.Ask user to give integer inputs to make a list. Store only even values given and print the list.
'''
ls=[]
while True:
    num=int(input("Enter>"))
    if num==0:
        break
    else:
        if num%2==0:
            ls.append(num)
print(ls)

'''
##
##Output:
##Enter>5
##Enter>9
##Enter>5
##Enter>4
##Enter>5
##Enter>45
##Enter>11
##Enter>55
##Enter>12
##Enter>56
##Enter>54
##Enter>84
##Enter>21
##Enter>22
##Enter>32
##Enter>19
##Enter>0
##[4, 12, 56, 54, 84, 22, 32]





















