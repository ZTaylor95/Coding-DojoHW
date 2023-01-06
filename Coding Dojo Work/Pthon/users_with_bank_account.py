class BankAccount:
    def __init__(self, balance=0,int_rate=0.05):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self,amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient funds: You have been charged $5 ")
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
            print("get yo paper up")
        return self


class User:
    def __init__(self,first_name,last_name,email,age,is_rewards_member,balance=0,int_rate=0.05):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = is_rewards_member
        self.gold_card_points = 0
        self.account = BankAccount(balance,int_rate)

    def display_info(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.age)
        print(self.is_rewards_member)
        print(self.gold_card_points)
        return self


    def enroll(self):
        if self.is_rewards_member is False:
            self.is_rewards_member = True
            self.gold_card_points = 200
        else: self.gold_card_points = 200
        print("You have already enrolled")
        return self

    def spend_points(self,amount):
        if self.gold_card_points < amount:
            self.gold_card_points = ("you are broke")
        else : self.gold_card_points = self.gold_card_points - amount
        return self

    def make_deposit(self,amount):
        self.account.deposit(amount)
        print('Your deposit was successful')
        return self

    def make_withdraw(self,amount):
        self.account.withdraw(amount)
        print('Your withdrawal was successful')
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self







jake_cat = User("Jake" , "Cat" , "jakekitty@gmail.com" , 20 , True, 300)
jonny_mane = User("Jonny" , "Mane" , "jmane12@gmail.com" , 87 ,0.3, False)
kanye_west = User("Kanye" , "West" , "kwest@gmail.com" , 100 ,0.3, False)

jake_cat.enroll().spend_points(50).display_info()
jonny_mane.enroll().spend_points(45).display_info()
kanye_west.spend_points(40).display_info()

jake_cat.account.get_interest()
jake_cat.account.display_account_info()

jake_cat.make_withdraw(50)




