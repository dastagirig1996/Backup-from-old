#1.Find all of the numbers from 1-1000 that are divisible by 7
'''
ls=[i for i in range(1,1001) if i%7==0]
print(ls)
'''
#Output:
####[7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105, 112, 119, 126, 133, 140, 147, 154, 161, 168, 175, 182,
#### 189, 196, 203, 210, 217, 224, 231, 238, 245, 252, 259, 266, 273, 280, 287, 294, 301, 308, 315, 322, 329, 336, 343,
#### 350, 357, 364, 371, 378, 385, 392, 399, 406, 413, 420, 427, 434, 441, 448, 455, 462, 469, 476, 483, 490, 497, 504,
#### 511, 518, 525, 532, 539, 546, 553, 560, 567, 574, 581, 588, 595, 602, 609, 616, 623, 630, 637, 644, 651, 658, 665,
#### 672, 679, 686, 693, 700, 707, 714, 721, 728, 735, 742, 749, 756, 763, 770, 777, 784, 791, 798, 805, 812, 819, 826,
#### 833, 840, 847, 854, 861, 868, 875, 882, 889, 896, 903, 910, 917, 924, 931, 938, 945, 952, 959, 966, 973, 980, 987, 994]

#2.Find all of the numbers from 1-1000 that have a 3 in them 
'''
ls=[i for i in range(1,1000) if "3" in str(i)]
print(ls)
'''
#Output:
##[3, 13, 23, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 43, 53, 63, 73, 83, 93, 103, 113, 123, 130, 131, 132, 133, 134, 135,
## 136, 137, 138, 139, 143, 153, 163, 173, 183, 193, 203, 213, 223, 230, 231, 232, 233, 234, 235, 236, 237, 238, 239, 243,
## 253, 263, 273, 283, 293, 300, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 311, 312, 313, 314, 315, 316, 317, 318,
## 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329, 330, 331, 332, 333, 334, 335, 336, 337, 338, 339, 340, 341, 342,
## 343, 344, 345, 346, 347, 348, 349, 350, 351, 352, 353, 354, 355, 356, 357, 358, 359, 360, 361, 362, 363, 364, 365, 366,
## 367, 368, 369, 370, 371, 372, 373, 374, 375, 376, 377, 378, 379, 380, 381, 382, 383, 384, 385, 386, 387, 388, 389, 390,
## 391, 392, 393, 394, 395, 396, 397, 398, 399, 403, 413, 423, 430, 431, 432, 433, 434, 435, 436, 437, 438, 439, 443, 453,
## 463, 473, 483, 493, 503, 513, 523, 530, 531, 532, 533, 534, 535, 536, 537, 538, 539, 543, 553, 563, 573, 583, 593, 603,
## 613, 623, 630, 631, 632, 633, 634, 635, 636, 637, 638, 639, 643, 653, 663, 673, 683, 693, 703, 713, 723, 730, 731, 732,
## 733, 734, 735, 736, 737, 738, 739, 743, 753, 763, 773, 783, 793, 803, 813, 823, 830, 831, 832, 833, 834, 835, 836, 837,
## 838, 839, 843, 853, 863, 873, 883, 893, 903, 913, 923, 930, 931, 932, 933, 934, 935, 936, 937, 938, 939, 943, 953, 963,
## 973, 983, 993]


#3.Count the number of spaces in a string
'''
st="An enriching course designed by the experts to help you crack the coding"
ls=[s for s in st if s==" "]
print(len(ls))
'''
##Output:
##12

#4.Create a list of all the consonants in the string
# “Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams” 
'''
st="Yellow Yaks like yelling and yawning and yesturday they yodled while eating yuky yams"

vowels="aeiou AEIOU"

ls=[c for c in st if c not in vowels]
print(ls)
'''
##Output:    
##['Y', 'l', 'l', 'w', 'Y', 'k', 's', 'l', 'k', 'y', 'l', 'l', 'n', 'g', 'n', 'd', 'y', 'w', 'n', 'n', 'g', 'n', 'd',
## 'y', 's', 't', 'r', 'd', 'y', 't', 'h', 'y', 'y', 'd', 'l', 'd', 'w', 'h', 'l', 't', 'n', 'g', 'y', 'k', 'y', 'y',
## 'm', 's']


#5.Get the index and the value as a tuple for items in the list “hi”, 4, 8.99, ‘apple’, (‘t,b’,’n’).
#  Result would look like (index, value), (index, value) 
'''
ls=["hi", 4, 8.99, 'apple', ('t','b','n')]

ls=[(index,value) for index,value in  enumerate(ls) ]
print(ls)
'''
##Output:
##[(0, 'hi'), (1, 4), (2, 8.99), (3, 'apple'), (4, ('t', 'b', 'n'))]


#6.Find the common numbers in two lists (without using a tuple or set) list_a = 1, 2, 3, 4, list_b = 2, 3, 4, 5 
'''
list_a = [1, 2, 3, 4]
list_b = [2, 3, 4, 5]

ls=[x for x in list_a if x in list_b]
print(ls)
'''
##Output:
##[2, 3, 4]

#7.Get only the numbers in a sentence like "In 1984 there were 13 instances of a protest with over 1000
 # people attending"
'''
txt="In 1984 there were 13 instances of a protest with over 1000 people attending"

ls=[int(c) for c in txt if c.isdigit()]
print(ls)
'''
##Output:
#[1, 9, 8, 4, 1, 3, 1, 0, 0, 0]

#8.Given numbers = range(20), produce a list containing the word ‘even’ if a number in the numbers is even,
#  and the word ‘odd’ if the number is odd. Result would look like ‘odd’,’odd’, ‘even’ 
'''
ls=["even" if i%2==0 else "odd" for i in range(20) ]
print(ls)
'''
##Output:
##['even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even',
## 'odd', 'even', 'odd', 'even', 'odd']

#9.Produce a list of tuples consisting of only the matching numbers in these lists list_a = 1, 2, 3,4,5,6,7,8,9,
#  list_b = 2, 7, 1, 12. Result would look like (4,4), (12,12) 
'''
list_a = [1, 2, 3,4,5,6,7,8,9]
list_b = [2, 7, 1, 12]

ls=[(s,s) for s in list_a if s in list_b ]
print(ls)
'''

##Output:
##[(1, 1), (2, 2), (7, 7)]


#10.Find all of the words in a string that are less than 4 letters 

'''
st="Given a string, the task is to write a Python program to count the number of spaces in the string."

ls=[w for w in st.split(" ") if len(w)<4]
print(ls)
'''
##Output:
##['a', 'the', 'is', 'to', 'a', 'to', 'the', 'of', 'in', 'the']

#11.Use a nested list comprehension to find all of the numbers from 1-1000
#   that are divisible by any single digit besides 1 (2-9)
 
#print([i for i in range(1,1000) for j in range(2,10) if i%j==0])

#12.
##a.Turn every item of a list into its square 
##b.Concatenate two lists index-wise list1 = ["M", "na", "i", "Ke"] 
##
##list2 = ["y", "me", "s", "lly"] 
##
##Expected output: ['My', 'name', 'is', 'Kelly'] 
##
##['My', 'name', 'is', 'Kelly'] list1 = ["Hello ", "take "] 
##
##list2 = ["Dear", "Sir"] 
##
##Expected output: ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir'] 

'''

ls1=[x**2 for x in range(1,5) ]
print(ls1)

'''

##Output:
##[1, 4, 9, 16]


#b.
'''
list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]


ls=[e+f for e,f in zip(list1,list2)]
print(ls)
'''
#output:
##['My', 'name', 'is', 'Kelly']
'''

list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]

ls=[ (a,b) for a in list1 for b in list2]
print(ls)
'''
##Output:
##[('Hello ', 'Dear'), ('Hello ', 'Sir'), ('take ', 'Dear'), ('take ', 'Sir')]
##

#13.Extend nested list by adding the sublist 
##list1 = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"] 
### sub list to add 
##
##sub_list = ["h", "i", "j"] 
##
##Expected Output: 

#['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']

'''

list1=["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

sub_list = ["h", "i", "j"]


list1[2][1][2].extend(sub_list)
print(list1)
'''
##Output:
##['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']


#14.Finding Transpose of a Matrix using
#  ListComprehension matrix = [[1, 2], [3,4], [5,6], [7,8]] o/p: [[1, 3, 5, 7], [2, 4, 6, 8]] 


'''
m = [[1, 2], [3,4], [5,6], [7,8]] 
print([[m[j][i] for j in range(len(m))] for i in range(len(m[0]))])
'''

##Output:
##[[1, 3, 5, 7], [2, 4, 6, 8]]

#15.Reverse each String in a Tuple

st="Given a string, the task is to write a Python program to count the number of spaces in the string."

ls=st.split(" ")
#tp=tuple(ls)

ls1=[i[::-1] for i in input(ls)]
print(ls1)



