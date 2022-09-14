#1.what is a variable in and describe the role of variable in python memory management?
       Variables are nothing but reserved memory locations to store values.
   This means that when you create a variable you reserve some space in memory.
   Based on the data type of a variable,the interpreter allocates memory and
   decides what can be stored in the reserved memory.

   
#2.what are the advantages and disadvantages of type casting?
Advantages:
 1).With the help of type casting, you can convert character data type to an int data type.
 2).If you are performing conversion between int and character data types then the value of the result will be integer type.
 3).Because it is a bigger data type between int and char data types
   Disadvantages:
 1).More complex type system.
 2).Source of bugs due to unexpected casts

 
#3.what is the difference between while loop and for loop?
       In a computer programming language,iteration statements like for loop and while loop and
   more are used for repeated execution of the instruction in a program.Both for loop and while
   loop is used to execute the statements again and again while the program is running.The major
   difference between for loop and while loop is that for loop is used when the number of iterations
   is known whereas,in the while loop,execution is done until the statement in the program is proved wrong.


#4.write 5 string method with example?
  1) Upper
  2) Lower
  3) Capitalize
  4) Split
  5) strip

 # Upper:

  str = "hyderabad"
  print(str.upper())

 #output:
        HYDERABAD

 # Lower:

   str ="HYDERABAD"
   print(str.lower())

 #output:
       HYDERABAD

 # Capitalize:

   str ="hyderabad"
   print(str.capitalize())
 #output:
        Hyderabad

 # Split:

    str ="hyderabad"
    print(str.split())

 #output:
      ['hyderabad']

 # Strip:

   str = "    hyderabad"
   print(str.strip())
 #output:
      hyderabad


#5.write the Precedence rule of python with example?
       The combination of values, variables, operators,and function calls
   is termed as an expression.The Python interpreter can evaluate a valid
   expression

>>> 10 - 17
-7

