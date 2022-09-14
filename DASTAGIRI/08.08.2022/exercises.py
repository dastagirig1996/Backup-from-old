#1.WAP to find the senior citizens in the given list,list values should take dynamicaly (or) from the user only.
# suppose list=[23,67,45,89,65,12,15,19], and output:[65,67,89] final list should be in accending order.
# person age is 60 (or) more than 60 belongs to senior citizens.?
'''
ages=[52,78,65,25,70,81,54,19,46,63,42]
senior_citizens=[]

for age in ages:
    if age>=60:
        senior_citizens.append(age)
ascending_ages=sorted(senior_citizens)
print(ascending_ages)
'''
#Output:
##[63, 65, 70, 78, 81]

#2. WAP to find the diagonal matrix absolute difference?
# suppose  1   2  3
#          7   9  3
#         12   5  67

'''
mat=[[1,2,3],
     [7,9,3],
     [12,5,67]]

a=mat[0][0]+mat[1][1]+mat[2][2]
b=mat[0][2]+mat[1][1]+mat[2][0]
c=b-a
print(abs(c))
''''
##Output:
##53
        
#3. WAP to solve this pattern
"""  A
     A B
     A B C
     A B C D
     A B C D E
     A B C D
     A B C
     A B
     A         """
'''
n=5
for i in range(n+1):    
    for j in range(1,i+1):
        print(chr(k),end=' ')
        k=k+1
    k=65       
    print()
for s in range(n-1,0,-1):
    for r in range(1,s+1):
        print(chr(k),end=' ')
        k=k+1
    k=65
    print()
'''
##Output:
##A 
##A B 
##A B C 
##A B C D 
##A B C D E 
##A B C D 
##A B C 
##A B 
##A 




















