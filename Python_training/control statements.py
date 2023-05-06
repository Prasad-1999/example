a = int(input("Enter the a value:"))
b = int(input("Enter the b value:"))

# Conditional statements
# if statement
if a > b:
    print("Right statement")
print("Wrong statement")

# if-else statement
if a < b:
    print("Right statement")
else:
    print("Wrong statement")

# Nested if statement
if a > b:
    print("Right statement")
    if a == b:
        print("Equal statement")
    else:
        ("Not equal statement")
else:
    ("Wrong statement")

# if-elif-else statement
if a > b:
    print("Right statement")
elif b > a:
    print("Wrong statement")
else:
    print("Equal statement")

# Looping statements
# for statement
for i in range(1, 10, 1):
    print(i)

# while statement
x = 0
while x < 10:
    print(x)
    x += 1

# jumping statements
# Break statement
for y in 'prasad':
    if y == 's':
        break
    else:
        print(y)

# continue statement
for y in 'prasad':
    if y == 's':
        continue
    else:
        print(y)

# pass statement
for y in 'prasad':
    pass
