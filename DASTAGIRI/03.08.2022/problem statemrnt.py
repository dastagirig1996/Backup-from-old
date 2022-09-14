##Write a program to check whether the given password is valid or not .
##conisder the password to be valid if it contain at least one digit ands one capital.
##
##input:it will be a single line containng string
##output: valid password or invalid password
##ex:GJ22191gopi
##
##ouput:valid password
password=input("Enter your password")
num_flag=False
letter_flag=False
for i in password:
    if i.isupper():
        letter_flag=True
    elif i.isnumeric():
        num_flag=True
    
    if num_flag and letter_flag:
        print("valid Password")
        break
else:
    print("invalid password")
##Output:
##Enter your passwordHllkih55d
##valid Password
