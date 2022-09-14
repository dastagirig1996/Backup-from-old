#finding palindrome
n=int(input('Enter a number.......'))
num=n
reverse=0

while(n>0):
    rem=n%10
    reverse=reverse*10+rem
    n=n//10
if num==reverse:
    print(num,'is in palindrome')
else:
    print(num,'not in palindrome')
    
    
