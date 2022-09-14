 # fibonacci series
n=int(input('Enter the Number....'))
b1=0
b2=1
d=0
while(d<=n):
    print(b1)
    nextem=b1+b2
    b1=b2
    b2=nextem
    d=d+1
