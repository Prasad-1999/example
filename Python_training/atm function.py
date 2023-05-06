# Atm program using function

amount = int(input("Enter the amount:"))  # amount
option = input("Enter the option:")


def credit(amount):
    return amount  # return credited amount


def debit(amount):
    # Enter the cash to take from total amount
    cash = int(input("Enter the cash:"))
    if amount > cash:
        return amount - cash  # return debited amount
    if amount < cash:
        return 'invalid cash'  # return invalid cash if cash more than amount


if option == '+':
    print(credit(amount))
if option == '-':
    print(debit(amount))
