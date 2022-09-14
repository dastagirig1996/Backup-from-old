#integer
'''
print("$$$Integer$$$$")
print("{}".format(10))              # Do not write space between {}
print("{} {}".format(10, 20))
print("{0}".format(10))
print("{0} {1}".format(10, 20))
print("{1} {0}".format(10, 20))
print("{num1}".format(num1=10))
print("{num1} {num2}".format(num1=10, num2=20))
print("{num2} {num1}".format(num1=10, num2=20))
'''
#output:

##$$$Integer$$$$
##10
##10 20
##10
##10 20
##20 10
##10
##10 20
##20 10

#float
'''
print("******** Float *********")
print("{}".format(10.56))
print("{} {}".format(10.56, 20.42))
print("{0}".format(10.56))
print("{0} {1}".format(10.56, 20.42))
print("{1} {0}".format(10.56, 20.42))
print("{num1}".format(num1=10.56))
print("{num1} {num2}".format(num1=10.56, num2=20.42))
print("{num2} {num1}".format(num1=10.56, num2=20.42))
'''
#output:

##******** Float *********
##10.56
##10.56 20.42
##10.56
##10.56 20.42
##20.42 10.56
##10.56
##10.56 20.42
##20.42 10.56


#strings

'''print("******** String *********")
print("{}".format("apple  "))
print("{} {}".format("apple", "banana"))
print("{0}".format("apple"))
print("{0} {1}".format("apple", "banana"))
print("{1} {0}".format("apple", "banana"))
print("{str1}".format(str1="apple"))
print("{str1} {str2}".format(str1="apple", str2="banana"))
print("{str2} {str1}".format(str1="apple", str2="banana"))
'''
#output:
##******** String *********
##apple  
##apple banana
##apple
##apple banana
##banana apple
##apple
##apple banana
##banana apple


# Integer and String
'''
print("Hello My Name is {}".format("alex"))
print("{} {}".format(10, "banana"))
print("{0} {1}".format(10, "banana"))
print("{1} {0}".format(10, "banana"))
print("{num1} {str1}".format(num1=10, str1="banana"))
print("{str1} {num1}".format(num1=10, str1="banana"))
'''
#output:
##Hello My Name is alex
##10 banana
##10 banana
##banana 10
##10 banana
##banana 10


#Comma as thousand Separator
'''print("{:,}".format(34567890))'''

#output:
##34,567,890


#variable

'''name = "ram"
age= 62
print("My name is {} and age {}".format(name, age))'''




#output:My name is ram and age 62

# Expressing a Percentage
'''a = 50
b = 3
print("{:.2%}".format(a/b))

#output:1666.67%'''

# Accessing arguments  items
'''value = (10, 20)
print("{0[0]} {0[1]}".format(value))

#output:10 20'''

# Format with Dict
'''data1 = {'rahul': 2000, 'sonam': 3000}
print("{0[rahul]:d} {0[sonam]:d}".format(data1))

#output:2000 3000'''

# Format with Dict
'''data2 = {'rahul': 2000, 'sonam': 3000}
print("{d[rahul]:d} {d[sonam]:d}".format(d=data2))

#output:2000 3000'''

# Accessing arguments by name:
'''data3 = {'rahul': 2000, 'sonam': 3000}
print("{rahul} {sonam}".format(**data3))

#output:2000 3000'''

# ** is a format parameter (minimum field width)
 
 
# Integer
'''print("******** Integer ********")
print("{}".format(15))                          # Printing as string 15
print("{:d}".format(15))
print("{0:d}".format(15))
print("{num:d}".format(num=15))
print("{num:5d}".format(num=15))
print("{num:05d}".format(num=15))
print("{num:+5d}".format(num=15))
print("{num:<5d}".format(num=15))               # Left align
print("{num:*<5d}".format(num=15))              # Left align with fill
print("{num:*>5d}".format(num=15))              # Right align with fill
print("{num:^5d}".format(num=15))               # Center align
print("{num:*^5d}".format(num=15))              # Center align with fill

#output:******** Integer ********
15
15
15
15
   15
00015
  +15
15   
15***
***15
 15  
*15**'''

#Float
'''print("******** Float ********")
print("{}".format(15.65))                       # Printing as string 15.65
print("{:f}".format(15.65))                 
print("{0:f}".format(15.65))
print("{num:f}".format(num=15.65))
print("{num:8f}".format(num=15.65))             # 15.650000 
print("{num:8.3f}".format(num=15.65))
print("{num:+8.2f}".format(num=15.65))
print("{num:<8.2f}".format(num=15.65))          # Left align
print("{num:*<8.2f}".format(num=15.65))         # Left align with fill
print("{num:*>8.2f}".format(num=15.65))         # Right align with fill
print("{num:^8.2f}".format(num=15.65))          # Center align
print("{num:*^8.2f}".format(num=15.65))         # Center align with fill

#output:******** Float ********
15.65
15.650000
15.650000
15.650000
15.650000
  15.650
  +15.65
15.65   
15.65***
***15.65
 15.65  
*15.65**'''
#String
'''print("******** String ********")
print("{:8s}".format("apple"))
print("{:<8}".format("apple"))
print("{:*<8}".format("apple"))
print("{:>8}".format("apple"))
print("{:*>8s}".format("apple"))
print("{:^8s}".format("apple"))
print("{:*^8s}".format("apple"))

#output:******** String ********
apple   
apple   
apple***
   apple
***apple
 apple  
*apple**'''

'''print("******** Truncating String ********")
print("{:.3s}".format("ojas"))
print("{:8.3s}".format("ojas"))
print("{:*<8.3s}".format("ojas"))
print("{:>8.3s}".format("ojas"))
print("{:*>8.3s}".format("ojas"))
print("{:^8.3s}".format("ojas"))
print("{:*^8.3s}".format("ojas"))

#output:******** Truncating String ********
oja
oja     
oja*****
     oja
*****oja
  oja   
**oja***'''

# Integer

'''print("******** Integer *********")
a = 10
b = 20
print(f"{a}")               # empty expression not allowed
print(f"{a} {b}")
print(f"{b} {a}")


#output:******** Integer *********
10
10 20
20 10'''

##Float
'''
print("******** Float *********")
c = 10.56
d = 20.42
print(f"{c}")
print(f"{c} {d}")
print(f"{d} {c}")

#output:******** Float *********
10.56
10.56 20.42
20.42 10.56
'''
#String

'''print("******** String *********")
f_name = "alex"
l_name = "albert"
print(f"{f_name}")
print(f"{f_name} {l_name}")
print(f"{l_name} {f_name}")

#output:******** String *********
alex
alex albert
albert alex
'''

# Integer and String

'''name = "alex albert"
age = 10
print(f"Hello My Name is {name}")
print(f"{name} {age}")
print(f"{age} {name}")

#output:Hello My Name is alex albert
alex albert 10
10 alex albert'''

#integer
'''print("******** Integer ********")
num = 15
print(f"{num}")             # Treated as String becoz no type mention
print(f"{num:d}")
print(f"{num:5d}")
print(f"{num:05d}")
print(f"{num:+5d}")
print(f"{num:<5d}")         # Left align
print(f"{num:*<5d}")        # Left align with fill
print(f"{num:*>5d}")        # Right align with fill
print(f"{num:^5d}")         # Center align
print(f"{num:*^5d}")        # Center align with fill

#output:******** Integer ********
15
15
   15
00015
  +15
15   
15***
***15
 15  
*15**'''

 
#Float

'''print("******** Float ********")
num = 15.65
price = 15.65123456789
print(f"{num}")             # Treated as String becoz no type mention
print(f"{num:f}")
print(f"{num:8f}")          # 15.650000 
print(f"{price:.20f}")
print(f"{num:8.3f}")
print(f"{num:+8.2f}")
print(f"{num:<8.2f}")       # Left align
print(f"{num:*<8.2f}")      # Left align with fill
print(f"{num:*>8.2f}")      # Right align with fill
print(f"{num:^8.2f}")       # Center align
print(f"{num:*^8.2f}")      # Center align with fill

#output:******** Float ********
15.65
15.650000
15.650000
15.65123456789000044864
  15.650
  +15.65
15.65   
15.65***
***15.65
 15.65  
*15.65**'''

#String

'''print("******** String ********")
name = "alexa"
print(f"{name}")
print(f"{name:s}")
print(f"{name:8s}")
print(f"{name:<8}")
print(f"{name:*<8}")
print(f"{name:>8}")
print(f"{name:*>8s}")
print(f"{name:^8s}")
print(f"{name:*^8s}")

#output:******** String ********
alexa
alexa
alexa   
alexa   
alexa***
   alexa
***alexa
 alexa  
*alexa**'''

'''print("******** Truncating String ********")
name = "alexalbert"
print(f"{name:.3s}")
print(f"{name:8.3s}")
print(f"{name:*<8.3s}")
print(f"{name:>8.3s}")
print(f"{name:*>8.3s}")
print(f"{name:^8.3s}")
print(f"{name:*^8.3s}")

#output:******** Truncating String ********
ale
ale     
ale*****
     ale
*****ale
  ale   
**ale***'''

 
# Thousand Separator
'''
price = 1234567890
print(f"{price:,}")
print(f"{price:_}")

#output:1,234,567,890
1_234_567_890'''

#Variable

'''name = "Rahul"
age= 62
print(f"My name is {name} and age {age}")

#output:My name is Rahul and age 62'''

# Expression
'''print(f"{10*8}")
#output:80'''

# Expressing a Percentage
'''a = 50
b = 3
print(f"{a/b:.2%}")

#output:1666.67%'''

# Accessing arguments  items
'''value = (10, 20)
print(f"{value[0]} {value[1]}")

#output:10 20'''

# Format with Dict
'''data = {'rahul': 2000, 'sonam': 3000}
print(f"{data['rahul']:d} {data['sonam']:d}")

#output:2000 3000'''

#Calling Function
'''name= "alexalbert"
print(f"{name}")
print(f"{name.upper()}")

#output:alexalbert
ALEXALBERT'''

# Using object created from class
#print(f"{obj.name}")

# Curly Braces
'''
print(f"{10}")
print(f"{{10}}")

#output:10
{10}'''

# Date and Time

'''from datetime import datetime
today = datetime(2019, 10, 5)
print(f"{today}")
print(f"{today:%d-%b-%Y}")
print(f"{today:%d/%b/%Y}")
print(f"{today:%b/%d/%Y}")

#output:2019-10-05 00:00:00
05-Oct-2019
05/Oct/2019
Oct/05/2019'''

#datetime — Basic date and time types — Python 3.7.13 documentation
 
''' 
print("%d" % 432)   
print("%d %d" % (432, 345))
print("%f" %432.123)
print("%f %f" %(432.123, 10.3)) 
print("%f" %432.123456)
print("%f" %432.12345651)
print("%s" % "alexalbert")
print("%s %s" % ("Hello", "alexalbert"))
print("%d %s" % (432, "alexalbert"))
#print("%s %d" % (432, "alexalbert"))       TypeError
print("%(nm)s %(ag)d" % {'ag':432, 'nm':"alexalbert"})
 
print("% d" % 432)
print("%          d" % 432)
print("%+d" % 432)
 
print("%8d" % 432)
print("%08d" % 432)
print("%.3f" %432.123)
print("%.2f" %432.123)
print("%.2f" %432.128)
print("%9.2f" %432.128)
print("%09.2f" %432.123)
print("%9.2f" %4388453232.124)

#output:432
432 345
432.123000
432.123000 10.300000
432.123456
432.123457
alexalbert
Hello alexalbert
432 alexalbert
alexalbert 432
 432
 432
+432
     432
00000432
432.123
432.12
432.13
   432.13
000432.12
4388453232.12'''
