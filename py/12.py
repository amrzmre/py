# #CLASSES AND OBJECT

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
    
# # -------------------------------------------

# # Objects:
# # instance of a classes

# # Creating objects (instances)
# person1 = Person("Alice", 25)  
# person2 = Person("Bob", 30)

# # Accessing attributes
# print(person1.name)      # "Alice"
# print(person1.age)       # 25


# # Calling methods
# print(person1.introduce())
# print(person1.have_birthday())

# # Class attributes
# print(Person.species)  # "Homo sapiens"
# print(person1.species) # "Homo sapiens"


# ---------------------------------------------------------

# bank account

# class BankAccount:
#     def __init__(self, account_number, owner, balance=0):
#         self.account_number = account_number
#         self.owner = owner
#         self.balance = balance
#         self.transactions_history = []

#     def deposit(self, amount):
#         if amount > 0:
#             self.balance += amount
#             self.transactions_history.append(f"deposited ${amount}")
#             return f"deposited ${amount}. New balance: ${self.balance}"
#         else:
#             return "invalid deposit amount"
        
#     def withdraw(self, amount):
#         if amount > 0 and amount <= self.balance:
#             self.balance -= amount
#             self.transactions_history.append(f"withdrew ${amount}")
#             return f"withdrew ${amount}. New balance: ${self.balance}"
#         else:
#             return "invalid withdrawal amount or insufficient funds"

#     def get_balance(self):
#         return f"current balance: ${self.balance}"
    
#     def get_transactions_history(self):
#         return self.transactions_history
    
# # using the BankAccount class
# account = BankAccount("123456789", "alice", 1000)
# print(account.deposit(500))
# print(account.withdraw(200))
# print(account.get_balance())

#-------------------------------------------------

" EXCERCISE: "

"""
1. Create a simple game character class with health, attack and
heal methods.
"""

# Create a GameCharacter class
class GameCharacter:
    # Constructor - runs when creating a new character
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power
    
    # Method to attack another character
    def attack(self, target):
        print(f"{self.name} attacks {target.name}!")
        target.health -= self.attack_power
        print(f"{target.name} takes {self.attack_power} damage!")
        print(f"{target.name}'s health: {target.health}")
    
    # Method to heal the character
    def heal(self, amount):
        self.health += amount
        print(f"{self.name} heals for {amount} HP!")
        print(f"{self.name}'s health: {self.health}")
    
    # Method to display character status
    def status(self):
        print(f"--- {self.name}'s Status ---")
        print(f"Health: {self.health}")
        print(f"Attack Power: {self.attack_power}")
        print()


# Create two characters (objects)
print("=== Creating Characters ===")
warrior = GameCharacter("Warrior", 100, 25)
mage = GameCharacter("Mage", 80, 30)
print()

# Show initial status
warrior.status()
mage.status()

# Battle sequence
print("=== Battle Begins! ===")
print()

# Warrior attacks Mage
warrior.attack(mage)
print()

# Mage attacks Warrior
mage.attack(warrior)
print()

# Warrior attacks again
warrior.attack(mage)
print()

# Mage heals
mage.heal(20)
print()

# Final status
print("=== Final Status ===")
warrior.status()
mage.status()