'''
Advanced Python Objects Test
'''
from collections import Counter

#Problem 1: Convert 1024 to binary and hexadecimal representation
from itertools import count

num = 1024
bi = bin(1024)
print(bi)

#Problem 2: Round 5.23222 to two decimal places

num = 5.23222
rou = round(number= num , ndigits=2)
print(rou)

#Problem 3: Check if every letter in the string s is lower case

s= 'hello how are you Mary, are you feeling okay?'

is_low = s.islower()
print(is_low)

#Problem 4: How many times does the letter 'w' show up in the string below?

s = 'twywywtwywbwhsjhwuwshshwuwwwjdjdid'

print(Counter(s)['w'])



#Problem 5: Find the elements in set1 that are not in set2:

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set1 - set2)


#Problem 6: Find all elements that are in either set:

set1 = {2,3,1,5,6,8}
set2 = {3,1,7,5,6,8}

print(set1.union(set2))


#Problem 7: Create this dictionary: {0: 0, 1: 1, 2: 8, 3: 27, 4: 64} using a dictionary comprehension.

dic = {num : num**3  for num in range(0,5) }
print(dic)

#Problem 8: Reverse the list below:

list1 = [1,2,3,4]

print(list(reversed(list1)))
print(list1)

#Problem 9: Sort the list below:
list2 = [3,4,2,5,1]
list2.sort(reverse=True)
print(list2)


