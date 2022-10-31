# make user choose the operation --> needs if/elif for the operations to work
operation = input('''
Type the operation you wish to perform: 
+ addition
- subtration
* multiplication
/ division
''')

# input numbers
# use int() so that you cant enter words or symbols
number_1 = int(input('Enter a number: '))
number_2 = int(input('Enter a second number: '))

# operators: ADDITION
if operation == '+':
    print('{} + {} = '.format(number_1, number_2)) #restates the numbers in the output
    print(number_1 + number_2)

# operators: SUBTRACTION
elif operation == '-':
    print('{} - {} = '.format(number_1, number_2))
    print(number_1 - number_2)

# operators: MULTIPLICATION
elif operation == '*':
    print('{} * {} = '.format(number_1, number_2))
    print(number_1 * number_2)

# operators: DIVISION
elif operation == '/':
    print('{} / {} = '.format(number_1, number_2))
    print(number_1 / number_2)

else:
    print('Error: Please type a valid operator')