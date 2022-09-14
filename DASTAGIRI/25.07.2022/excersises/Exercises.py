'''#1.WAP for eligibility of a canditate voter_id,
  suppose age between (18 to 80 years old) using flow control conditions?
  
age=int(input("Enter age :"))
if 18<=age<=80:
    print("You are eligibile for the voter id")
else:
    print("you are not eligible for the voter id")'''

'''#2.WAP for calculating student marks in 5-subjects,and find  grades,(suppose grade A,B,C and Fail)?
dic={}
while True:
    name=input("Enter name:")
    if name=="":
        break
    else:
        adding=0
        subjects=5
        for i in range(subjects):
            marks=int(input("Enter marks"))
            adding=adding+marks
            average=adding//subjects
        dic[name]=average
    print("\n")
for k,v in dic.items():
    if v>=80:
        print(k,"average marks:-",v,"A Grade")
    elif 60<=v<80:
        print(k,"average marks:-",v,"B Grade")
    elif 35<=v<60:
        print(k,"average marks:-",v,"B Grade")
    else:
        print(k,"average marks:-",v,"Fail")

#Output:
Enter name:hari
Enter marks58
Enter marks54
Enter marks87
Enter marks54
Enter marks65


Enter name:krish
Enter marks58
Enter marks56
Enter marks78
Enter marks45
Enter marks65


Enter name:ramu
Enter marks45
Enter marks14
Enter marks52
Enter marks25
Enter marks30


Enter name:
hari average marks:- 63 B Grade
krish average marks:- 60 B Grade
ramu average marks:- 33 Fail'''

'''#3.WAP for finding  even or odd number using (if .. else ... condition)?
num=int(input("Enter number:"))
if num%2==0:
    print(num,"Even number")
else:
    print(num,"Odd number")'''

'''#4.WAP calculating area of a circle, result in positive integers only not in float values
r=int(input("a:"))
pi=3.14
area=pi*(r**2)
print(int(area))'''

'''#5.WAP for finding  variables A and B are having the same memory location?
a=int(input("a:"))
b=int(input("b:"))
if id(a)==id(b):
    print("a,b in same mamory location")
else:
    print("a,b in different location")
    
#Output:
a:56
b:56
a,b in same mamory location'''

