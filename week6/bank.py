class Bank:
    def __init__(self):
        self.accounts = []

class Account:
    def __init__(self, accountName, amount, dateOfCreation):
        self.accoutName = accountName
        self.amount = amount
        self.dateOfCreation = dateOfCreation


class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

b = Bank()
ac = Account("savings", 123, "26/06/1992")
cu = Customer("Per Poulsen", 102)


ask = input("What would you like to do today?\n1: Add new account\n2: See account details\n3: See customer details\n")

if (ask == "1"):
    b.accounts.append(Account("checkings", 111, "23/11/2003"))
    print("added ", b.accounts[0])
elif (ask == "2"):
    print(ac.__dict__)
elif (ask == "3"):
    print(cu.__dict__)
else:
    print("Something went wrong, please try again")