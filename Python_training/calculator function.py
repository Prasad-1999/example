# calculator program using module function.
a = int(input("Enter the a value:"))
b = int(input("Enter the b value:"))
option = input("Enter the option:")


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


if option == '+':
    print(add(a, b))
if option == '-':
    print(sub(a, b))
if option == '*':
    print(mul(a, b))
if option == '/':
    print(div(a, b))
