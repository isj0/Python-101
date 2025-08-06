#!/usr/bin/env python3


num1 = float(input("Enter first number: "))
num2 = float(input('Enter second number: '))

operation = input('Choose the operation (+, -, *, /): ')

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Invalid Operation'
else:
    result = 'Invalid Operation selected.'

print(result)