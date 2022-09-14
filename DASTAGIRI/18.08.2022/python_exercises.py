#1.Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#  between 2000 and 3200 (both included). 

#The numbers obtained should be printed in a comma-separated sequence on a single line.
'''
ls=[]
for i in range(2000,3200):
    if i%7==0 and i%5!=0:
        ls.append(i)
print(*ls,sep=",")
'''
##Output:
##2002,2009,2016,2023,2037,2044,2051,2058,2072,2079,2086,2093,2107,2114,2121,2128,2142,2149,2156,2163,2177,2184,2191,
##2198,2212,2219,2226,2233,2247,2254,2261,2268,2282,2289,2296,2303,2317,2324,2331,2338,2352,2359,2366,2373,2387,2394,
##2401,2408,2422,2429,2436,2443,2457,2464,2471,2478,2492,2499,2506,2513,2527,2534,2541,2548,2562,2569,2576,2583,2597,
##2604,2611,2618,2632,2639,2646,2653,2667,2674,2681,2688,2702,2709,2716,2723,2737,2744,2751,2758,2772,2779,2786,2793,
##2807,2814,2821,2828,2842,2849,2856,2863,2877,2884,2891,2898,2912,2919,2926,2933,2947,2954,2961,2968,2982,2989,2996,
##3003,3017,3024,3031,3038,3052,3059,3066,3073,3087,3094,3101,3108,3122,3129,3136,3143,3157,3164,3171,3178,3192,3199

#2.Write a program which can compute the factorial of a given numbers. 
##The results should be printed in a comma-separated sequence on a single line.
##
##Suppose the following input is supplied to the program: 
##
##8 
##
##Then, the output should be: 
##
##40320 
'''
n=8
mul=1
for i in range(1,n+1):
    mul=mul*i
print(mul)
'''
#Output:
##40320

##3.With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. 
##
##  Suppose the following input is supplied to the program: 
##
##  8 
##
##  Then, the output should be: 
##
##  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64} 
'''
dic={}
n=8
for i in range(1,n+1):
    dic[i]=i*i
print(dic)
'''
##Output:
##{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

#4. Write a program which accepts a sequence of comma-separated numbers from console and generate
#a list and a tuple which contains every number.  

##Suppose the following input is supplied to the program:  
##34,67,55,33,12,98  
##Then, the output should be:  
##['34', '67', '55', '33', '12', '98']
##
##('34', '67', '55', '33', '12', '98') 
'''
ls=list(map(int,input("Enter").split(",")))
print(ls)
tp=tuple(ls)
print(tp)
'''
##Output:
##Enter34,67,55,33,12,98
##[34, 67, 55, 33, 12, 98]
##(34, 67, 55, 33, 12, 98)


##5.Write a program that accepts a comma separated sequence of words as input and prints the words
##in a comma-separated sequence after sorting them alphabetically. 
##
##Suppose the following input is supplied to the program: 
##
##without,hello,bag,world 
##
##Then, the output should be: 
##
##bag,hello,without,world
'''
ls=[s for s in input("enter").split(",")]
ls.sort()
print(*ls,sep=",")
'''
##Output:
##enterwithout,bag,hello,world
##bag,hello,without,world


##6.Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 

##Suppose the following input is supplied to the program: 
##
##Hello world 
##
##Practice makes perfect 
##
##Then, the output should be: 
##
##HELLO WORLD 
##
##PRACTICE MAKES PERFECT 
'''
while True:
    name=input()
    if name=="":
        break
    else:
        print(name.upper())
'''       
##Output:
##hello world
##HELLO WORLD
##may i help you
##MAY I HELP YOU

#7.Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
##whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma
##separated sequence. 

##Example:      
##0100,0011,1010,1001 
'''
binary=list(map(str,input("enter").split(",")))
print(binary)
for i in binary:
    dec=int(i,2)
    if dec%5==0:
        print(i)
'''
##Output:
##enter0100,0011,1010,1001
##['0100', '0011', '1010', '1001']
##1010

#8.Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters. 

##Suppose the following input is supplied to the program: 
##
##Hello world! 
##
##Then, the output should be: 
##
##UPPER CASE 1 
##LOWER CASE 9
'''
upper=0
lower=0
st="Hello world"
for ch in st:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
print("UPPER CASE ",upper,"\nLOWER CASE ",lower)
'''

##Output:
##UPPER CASE  1 
##LOWER CASE  9

#9.Write a program to compute the frequency of the words from the input. The output should output
##after sorting the key alphanumerically.  
##
##Suppose the following input is supplied to the program: 
##
##New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3. 
##
##Then, the output should be: 
##
##2:2 
##
##3.:1 
##
##3?:1 
##
##New:1 
##
##Python:5 
##
## 	Read:1 
##
##and:1 
##
##between:1 
##
##choosing:1 
##
##or:2 

##to:1 
'''
st="New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3."

ls=st.split(" ")
dic={}
for s in ls:
    if s not in dic:
        dic[s]=1
    else:
        dic[s]=dic[s]+1
for k,v in dic.items():
    print(k,':',v)
'''
##Output:
##New : 1
##to : 1
##Python : 5
##or : 2
##choosing : 1
##between : 1
##2 : 2
##and : 1
##3? : 1
##Read : 1
##3. : 1

#10.Convert 2nd Part of String into Upper Case
'''
st="hello"
st1=st[1].upper()
st2=""
for i in range(len(st)):
    if i==1:
        st2=st2+st1
    else:
        st2=st2+st[i]
print(st2)
'''
##Output:
##hEllo

#11.With a given tuple (1,2,3,4,5,6,7,8,9,10), write a program
# to print the first half values in one line and the last half values in one line.\ 

'''
tp=(1,2,3,4,5,6,7,8,9,10)
half=len(tp)//2
print(tp[:half],'\n',tp[half:])
'''
##OUtput:
##(1, 2, 3, 4, 5) 
## (6, 7, 8, 9, 10)
































