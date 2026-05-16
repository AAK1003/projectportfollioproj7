def check_number(prompt):
    while True:
        num = input(prompt)
        if num.isnumeric():
            return int(num)
        print('Invalid number, please respond again.')

def check_sign(prompt):
    while True:
        operation = input(prompt)
        if operation == '+' or operation == '-' or operation == '*' or operation == '/':
            return operation
        print('Invalid operation, please respond again.')

def operation(num1, num2, sign):
    if sign == '+':
        print('The sum is: ' + str(num1 + num2))
    elif sign == '-':
        print('The difference is: ' + str(num1-num2))
    elif sign == '*':
        print('The product is: ' + str(num1 * num2))
    elif sign == '/':
        if num2 == 0:
            print('The quotient is: Undefined')
        else:
            print('The quotient is: ' + str(num1 / num2))

num1 = check_number('What is the first number you want to calculate with(in 1+2=3, 1 would be first number)? ')
num2 = check_number('What is the second number you want to calculate with(in 1+2=3, 2 would be the second number)? ')
sign = check_sign('What is the operation you want to use on the numbers(+, -, *, /)? ')
operation(num1, num2, sign)
