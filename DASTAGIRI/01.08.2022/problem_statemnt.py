'''You are required to enter a word that consists of x and y 
that denote the number of Zs and Os respectively. The input word is considered similar to word zoo if 2 * x = y


Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

    First line: A word that starts with several Zs and continues by several Os.
    Note: The maximum length of this word must be 20.

    

Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.

instruction
-----------
if input = zzzoooooo then print "yes".
if input = zzooo print "no"'''

st=input("Enter:")
x='z'
y='o'
size=0
size1=0
for ch in st:
    if ch ==x:
        size=size+1
        continue
    if ch ==y:
        size1=size1+1
if (size**2)==size1:
    print("yes")
else:
    print("no")
    
