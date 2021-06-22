# Dictionary in python 
# It is an unordered collection
# Used 'key'-'value' pairs to store values.
# it is identified with {} 
print("**********dictionary in python")

students_dic = {1 : 'Atishay' ,2 : 'Vikas' ,3 : 'Aakash' }
print(students_dic)

print("**********fetch value in python")

print(students_dic[2])

print("**********nested list in dictionary in python")

students_dic[4] = ['107 Simran sun' , 'indore' ,'mp']

print(students_dic)

print("********** fetch nested list element in dictionary in python")

print(students_dic[4][1])

print("********** modify nested list element in dictionary in python")
students_dic[4][2] = 'M.P.'

print(students_dic[4][2])

print("********** dictionary methods in python")
print("********** keys()")
print(students_dic.keys())

print("********** values()")
print(students_dic.values())

print("********** items()")
print(students_dic.items())

 

