# variable argument
# *args

def cal_mean(*args):
    sum = 0
    for element in args:
        sum = sum + element

    return sum/len(args)

print(cal_mean(1,2,3,4,6,6,7,8,9,9,0))
print('----------------------------------------')

# variable argument(key, value)
# **args

def get_full_name(**kwargs):
    return kwargs['first'] + ' ' +  kwargs['last']


print(get_full_name(first = 'Atishay' , last = 'Sharma'))
print('----------------------------------------')

# both *args and **kwargs

def make_address( *args , **kwargs):
    return '{}'.format(args[0]) + ' '+kwargs['city'] +' '+ kwargs['state']  +' '+ kwargs['country']

print(make_address(107 , city='Indore',state='M.P',country='India'))

print('----------------------------------------')

#Function #10: skyline
# 'hello' to 'hElLo'
def convert_str(name):
    letter_list = list(name)
    for index,letter in enumerate(letter_list):
        if index%2==1:
            letter_list[index] = letter.upper()
    return str(''.join(letter_list))

print(convert_str('mystring'))

print('----------------------------------------')



