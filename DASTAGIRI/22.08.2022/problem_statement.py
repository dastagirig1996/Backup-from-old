##Task
##Given  sets of integers,  and , print their symmetric difference in ascending order.
##The term symmetric difference indicates those values that exist in either  or  but do not exist in both.
##
##Input Format
##
##The first line of input contains an integer, .
##The second line contains  space-separated integers.
##The third line contains an integer, .
##The fourth line contains  space-separated integers.
##
##Output Format
##
##Output the symmetric difference integers in ascending order, one per line.
##
##Sample Input
##
##STDIN       Function
##-----       --------
##4           set a size M = 4
##2 4 5 9     a = {2, 4, 5, 9}
##4           set b size N = 4
##2 4 11 12   b = {2, 4, 11, 12}
##Sample Output
##
##5
##9
##11
##12
'''
M= int(input())
a=set(map(int,input().split()))
       
N= int(input())
b=set(map(int,input().split()))

adef=a.symmetric_difference(b)
bdef=b.symmetric_difference(a)

result=adef.union(bdef)
for i in sorted(list(result)):
    print(i)
'''
##Output:
##4
##1 2 3 4
##4
##1 2 5 6
##3
##4
##5
##6










