n=int(input('enter the value....'))
s=len(str((n)))
num=n
k=0
d=0
while(d<=s):
    arm=n%10
    k=k+arm**s
    n=n//10
    d=d+1
if num==k:
    print(num,'is Armstrong')
else:
    print(num,'is not a Armstrong')
