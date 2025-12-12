
def greet_person(name):
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

def add_numbers(a, b):
    return a + b

result_1 = add_numbers(5, 7)
result_2 = add_numbers(-3, 12)
print(f"Result 1: {result_1}")
print(f"Result 2: {result_2}")


def greet_with_title(name, title="Mr./Ms."):
    return(f"Hello, {title} {name}!")

print(greet_with_title("Charlie"))
print(greet_with_title("Diana", "Dr."))


# Example: WITH return vs WITHOUT return
print("\n--- WITH return ---")
def multiply_with_return(a, b):
    result = a * b
    return result  # sends value back

answer = multiply_with_return(4, 5)
print(f"Answer: {answer}")  # prints: Answer: 20


print("\n--- WITHOUT return ---")
def multiply_without_return(a, b):
    result = a * b
    print(f"Result is: {result}")  # prints inside function

answer2 = multiply_without_return(4, 5)
print(f"Answer stored: {answer2}")  # prints: Answer stored: None

# functions: args & kwargs

def flexible_function(*args, **kwargs):
    print("Positional arguments (args):", args)
    print("Keyword arguments (kwargs):", kwargs)

flexible_function(1, 2, 3, name="Alice", age=30)