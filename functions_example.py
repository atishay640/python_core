# functions


def greeting(name):
    '''
    :discription: This function creates greeting message.
    :param name: your name
    :return string: greeting message
    '''
    return "Hey " +name



print( help(greeting))

print('---------------------------------------------------')

def check_prime_num(given_num):
    flag = None
    for num in range(2,given_num):
        if given_num%num == 0:
            flag = False
            break;
        else:
            flag = True

    if flag:
        print('Prime')
    elif not flag:
        print('Not Prime')

check_prime_num(56)

print('----------------------------------------------------')

def extract_end(word):
    last_letters = word[len(word) - 2: len(word)]
    return last_letters*3

print(extract_end('Hello'))
print('----------------------------------------------------')

# SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order¶


def check_num(num_list):
    flag = False
    for index,num in enumerate(num_list):
        if num == 0:
            if num_list[index + 1] == 0:
                if num_list[index + 2] == 7:
                    flag = True

    return flag


print(check_num([1,2,4,0,7,5]))

print('-------------------check_prime_count---------------------------------')

# COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number

    # 2,3,5,7,11,13,17,19



def check_prime_count(num):
    list_for_check = list(range(2,num))
    count = 0
    flag = True
    for num in list_for_check:
        for num_2 in list_for_check:
            if num_2 >= num:
                break
            elif num_2 < num:
                if num%num_2 ==0:
                    flag =  False
            if flag:
                count = count + 1
    return count



print(check_prime_count(19))
print('----------------------------------------------------')

# count uppercase characters in a string


def check_upper_count():
    count = 0
    sentence = "My Name is Atishay Sharma and i am testing UPPER LETTER count"
    for letter in sentence:
        if letter.isupper():
            count = count + 1

    return count

print(check_upper_count())

print('----------------------------------------------------')

# collect unique elements from list

def unique_list():
    non_unique_list = [1,1,1,1,2,1,2,2,2,3,3,4,4,4,4,5,5,5,6,76,7,8,8,9,]
    num_unique_list = []
    for num in non_unique_list:
        if num not in num_unique_list:
            num_unique_list.append(num)
    return num_unique_list

print(unique_list())
