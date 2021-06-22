# useful operators in python
# range, enumeration, zip , in , min , max

# range : generates number in given range. it's syntex is similer as slicing

generated_list = list(range(0,11))
print(generated_list)

print('--------------------------------')
# generate a list of even num upto 100

generated_list = list (range(0 , 101 ,2))
print(generated_list)
print('--------------------------------')

# enumeration : unzip the values from a collection

new_list = ['a','b','c','d']

for index,value in enumerate(new_list):
        print(index,value)
print('--------------------------------')

# zip: combine two collections into a single one. it works just opposite to enumerate

list1 = ['a','b','c']
list2 = [1,2,3]

zipped = zip(list1, list2)
list3 = list(zipped)
print(list3)
print('--------------------------------')

# in: use for finding element exist in collection

isExist = 'a' in list1
print(isExist)

isExist = 'z' in list1
print(isExist)
print('--------------------------------')

# min/max : find min or max value from collection

minX = min(list1)
print(minX)

max2 = max(list2)
print(max2)
print('--------------------------------')

# import function from any module

from random import randint

randon_int = randint(0,100)
print(randon_int)

print('--------------------------------')
