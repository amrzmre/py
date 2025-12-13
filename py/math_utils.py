# MODULE & LIBRARIES

""" 
Module:
  · A file containing code
    (functions, classes, variables,
    etc.) that can be imported
    and used in other Python
    programs.

Libraries:
    · A collection of modules and
    packages that provide
    specific functionality.
"""
#--------------------------------------

" Module: "
# 1. Create math_utils.py

def add(a, b):
    """ Add two numbers """
    return a + b

def multiply(a, b):
    """ Multiply two numbers """
    return a * b

def factorial(n):
    """Calculate factorial of n"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

PI = 3.14159

class Calculator:
    def _init_(self):
        self.history = []

    def calculate(self, operation, a, b):
        if operation == "add":
            result - add(a, b)
        elif operation == "multiply":
            result = multiply(a, b)
        else:
            result = None

        self.history. append(f"{operation}({a}, {b}) = {result}")
        return result

