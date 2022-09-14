#wapp using  function of fibonacci series
def fibb(a,b,n):
    c=0
    while(c<n):
        print(a)
        nextelement=a+b
        a=b
        b=nextelement
        c=c+1
fibb(0,1,5)
