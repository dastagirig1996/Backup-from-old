#1.How would you confirm that 2 strings have the same identity?
'''
b=20
a=20
if a is b:
    print("same id")
'''
##Output:
##same id    

#2.How would you check if each word in a string begins with a capital letter?

'''
st='HelLo'
for i in st:
    if i.isupper():
        print(i)
'''        
##Output:
##H
##L

#3.Check if a string contains a specific substrin
'''
st="guido van rossum is the author of python"
print("is" in st)
'''
##Output:
##True

#4.Find the index of the first occurrence of a substring in a string?
'''
st="python programing language is language"
print(st.index("language"))
'''
##Output:
##18

#5. Count the total number of characters in a string
'''st= "guido van rossum"
ch=input("Enter...")
c=0
for i in st:
    if ch==iprint("is" in st):
        c=c+1
print(c)
'''
##Output:
##Enter...s
##2

#6.Count the number of a specific character in a string
'''
st='python was developed in 1990\'s'
print(st)
c=0
ch=input("enter.")
for i in st:
    if i==ch:
        c=c+1
print(ch,c,"times exist")
'''
##Output:
##python was developed in 1990's
##enter.e
##e 3 times exist

#7. Capitalize the first character of a string
'''print(input("enter").capitalize())'''

##Output:
##enterhai
##Hai

#8. What is an f-string and how do you use it?

'''F-strings provide a way to embed expressions inside string literals, using a minimal syntax'''
'''
name="sai"
marks=85
print(f"name is {name} and marks of {marks}")
'''
##Output:
##name is sai and marks of 85

#9.Search a specific part of a string for a substring

'''
st="guido van rossum is the author of python"
print("is" in st)
'''
##Output:
##True

#10.Interpolate a variable into a string using format()

'''
add="author"
print(f"guido van rossum is the {add} of python")
'''
##Output:
##guido van rossum is the author of python

#11. Check if a string contains only numbers
'''st=input("enter string")
if st.isdigit():
    print("true")
else:"guido van rossum
    print("false")
'''
##Output:
##enter string56883
##true

#12. Split a string on a specific character
'''
st="python is a programing language"
print(st.split("o"))
'''
##Output:
##['pyth', 'n is a pr', 'graming language']


#13. Check if a string is composed of all lower case characters
'''
st=input("enter")
if st.islower():
    print("all lower")
else:
    print("all charecters")
'''
##Output:
##enterHello world
##all charecters

#14.Check if the first character in a string is lowercase

'''
st=input("enter")
print(st[0].islower())
'''
##Output:
##enterhello
##True


#15. Can an integer be added to a string in Python?

''' yes, we can add integer as a string'''

#16.Reverse the string “hello world”
'''
st="hello world"
reverse=""
for ch in st:
    reverse=ch+reverse
print(reverse)
'''
##Output:
##dlrow olleh

#17. Join a list of strings into a single string, delimited by hyphens
'''
ls=['hello','world','good','morning']
print(','.join(ls))
'''
##Output:
##hello,world,good,morning

#18. Check if all characters in a string conform to ASCI
'''
st="guido van rossum"
print(st.isascii())
'''
#Output:
#True

#19. Uppercase or lowercase an entire string
'''
st="Guido van rossum"

print(st.upper(),"\n",st.lower())
'''
##Output:
##GUIDO VAN ROSSUM 
## guido van rossum

#20 Uppercase first and last character of a string
'''
st="guido van rossuM"
print(st[0].upper()+st[1:-1]+st[-1].lower())
'''
##Output:
##Guido van rossum

#21.Check if a string is all uppercase

##st=input("enter")
##for ch in st:
##    if ch.isupper():
##        print("all upper case")
##        break
##    else:
##        print("combined letters")
'''
str1=input("Enter the String")

print(str1.isupper())
'''
##Output:
##Enter the StringHello
##False

#22.When would you use splitlines()?
#splitlines() splits a string on line breaks.
'''sentence = "The author \ndevelops criteria for \nrecognising boundary \neffects."
print(sentence.splitlines())
'''
##Output:
##['The author ', 'develops criteria for ', 'recognising boundary ', 'effects.']

#23. Give an example of string slicing
'''
st="Guido van rossum"
print(st[2:5])
'''
##Output:
##ido

#24. Convert an integer to a string
'''
a=546
st=str(a)
print(st)
print(type(st))
'''
##Output:
##546
##<class 'str'>

#25. Check if a string contains only characters of the alphabet
'''
st=input("enter")
if st.isalpha():
    print("yes")
else:
    print("no")
'''
##Output:
##enterdyuyu656
##no

#26.Replace all instances of a substring in a string
'''
st="hello"
print(st.replace("h","A"))
'''
##Output:
##Aello

#27.Return the minimum character in a string
'''
ST="world"
print(min(ST))
'''
##Output:
##d

#28.Check if all characters in a string are alphanumeric
'''
st=input("enter")
if st.isalnum():
    print("yes")
'''
##Output:
##enterzjd54
##yes

#29.Remove whitespace from the left, right or both sides of a string
'''
st="            python is a programing language            "

print(st.lstrip())
print(st.rstrip())
print(st.strip())
'''
##Output:
##python is a programing language            
##            python is a programing language
##python is a programing language

#30.Check if a string begins with or ends with a specific character?
'''
name= "Dastagiri Goguvala"
print(name.startswith("Dastagiri"))
print(name.endswith("ala"))
'''
##Output:
##True
##True






