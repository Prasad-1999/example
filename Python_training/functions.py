# Function
'''
1.A function is defined as the block of statements(or)collection of statements to perform the task
2.A function program is re-usable 
3.A function should work when the function called otherwise it will not work.
'''
# Function program.
'''
1.A function program consists of mainly three parts i.e 
1)function name
2)function body 
3)function calling
'''

# program syntax:
# Function name:
"A function name defined as the name of function"
# Function body:
"A function body consists of another function,looping function,conditional function"
# Function calling:
"A function calling consists of function name as calling element"

# program


def add(a, b):  # function name
    print(a+b)  # function body


add(3, 4)  # function calling

# arbitary arguments:
'''
1.An arbitary arguments consists of the multiple arguments for a single parameter(*a).
2.It return result in tuple form.
'''

# program:


def arb(*a):
    print(a)


arb(39, 41, 1)

# kwargs(keyword arguments):
'''
1.keyword arguments are similar to artibary arguments but differents parameter indication(**a)
2.It result in dictionary form like key-values 
'''
# program:


def kwargs(**a):
    print(a)


kwargs(name='prasad', degree='b.tech')

# global variable:
'''
1.global variable is used outside the function 
2.global name refers this variables use in the entire function
'''
# Local variable:
'''
1.Local variable uses inside of the function.
2.This variable will work only inside the function of the program.
'''
# program:
a = "prasad"  # global variable.


def variable():
    b = "gollapalli"  # local variable
    print(a, b)


variable()

# modulus:
"It is the simply combination of one(or)more functions."


def add(a, b):
    print(a+b)


def mul(a, b):
    print(a*b)


# ADVANCE PYTHON
'''
Advance python mainly consists of four functions.they are:
1.lambda
2.filter()
3.map()
4.reduce
'''
# lambda function:
'''
1.lambda function means simply it is a unknown function.
2.when we pass multiple arguments but the expression is one in program.
'''
# program syntax
'''
A program mainly consists of four parts
1)function object
2)lambda function
3)arguments
4)expressions 
'''

# program:


def y(a): return a**4


print(y(2))


# filter():
"filter function simply consists of a condition based on that condition it will print the elements."

# syntax:
"filter(function name,sequence)"

# program:
x = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def name(i):
    if i >= 4:
        return True
    else:
        return False


result = filter(name, x)
print(list(result))
