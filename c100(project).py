class ATM(object):
    def __init__(self, name, surname, pin, bank):
        self.name = name
        self.surname = surname
        self.pin = pin
        self.bank = bank

    def insterCash(self, insert):
        self.insert = insert
        insert = input("how much would you like to insert? ")
        print(insert, "has been inserted")

    def withCash(self, withdraw):
        self.withdraw = withdraw
        withdraw = input("how much would you like to withdrawed? ")
        print(withdraw, "has been withdrawed")


jhon = ATM("Jhon", "maxwell", "1234", "peak")
print(jhon.bank)
