class BankAccount:

    def __init__(self, bank_name, balance):
        self.bank_name = bank_name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f" deposit made is {amount} and new balance is {self.balance}"
        else:
            return "amount cannot be negative or 0"

    def withdraw(self, decrease_balance):
        self.balance -= decrease_balance
        if decrease_balance > 0:
            if self.balance != 0:
                if decrease_balance > self.balance:
                    return "insufficient balance"
                else:
                    return f" Account balance is {self.balance}"
            else:
                return "account is 0"

        else:
            return "withdrawal cannot be zero"


bank1 = BankAccount("teejay", 100)
print(bank1.deposit(37))
print(bank1.withdraw(20))
