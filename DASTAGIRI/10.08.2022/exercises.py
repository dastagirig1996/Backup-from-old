#1.Display square and perfect square root of numbers from 48 to 82. using list Comprehension.
'''

ls=[x**2 for x in range(48,83) ]
print(ls)

s={x for x in range(48,83) for y in range(1,x) if x**(1/2)%y==0}
print(s)
'''
##Output:
##[2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225,
## 4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724]
##{64, 49, 81}
    
#2.Display square and perfect square root of numbers from 48 to 82. using dictionary Comprehension.
  
'''
dic={value:**2 for key in range(48,83) for value in range(1,83//2) if key**(1/2)%value==0  }
print(dic)
'''

##Output:
##{48: 2304, 49: 2401, 50: 2500, 51: 2601, 52: 2704, 53: 2809, 54: 2916, 55: 3025, 56: 3136, 57: 3249, 58: 3364,
## 59: 3481, 60: 3600, 61: 3721, 62: 3844, 63: 3969, 64: 4096, 65: 4225, 66: 4356, 67: 4489, 68: 4624, 69: 4761,
## 70: 4900, 71: 5041, 72: 5184, 73: 5329, 74: 5476, 75: 5625, 76: 5776, 77: 5929, 78: 6084, 79: 6241, 80: 6400,
## 81: 6561, 82: 6724}
'''
import math
dic1={math.floor(k**0.5):k for k in range (48,83) if (math.sqrt(k)==math.floor(math.sqrt(k)))}
print(dic1)
'''
##Output:
##{7: 49, 8: 64, 9: 81}

#3.if the square of number inside list is divisible by 2 print the num.(1st question's answer should be taken as a list)
'''
lst=[2304, 2401, 2500, 2601, 2704, 2809, 2916, 3025, 3136, 3249, 3364, 3481, 3600, 3721, 3844, 3969, 4096, 4225,4356, 4489, 4624, 4761, 4900, 5041, 5184, 5329, 5476, 5625, 5776, 5929, 6084, 6241, 6400, 6561, 6724]

ls=[x for x in lst if x%2==0 ]
print(ls)
'''

##Output:
##[2304, 2500, 2704, 2916, 3136, 3364, 3600, 3844, 4096, 4356, 4624, 4900, 5184, 5476, 5776, 6084, 6400, 6724]




















