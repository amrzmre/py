# FUNCTIONS

# Functions:
# · Reusable block of code that do specific task

#------------------------------------------------

# Functions with parameters
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")

# Functions with return values
def add_numbers(a, b):
    return a + b

result = add_numbers(5, 3)
print(result) # 8

# Default parameters
def greet_with_title(name, title="Mr."):
    return f"Hello, {title} {name}!"

print(greet_with_title("Smith"))             # "Hello, Mr. Smith!"
print(greet_with_title("Johnson", "Dr."))    # "Hello, Dr. Johnson!"


#------------------------------------------------

" args : "
# · access by index: args[0]
# · unpacking: func(*list)

# *args - variable number of arguments
def sum_all(*args):
    return sum(args)

print(sum_all(1, 2, 3, 4,5))  # 15

#------------------------------------------------

" kwargs : "
# · access by key: kwargs['key']
# · unpacking: func( ** dict)

# ** kwargs - keyword arguments
def print_info( ** kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")

#------------------------------------------------

" args & kwargs : "

# Combining *args and ** kwargs
def flexible_function(*args, ** kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

flexible_function(1, 2, 3, name="Alice", age=25)

#--------------------------------------------------

" lambda : "
# · anonymous function
# · small function

# Lambda functions (anonymous functions)
square = lambda x: x ** 2
print(square(5)) # 25

add = lambda x, y: x + y
print(add(3, 4)) # 7

#--------------------------------------------------

" EXCERCISE "

"""
1. Write a function that checks if a number is prime.

"""

# Function to check if a number is prime
def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False
    
    # Check if number is divisible by any number from 2 to number-1
    for i in range(2, number):
        if number % i == 0:  # If divisible, not prime
            return False
    
    # If no divisors found, it's prime
    return True


# Test the function with different numbers
print("=== Testing Prime Numbers ===")

test_numbers = [1, 2, 3, 4, 5, 10, 13, 17, 20, 23, 29, 30]

for num in test_numbers:
    if is_prime(num):
        print(f"{num} is PRIME")
    else:
        print(f"{num} is NOT prime")

print()

# # Ask user for input (optional)
# user_number = int(input("Enter a number to check if it's prime: "))

# if is_prime(user_number):
#     print(f"{user_number} is a PRIME number!")
# else:
#     print(f"{user_number} is NOT a prime number.")


#---------------------------------------------------------

"""
2. Build a temperature converter function. (Celsius to Fahrenheit)
"""

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit


# Test the function with different temperatures
print("=== Celsius to Fahrenheit Converter ===")
print()

# Test various temperatures
test_temps = [0, 10, 20, 25, 30, 37, 100]

for temp in test_temps:
    result = celsius_to_fahrenheit(temp)
    print(f"{temp}°C = {result}°F")

print()

# # User input
# celsius = float(input("Enter temperature in Celsius: "))
# fahrenheit = celsius_to_fahrenheit(celsius)
# print(f"{celsius}°C is equal to {fahrenheit}°F")