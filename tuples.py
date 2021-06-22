# tuples in python 
# tuples are immutable collection
# identified by ()
# indexing and slicing allowed

stu_list = (1,'a',102.3)
print(stu_list)

print("*********indexing")

print(stu_list[2])

print("*********slicing")

print(stu_list[1::])

print("*********immutablity")

#stu_list[2] = 111.11

print("*********concatination")

tuple_one = (1,2,3)
tuple_two = (10,20,30)
new_list = tuple_one + tuple_two
print(new_list)

print("*********methods")

print( len(new_list))

print(type(new_list))


