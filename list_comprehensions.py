# list comprehension

# without using list comprehension

word = 'atishay'
letter_list = []
for letter in word:
    letter_list.append(letter)
print(letter_list)
print('-------------------------------------------')

# with list  comprehension

letter_list = [ letter for letter in word]
print(letter_list)
print('-------------------------------------------')

# operation on element in list comprehension

num_list = [1,2,3,4,5,6,7,8,9]

sqr_num_list = [num**2 for num in num_list]
print(sqr_num_list)

print('-------------------------------------------')

list_div_by_3 = [ a for a in range(0 ,50) if a%3 == 0]
print(list_div_by_3)

print('-------------------------------------------')

list_fizz_buzz = list(range(1, 101))
for index,num in enumerate(list_fizz_buzz):
    if num %15 == 0:
        list_fizz_buzz[index] = 'fizzbuzz'
    elif num %3 == 0:
        list_fizz_buzz[index] = 'fizz'
    elif num %5 == 0:
        list_fizz_buzz[index] = 'buzz'

print(list_fizz_buzz)
print('-------------------------------------------')

sentence = 'create a list of first letter of this sentence.'
list_of_first_letters = []
for word in sentence.split(' '):
    list_of_first_letters.append(word[0])
print(list_of_first_letters)
