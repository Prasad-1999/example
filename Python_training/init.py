class mobile():
    def __init__(self, name, ram, rom, price):
        self.a = name
        self.b = ram
        self.c = rom
        self.d = price

    def prasad(self):
        print(self.a, self.b, self.c, self.d)


while True:
    name = input("Enter the mobile name:")
    ram = input("Enter the mobile ram:")
    rom = input("Enter the mobile rom:")
    price = input("Enter the mobile price:")
    phone = mobile(name, ram, rom, price)
    phone.prasad()
