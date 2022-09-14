#dictionary methods

#clear():Removes all the elements from the dictionary

'''a={"a":1,"b":2,"c":3,"d":5}
a.clear()
print(a)

#output:{}'''

#copy():copies one  tuple to other tuple

'''a={"a":4,"b":2,"c":3}
b = a.copy()
print(b)

#output:{'a': 4, 'b': 2, 'c': 3}'''

#fromkeys():Returns a dictionary with the specified keys and value
'''
p =('a','b','c')
q=(0,1,2)
print(dict.fromkeys(p,q))

'''
#output:{'a': (0, 1, 2), 'b': (0, 1, 2), 'c': (0, 1, 2)}

#get():Returns the value of the specified key
'''
a = {'aa':123,'bb':354,'cc':567}
print(a.get("aa"))
'''

#output:123


#items():Returns a list containing a tuple for each key value pair

'''a = {'aa':123,'bb':567,'cc':678,'dd':987}
print(a.items())

#output:dict_items([('aa', 123), ('bb', 567), ('cc', 678), ('dd', 987)])'''

#keys():Returns a list containing the dictionary's keys

'''a ={'a':12,'b':45,'c':67,'d':89}
print(a.keys())

#output:dict_keys(['a', 'b', 'c', 'd'])'''

#pop():Removes the element with the specified key

'''a = {'a':34,'b':56,'c':78,'d':89}
a.pop('a')
print(a)

#output:{'b': 56, 'c': 78, 'd': 89}'''


#popitem():Removes the last inserted key-value pair

'''a={'a':23,'b':54,'c':78,'d':78}
a.popitem()
print(a)

#output:{'a': 23, 'b': 54, 'c': 78}'''

#setdefault():Returns the value of the specified key. If the key does not exist: insert the key,
#with the specified value
'''
a={'a':'aa','b':'bb','c':'cc','d':'dd'}
b = a.setdefault('a',"f")
print(b)
'''
#output:aa

'''a = {'a':'aa','b':'bb','c':'cc','d':'dd'}
b = a.setdefault('e','ee')
print(b)

#output:ee'''

#update():Updates the dictionary with the specified key-value pairs
'''
a = {'name':'sai','age':12,'class':7}
a.update({"hello":125})
print(a)'''
#output:{'name': 'sai', 'age': 12, 'class': 7, 'hello': 125}

#values():Returns a list of all the values in the dictionary

'''a = {'name':'sai','age':12,'class':7}
b=a.values()
print(b)

#output:dict_values(['sai', 12, 7])'''
