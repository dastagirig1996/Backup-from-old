#1. WAP to print middle charector of the string
'''
st="announcemet"
c=0
for i in st:
    c=c+1
length=c//2    
print(st[length])
'''
##Output:
##n

#2.WAP to print half reverse of the string
##Input: KNOWLEDGE
##Output: EGDELKNOW
'''
st="KNOWLEDGE"
lenth_st=len(st)//2

st1=st[::-1]
lenth_st1=len(st1)//2


print((st1[0:(lenth_st1)+1])+(st[0:lenth_st]))
'''
##Output:
##EGDELKNOW

#3. WAP to remove all the vowels from the given string 
'''
st="environment"
vowels="aeiou"
new=""
for ch in st:
    if ch in vowels:
        continue
    else:
        new=new+ch
         
print(new)
'''
##Output:
##nvrnmnt

#4. WAP to insert * in front of every vouels in the string.

##Input: BANANA
##Output: B*AN*AN*A
'''
st="BANANA"
st1=""

for ch in st:
    if ch=="A":
        st1=st1+"*"+"A"
    else:
        st1=st1+ch
print(st1)
'''
##Output:
##B*AN*AN*A


#5.WAP to count number of words in the string.
'''
st="Sharing of resources was not delimited by household boundaries"
ls=st.split()
c=0
for i in ls:
    c=c+1
print("number of words",c)
'''
##Output:
##number of words 9

#6.WAP to remove extra space from the given string 
'''
st="    environment pollution"
print(st.strip())
'''
##Oupput:
##environment pollution


#7.WAP to insert string in between the given string
##Input: Ojas technologies 
##Output: Ojas innovative technologies 
'''
st="Ojas technologies"
add="innovative"
ls=st.split()
ls.insert(1,add)
st1=" ".join(ls)
print(st1)
'''
##Output:
##Ojas innovative technologies

#8.WAP to find the ascci value of given char
'''
char=input("enter charecter..")
print(ord(char))
'''
##Output:
##enter charecter..s
##115

#9.insert ojas in front of every string 
'''
st="hello"
st1=""

for ch in st:
    st1=st1+"ojas"+ch
print(st1) 
'''   
##Output:
##ojashojaseojaslojaslojaso

#10.insert ojas in every extra space in the string
'''
st="     environment pollution    "
st1=""
for ch in st:
    if ch==" ":
       st1=st1+"*"
    else:
        st1=st1+ch
print(st1)
'''
##Output:
##*****environment*pollution****




