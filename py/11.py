# ERROR HANDLING

# Error Handling:
""" · process of anticipating, catching, and managing errors 
that occur during program execution
"""

# Basic exception handling
try:
    number = int(input("Enter a number:"))
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("Invalid input! Please enter a number.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

#--------------------------------------------------

# Using else and finally
try:
    file = open("data.txt", "r")
except FileNotFoundError:
    print("File not found!")
else:
# Executes if no exception occurred
    content = file.read()
    print("File read successfully")
finally:
    # Always executes
    if 'file' in locals() and not file.closed:
        file.close()
    print("Cleanup completed")

#--------------------------------------------------

# raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(12)
except ValueError as e:
    print(f"Validation Error: {e}")

#--------------------------------------------------

# using else and finally

try:
    file = open("sample.txt", "r")
except FileNotFoundError as e:
    print(f"File not found: {e}")
else:
    content = file.read()
    print(f"File read successfully: {content}")
finally:
    if 'file' in locals() and not file.closed:
        file.close()
    print("File operation completed.")
