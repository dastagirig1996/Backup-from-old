#1) WAP to reverse a number
'''num=int(input("Ener:"))
reverse=0
while(num>0):
    m=num%10
    reverse=reverse*10+m
    num=num//10
print(reverse)

#output:
Ener:153
351'''

#2. WAP to count  the number  occurrence/frequency  of a  each character in a string.
'''st="good morning"
dic={}
for i in st:
    if i in dic.keys():
        dic[i]=dic[i]+1
    else:
        dic[i]=1
print(dic)'''

#Output:{'g': 2, 'o': 3, 'd': 1, ' ': 1, 'm': 1, 'r': 1, 'n': 2, 'i': 1}

'''#3.WAP  to check length of two string is equal or not.
st1=input("string:")
st2=input("string:")
if len(st1)==len(st2):
    print("Equal")
else:
    print("not eual")

#Output:
    string:ssfsf
    string:ssvsg
    Equal'''

#4. Python program to print even numbers up to 100
'''n=100
for i in range(1,n+1):
    if i%2==0:
        print(i)
#Output:
2
4
6
8
10
12
14
16
18
20
22
24
26
28
30
32
34
36
38
40
42
44
46
48
50
52
54
56
58
60
62
64
66
68
70
72
74
76
78
80
82
84
86
88
90
92
94
96
98
100'''

#5. Write a program in python to find greatest among three integers
'''a=int(input("Enter:"))
b=int(input("Enter:"))
c=int(input("Enter:"))
if a>b:
    if a>c:
        print("a is bigger")
    else:
        print("c is bigger")
elif b>c:
    print("b is bigger")
else:
    print("c is bigger")

#Output:
Enter:8
Enter:41
Enter:2
b is bigger'''


    
