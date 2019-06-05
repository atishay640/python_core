#sets in python
# unique and unordered collection

myset = set()
myset.add(1)
myset.add(2)
myset.add(2) #only unique element

#list to set
mylist = [1,23,4,5,6,77,7,7,77,'a',7,7221]
myset = set(mylist) # set has only unique elements of list
print(myset)
