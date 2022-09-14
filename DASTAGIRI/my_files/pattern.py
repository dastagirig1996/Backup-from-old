##n=5
##s=1
##for i in range(n,0,-1):
##  for j in range(1,i):
##    print(" ",end=" ")
##  for k in range(0,s):
##    print(s,end=" ")
##  s=s+1
##  print("\r")


##n=5
##for i in range(1,n+1):
##  for j in range(1,n+1):
##    if i>j:
##      print(i,end=" ")
##    else:
##      print(j,end=" ")
##  print()

'''
1  
2  4  
3  6  9  
4  8  12  16  
5  10  15  20  25  
6  12  18  24  30  36  
7  14  21  28  35  42  49  
8  16  24  32  40  48  56  64 

'''
##n=9
##num=1
##k=1
##for rows in range(1,n):
##    num=num+1
##    for colums in range(1,rows+1):
##        num=num*colums
##        print(num,end=" ")
##        num=rows
##        
##        
##    print()

##n=8
##for i in range(1,n+1):
##    for j in range(1,i+1):
##        square=i*j
##        print(square,end=" ")
##    print()


count=1
flag=0
num=int(input('Enter number:'))
row=(num)
col=2
for i in range(row):
    for j in range(col):
        if flag==0:
            print(count,end='')
        else:
            print('*',end='')
            
    if i%2==0:
        flag=1
        count+=1
    else:
        flag=0
    col+=1
    print('\r')














































