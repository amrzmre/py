# error handling

# raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    elif age > 120:
        raise ValueError("Age seems unrealistic")
    return True

try:
    validate_age(145)
except ValueError as e:
    print(f"Validation Error: {e}")



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
