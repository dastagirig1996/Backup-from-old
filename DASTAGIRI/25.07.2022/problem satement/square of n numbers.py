# Finding squares upto n
n=int(input("Enter n value :"))
ls=[]
if 1<=n<=20:
    for i in range(0,n):
        s=i**2
        ls.append(s)
for i in ls:
    print(i,"\t")
        
