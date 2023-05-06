a = int(input("Enter the 1st number:"))
b = int(input("Enter the 2nd number:"))
option = int(input("Enter the option:"))
if option == 1:
    c = a+b  # it will add the numbers
    print("The result of adding two numbers:", c)
elif option == 2:
    c = a-b  # it will subtract the numbers
    print("The result of subtracting two numbers:", c)
elif option == 3:
    c = a*b  # it will multiply the numbers
    print("The result of multiplying two numbers:", c)
elif option == 4:
    c = a/b  # it will divison the numbers
    print("The result of dividing two numbers:", c)
else:
    print("Invalid number")
