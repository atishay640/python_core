
# counter in collection module
# returns dictionary

from collections import Counter

# to count number of occurance in a list
alist = [1,2,3,4,56,67,78,8,9,5,4,6,5,42,5,2,58,14,5,2,58,5,22954,21,55,42,5,8,2,5496521,8]

print(Counter(alist))

print('--------------------------------------------------------------------------------------')
# with string

astr = 'atishay sharma'
print(Counter(astr))

print('--------------------------------------------------------------------------------------')

list
# with string to count occurence of words in sentence

asentence = 'i want to talk but she do not want to talk to me when she is not in good mood.'
word_list = asentence.split()
print(Counter(word_list))


