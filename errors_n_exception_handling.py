'''# try, except, finally
# We can use else block after except
'''
print('Test User login\n')


def add(num1, num2):
    return num1 + num2


if __name__ == '__main__':
    while True:
        num1 = 0
        num2 = 0
        try:
            num1 = int(input('Enter Number1:\n'))
            num2 = int(input('Enter Number2:\n'))

        except ValueError:
            print('Only Number accepted\n')
            continue

        else:
            print('sum = {}'.format(add(num1, num2)))
            decision = input('Want to try next?(Y/N)')
            if 'Y' == decision.upper():
                continue
            else:
                break
