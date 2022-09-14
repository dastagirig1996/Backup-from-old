# Finding Prime Numbers
ls=[]
n=int(input('Enter Number....'))
for i in range(1,n+1):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        ls.append(i)
print('List of Prime Numbers',ls)
