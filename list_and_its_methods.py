# list in python 
# list is an ordered collection. 
# list can store any type of value
# It supports both indexing and slicing like string in python.
# identified with [] 
 
print("********list in python")
char_list = ['a','t','i','s','h','a','y']
print(char_list)

print("********indexing in python list")

first_char = char_list[0]
print(first_char)

last_char = char_list[6]
print(last_char)

print("********slicing in python list")

sub_list = char_list[3::1]

print(sub_list)

print("********mixed data type list in python list")

all_type_list = ['String',10,15.33]
print(all_type_list)

print("********Sorting of list in python list")

char_list.sort()
print(char_list)

print("********reverse of list in python list")
char_list.reverse()
print(char_list)

print("********Removing element from list in python list")
char_list = ['a','t','i','s','h','a','y']

#remove last element  from list
char_list.pop() 

print(char_list)
#remove specific element  from list
char_list.pop(2) 
print(char_list)

print("********Adding element in list in python list")

char_list.append('y')
print(char_list)
#add specific element at any position from list
char_list[2] = 'new item'
print(char_list)

print("********concat two list in python list")

list_num = [1,2,3,4,5,6]
list_char = ['a','t','i','s','h','a','y']

concated_list = list_num + list_char
print(concated_list)

