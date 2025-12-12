# #classes

# # a template for creating new objects

# class person:

#     species = "homo sapiens"  # class variable

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def introduce(self):
#         return f"hi, I am {self.name} and i am {self.age} years old"

#     def birthday(self):
#         self.age += 1
#         return f"happy birthday! {self.name} is now {self.age}."
    

# person1 = person("alice", 25)
# person2 = person("bob", 30)


# print(person1.introduce())
# print(person1.birthday())

# print(person.species)
# print(person1.species)


# bank account

class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.transactions_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions_history.append(f"deposited ${amount}")
            return f"deposited ${amount}. New balance: ${self.balance}"
        else:
            return "invalid deposit amount"
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transactions_history.append(f"withdrew ${amount}")
            return f"withdrew ${amount}. New balance: ${self.balance}"
        else:
            return "invalid withdrawal amount or insufficient funds"

    def get_balance(self):
        return f"current balance: ${self.balance}"
    
    def get_transactions_history(self):
        return self.transactions_history
    

account = BankAccount("123456789", "alice", 1000)
print(account.deposit(500))
print(account.withdraw(200))
print(account.get_balance())