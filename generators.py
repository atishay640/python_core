'''
Generators
'''

# def sqr_without_generator(n):
#     squares = []
#     for num in range(n):
#         squares.append(num**2)
#
#     return squares
#
# print(sqr_without_generator(10))


'''
Problem 1
Create a generator that generates the squares of numbers up to some number N.
'''
def sqr_with_generator(n):
    for num in range(n):
        yield num**2


for num in sqr_with_generator(10):
    print(num)

print('----------------------------------------------------------------------------')
'''
Problem 2
Create a generator that yields "n" random numbers between a low and high number (that are inputs). 
Note: Use the random library. For example:
'''

import random

def generate_random(from_ , to_ , n):
    for num in range(n):
        a= random.randint(from_,to_)
        yield a

for num in generate_random(1,20,10):
    print(num)
print('----------------------------------------------------------------------------')

'''
Problem 3
Use the iter() function to convert the string below into an iterator:
'''

s = 'hello'
siter = iter(s)
print(next(siter))
print(next(siter))
print('----------------------------------------------------------------------------')
