# Write the table with the nested for loop program
num = int(input("enter the number:"))
for i in range(1, num+6):
    for j in range(1, i+1):
        print(num, '*', j, "=", num*j)
    print()
