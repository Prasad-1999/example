cash = [1000, 2000, 3000]
amount = int(input("Enter the amount:"))
option = int(input("Enter the option:"))
if option == 1:
    cash.append(amount)
    print(cash)
elif option == 2:
    cash.remove(amount)
    print(cash)
else:
    print("invalid number")
