import math

def addition(num1, num2):
    total_sum = num1 + num2
    print(f"The total sum of your addition is {total_sum}.")

def subtraction(num1, num2):
    total_difference = num1 - num2
    print(f"The total difference of your subtraction is {total_difference}")

def multiplication(num1, num2):
    total_product = num1 * num2
    print(f"The total product of your multiplication is {total_product}")

def division(num1, num2):
    total_divided = num1 / num2
    print(f"The total divided result of your division is {total_divided}")

def exponent(num1, num2):
    total_exponentiation = num1 ** num2
    print(f"The total exponentiation of your exponent operation is {total_exponentiation}")

def square_root(num1):
    total_root = math.sqrt(num1)
    print(f"The result of your square root is {total_root}")


keep_going = True
while keep_going == True:
    operation = input("Welcome to the calculator, what operation do you want  to preform(+, -, *, /, ^, or root)? ")
    if operation == "+":
        num1 = float(input("What is the first number you want to add? "))
        num2 = float(input("What is the second number you want to add? "))
        addition(num1, num2)
    elif operation == "-":
        num1 = float(input("What is the first number you want to subtract(this will be the number that is not negative)? "))
        num2 = float(input("What is the second number you want to subtract? "))
        subtraction(num1, num2)
    elif operation == "*":
        num1 = float(input("What is the first number you want to multiply? "))
        num2 = float(input("What is the second number you want to multiply? "))
        multiplication(num1, num2)
    elif operation == "/":
        num1 = float(input("What is the first number you want to divide(you will divide this by the second number)? "))
        num2 = float(input("What is the second number you want to divide? "))
        division(num1, num2)
    elif operation == "^":
        num1 = float(input("What is the first number you want as the base? "))
        num2 = float(input("What is the number you want to exponentiate the base by? "))
        exponent(num1, num2)
    elif operation == "root":
        num1 = float(input("What is the number you want to square root? "))
        square_root(num1)
    keep_going = input("Do you want to keep calculating(Y or N)? ").upper()
    if keep_going == "Y":
        keep_going = True
    else:
        keep_going = False
    if keep_going == False:
        break