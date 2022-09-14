'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks]
for a list of students. Print the average of the marks array for the student name provided,
showing 2 places after the decimal.

Example
marks key:value pairs are
'alpha':[20,30,40]
'beta':[30,50,70]

query_name='beta'
2<=n<=10
0<=marks[i]<=100
length of marks arrys=3
The query_name is 'beta'. beta's average score is .

Input Format

The first line contains the integer , the number of students'\ records.
The next  lines contain the names and marks obtained by a student,
each value separated by a space. The final line contains query_name, the name of a student to query.

Constraints


Output Format

Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.

Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
Sample Output 0

56.00
Explanation 0

marks for Mallika are{52,56,60} whose average is ((52+56+60)/3)=56

Marks for Malika are  whose average is 

Sample Input 1

2
Harsh 25 26.5 28
Anurag 26 28 30
Harsh
Sample Output 1

26.50
'''
'''
dic={}
while True:
    name=input("Enter student name:")
    if name =='':
        break
    else:
        sums=0
        ls=[]
        sub=3
        for i in range(sub):   
            marks=int(input("ENter marks"))
            ls.append(marks)
            dic[name]=ls

student=input("Enter selected student name..")
for a,b in dic.items():
    if a==student:
        print("average marks of {} is :{}".format(student,sum(dic[student])//sub))'''
##Output:
##Enter student name:ha
##ENter marks85
##ENter marks78
##ENter marks85
##Enter student name:ru
##ENter marks78
##ENter marks85
##ENter marks63
##Enter student name:
##Enter selected student name..ru
##average marks of ru is :75

    


    





















