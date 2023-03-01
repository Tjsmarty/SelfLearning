class BankAccount:
    def __init__(self, name, bal=0):
        self.name = name
        self.bal = bal

    def deposit(self, amount):
        if amount > 0:
            self.bal += amount
        print(f"{amount} was deposited in your account \nYour account balance is now {account1.bal}")

    def withdraw(self, withdrawal_amount):
        if 0 < withdrawal_amount <= self.bal:
            self.bal -= withdrawal_amount
            print(f"You have withdrawn {withdrawal_amount} from your account\nYour account balance is now {self.bal}")
        else:
            print("sorry you have insufficient amount")


print()
account1 = BankAccount("Teejay", 0)
print(account1.name)
account1.deposit(3000)

print()
#
print(account1.name)
account1.deposit(5000)
#
#
print()
account1.withdraw(10000)
