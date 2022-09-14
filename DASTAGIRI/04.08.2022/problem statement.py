##13. Write a Python program to find the strings in a given list, starting with a given prefix.
##Input:
##[( ca,('cat', 'car', 'fear', 'center'))]
##Output:
##['cat', 'car']
##Input:
##[(do,('cat', 'dog', 'shatter', 'donut', 'at', 'todo'))]
##Output:
##['dog', 'donut']


ls=['cat', 'car', 'fear', 'center']
result=[]
for i in ls:
    if i.startswith("ca"):
        result.append(i)
print(result)
    
##Output:
##['cat', 'car']

