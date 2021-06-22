# lambda
# map function : to apply some operation on collection use it
# filter function : to filter the collection use it

# without lambda function

def square(num):
    return num**2

num_list = [1,2,3,4,5,6,8,9]

num_list_sqr = list(map(square,num_list))

print(num_list_sqr)
print('-----------------------------')
# with lambda or anonymous function

num_list_sqr = list( map(lambda num:num**2 , num_list))
print(num_list_sqr)

print('-----------------------------')

num_list = [1,2,3,4,5,6,7,8,9]

odd_num_list = list( filter(lambda num :  num%2==1 , num_list ))
print(odd_num_list)
