import array as arr
ary=arr.array('i',(5,3,6,11,87,21,-65,24,32,4,7))
for i in range(0,7):
    print(ary[i],end=' ')
print(type(arr))


ary.insert(1,25)
for i in range(0,7):
    print(ary[i],end=' ')
print()

ary.append(65)
for i in range(0,(len(ary))):
    print(ary[i],end=' ')
