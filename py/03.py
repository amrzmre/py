
# # input/output validation

# name = input("enter your name: ")
# height = float(input("enter your height in cm: "))

# # input validation
# while True:
#     try:
#         age = int(input("enter your age: "))
#         if age > 0:
#             break
#         else:
#             print("please enter a positive integer for age.")
#     except ValueError:
#         print("Age must be positive")

# # output validation
# print(f"hello, {name}!")
# print(f"you are {age} years old and {height} cm tall.")

# # excercises:

# """ 
# 1. create a simple calculator that takes two numbers
#    and an operation from user
# """

# num1 = int(input("enter first number: "))
# num2 = int(input("enter second number: "))
# operation = input("enter operation (+, -, *, /): ")

# while True:
#     try:
#         if operation == "+":
#             result = num1 + num2
#         elif operation == "-":
#             result = num1 - num2
#         elif operation == "*":
#             result = num1 * num2
#         elif operation == "/":
#             result = num1 / num2
#         else:
#             print("invalid operation. please enter one of +, -, *, /.")
#             operation = input("enter operation (+, -, *, /): ")
#             continue
#         break
#     except ZeroDivisionError:
#         print("error: division by zero is not allowed.")
#         num2 = int(input("enter a non-zero second number: "))

# print(f"result: {num1} {operation} {num2} = {result}")

# improvement of the calculator

try:
    num1 = float(input("enter first number: "))
    num2 = float(input("enter second number: "))
except ValueError:
    print("error: please enter valid numbers.")
    exit()


operation = input("enter operation (+, -, *, /): ")

while True:
    try:
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            result = num1 / num2
        else:
            print("invalid operation. please enter one of +, -, *, /.")
            operation = input("enter operation (+, -, *, /): ")
            continue
        break
    except ZeroDivisionError:
        print("error: division by zero is not allowed.")
        num2 = float(input("enter a non-zero second number: "))
        continue

print(f"result: {num1} {operation} {num2} = {result}")
  
  
