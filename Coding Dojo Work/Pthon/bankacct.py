class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self,amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient funds: Charging a $5 fee")
            self.balance = self.balance - 5
        else: 
            self.balance = self.balance - amount
        return self


    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self

    def get_interest(self):
        if self.balance > 0:
            total_with_int = self.balance * self.int_rate
            self.balance = self.balance + total_with_int
        else :  
            print("you have no monies")
        return self

rick_owens = BankAccount(0.07)
carti_vamp = BankAccount(0.1,300)


rick_owens.deposit(50).deposit(50).deposit(50).withdraw(100).get_interest().display_account_info()

carti_vamp.deposit(90).withdraw(22).withdraw(15).withdraw(30).deposit(500).get_interest().display_account_info()