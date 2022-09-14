#string methods
#upper:convert whole string to upper.
'''a = "hello"
print("uppercase of word: ",a.upper())


#output:uppercase of word:  HELLO'''

#lower: coverts whole string to lower.
'''a = "HELLO"
print("lowercase of word: ",a.lower())

#output:lowercase of word:  hello'''


#capitalize: coverts only first character of string to uppercase.

'''a = "asdfg"
print("captialize of word: ",a.capitalize())

#output:captialize of word:  Asdfg'''

#isupper():if all characters in the string are upper then it returns true.

'''a = "ADFG"
print("characters in the string are upper: ",a.isupper())

#output:characters in the string are upper:  True'''

#islower(): if all characters in the string are lower then it return False.
'''a = "Dfgh"
print("characters in the strings are lower: ",a.islower())

#output:characters in the strings are lower:  False'''

#istitle(): returns True if all words in a text start with a upper case letter, AND the rest of the word are lower case letters, otherwise False.

'''a = "The Boy Is Eating"
b =a.istitle()
print(b)

#output:True'''

#isdigit():Returns True if all characters in the string are digits.

'''a = "hai123"
print(a.isdigit())

#output:False
'''

#isalpha():Returns True if all characters in the string are in the alphabet

'''a = "hai"
print(a.isalpha())

#output:True'''

#isalphanum():Returns True if all characters in the string are alphanumeric

'''a = "hai54"
print(a.isalnum())

#output:True'''


#strip(): method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
'''a =" say 15  "
print(a.strip())

#output:say 15'''

#lstrip():removes left spcaes(begining of spaces)
'''a ="    123"
print(a.lstrip())

#output:123'''
#rstrip():removes right spcaes(ending of spaces)
'''a = "123   "
print(a.rstrip())

#output:123'''

#replace():Returns a string where a specified value is replaced with a specified value
'''a = "hel123"
print(a.replace("h","p"))

#output:pel123'''

#split():Splits the string at the specified separator, and returns a list

'''a = "sdftgju sddffgere"
print(a.split())

#output:['sdftgju', 'sddffgere']'''
#join():The join() method takes all items in an iterable and joins them into one string.

'''a=("adfg","hjut","asfdg")
print("fg".join(a))

#output:adfgfghjutfgasfdg'''

#startswith():method returns True if the string starts with the specified value, otherwise False.

'''a = "hi hellow"
print(a.startswith("hi"))

#output:True'''

#endswith():method returns True if the string ends with the specified value, otherwise False.
a="hi hello"
print(a.endswith("hello"))


#output:True
