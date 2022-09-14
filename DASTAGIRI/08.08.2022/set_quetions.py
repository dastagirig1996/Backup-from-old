#1.Add a list of elements to a given set
'''
ls=[5,7,8,1,5,4,7,8,2,66,25,3]
s=set(ls)
print(s)
'''

##Output:
##{1, 2, 66, 4, 5, 3, 7, 8, 25}


#2.Return a set of identical items from a given two sets
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5,88,9}

s3=s1.intersection(s2)
print(s3)

s4=s1&s2
print(s4)

s5=set()
for i in s1:
    if i in s2:
        s5.add(i)
print(s5)
'''
##Output:
##5 heloo 7
##5 heloo 7
##5 heloo 7

#3. Returns a new set with all items from both sets by removing duplicates
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5,88,9}

s3=s1|s2
#or
s4=s1.union(s2)

print(s3)
print(s4)


s5=set()
for i in s1:
    s5.add(i)
for j in s2:
    s5.add(j)
print(s5)
'''
#Output:
#{'heloo', 5, 7, 9, (2, 5, 1), 86, 88}
#{'heloo', 5, 7, 9, (2, 5, 1), 86, 88}
#{'heloo', 5, 7, 9, (2, 5, 1), 86, 88}


#4.Given two Python sets, update first set with items that exist only in the first set and not in the second set.
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5,88,9}
s3=set()
for el in s1:
    if el not in s2:
        s3.add(el)
print(s3)

s4=s1-s2
print(s4)

s5=s1.difference(s2)
print(s5)

'''
##Output:
##{86, (2, 5, 1)}
##{86, (2, 5, 1)}
##{86, (2, 5, 1)}


#5.Remove 10, 20, 30 elements from a following set at once
'''
s1={10,20,30,40,50,60,70,80}
s1.difference_update({10,20,30})
print(s1)
'''
##Output:
##{70, 40, 80, 50, 60}

#6.Return a set of all elements in either A or B, but not both
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5,88,9}

s1.difference_update(s2)
print(s1)
'''
##Output:
##{86, (2, 5, 1)}

#7.Determines whether or not the following two sets have any elements in common.
#  If yes display the common elements
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5,88,9}

s1.intersection_update(s2)
print(s1)
'''
##Output:
##{5, 'heloo', 7}

#8. Update set1 by adding items from set2, except common items
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5,88,9}

s1.symmetric_difference_update(s2)
print(s1)
'''
##Output:
##{86, 88, 9, (2, 5, 1)}


#9. Remove items from set1 that are not common to both set1 and set2
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5,88,9}

s1.difference_update(s2)
print(s1)
'''
##Output:
##{86, (2, 5, 1)}

#10.Write a Python program to check if a given set is superset of itself and superset of another given set
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5}
s3={5,8,7}

a=s1.issuperset(s1)
print(a)

b=s1.issuperset(s2)
print(b)

c=s1.issuperset(s3)
print(c)
'''
###Output:
##True
##True
##False

#11.a Python program to check a given set has no elements in common with other given set
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5,88}

s1.difference_update(s2)
print(s1)
'''
##Output:
##{86, (2, 5, 1)}

#12.Write a Python program to remove the intersection of a 2nd set from the 1st set.
'''
s1={5,7,86,"heloo",(2,5,1)}
s2={"heloo",7,5,88,9}

s2.difference_update(s1)
print(s2)
'''
##Output:
##{88, 9}

#13. Perform all sets methods by taking an example of your own.


##add()	Adds an element to the set
##clear()	Removes all the elements from the set
##copy()	Returns a copy of the set
##difference()	Returns a set containing the difference between two or more sets
##difference_update()	Removes the items in this set that are also included in another, specified set
##discard()	Remove the specified item
##intersection()	Returns a set, that is the intersection of two or more sets
##intersection_update()	Removes the items in this set that are not present in other, specified set(s)
##isdisjoint()	Returns whether two sets have a intersection or not
##issubset()	Returns whether another set contains this set or not
##issuperset()	Returns whether this set contains another set or not
##pop()	Removes an element from the set
##remove()	Removes the specified element
##symmetric_difference()	Returns a set with the symmetric differences of two sets
##symmetric_difference_update()	inserts the symmetric differences from this set and another
##union()	Return a set containing the union of sets
##update()	Update the set with another set, or any other iterable


#p={5,7,86,"heloo",(2,5,1)}
#q={"heloo",7,5,88,9}



##add()
'''
p.add(100)
print(p)
'''
##Output:
##{100, 5, 86, 7, 'heloo', (2, 5, 1)}

##clear()
'''
r={55,2,5,48,99,12}
r.clear()
print(r)
'''
##Output:
##set()

##copy()
'''
t=p.copy()
print(t)
'''
##Output:
##{5, 86, 7, 'heloo', (2, 5, 1)}

##difference()
'''
u=p.difference(q)
print(u)
'''
##Output:
##{86, (2, 5, 1)}


##p={100,5,7,86,"heloo",(2,5,1)}
##q={"heloo",7,5,88,9}


##difference_update()
'''
p.difference_update(q)
print(p)
'''
##Output:
##{100, 86, (2, 5, 1)}


##discard()
'''
p.discard(100)
print(p)
'''
##Output:
##{'heloo', 5, 86, 7, (2, 5, 1)}

p={5,7,86,"heloo",(2,5,1)}
q={"heloo",7,5,88,9}

##intersection()
'''
t=p.intersection(q)
print(t)
'''
##Output:
##{7, 5, 'heloo'}


##intersection_update()
'''
p.intersection_update(q)
print(p)
'''
##Output:
##{'heloo', 5, 7}

##isdisjoint()
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z= {"banana","mango","amazon"}

c=x.isdisjoint(y)
print(c)

d=x.isdisjoint(z)
print(d)
'''
##Output:
##True
##False

##issubset()

x = {"a", "b", "c",}
y = {"f", "e", "d", "c", "b", "a"}
'''
z=x.issubset(y)
print(z)
'''

##Output:
##True

##issuperset()
'''
z=y.issuperset(x)
print(z)
'''
##Output:
##True

##pop()
'''
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)
'''
##Output:
##{'apple', 'cherry'}


##remove()
'''
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")
print(fruits)
'''
##Output:
##{'cherry', 'apple'}

##symmetric_difference()
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.symmetric_difference(y)
print(z)
'''
##Output:
##{'cherry', 'microsoft', 'google', 'banana'}

##symmetric_difference_update()
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.symmetric_difference_update(y)
print(x)
'''
##Output:
#{'google', 'banana', 'cherry', 'microsoft'}

##union()
'''
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z=x.union(y)
print(z)
'''
##Output:
##{'google', 'cherry', 'microsoft', 'apple', 'banana'}

##update()

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.update(y)
print(x)

##Output:
##{'apple', 'microsoft', 'banana', 'cherry', 'google'}






























































