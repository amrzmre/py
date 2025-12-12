
# # LISTS

# # list: a set of data within square brackets [...]

# fruits = ["apple", "banana", "orange"]
# numbers = [1, 2, 3, 4, 5]
# mixed = ["hello", 42, 3.14, True]
# empty_list = []

# # accessing elements
# print(fruits[0])      #"apple"
# print(fruits[-1])     #"orange"
# print(numbers[1:4])   #[2, 3, 4]
# print(numbers[:3])    #[1, 2, 3]
# print(numbers[2:])    #[3, 4, 5]


# # list operation: CRUD (Create, Read, Update, Delete) a list

# fruits = ["apple", "banana", "orange"]
# numbers = [1, 2, 3, 4, 5]
# mixed = ["hello", 42, 3.14, True]
# empty_list = []

# fruits.append("grape")          # Add to end
# fruits.insert(1, "kiwi")        # insert at index
# fruits.remove("banana")         # remove by value
# popped_fruit = fruits.pop()     # remove and return last 
# fruits.sort()                   # sort list
# fruits.reverse()                # reverse in place


# # list operations
# len(fruits)                # length
# "apple" in fruits           # check membership
# fruits + ["mango"]          # concatenation
# fruits * 2                  # repetition


# print(len(fruits))

#--------------------------------------------------------------------------------------------

#EXERCISE:

"""
1. Create a grocery list and perform various operations.

"""

# # Create a grocery list
# grocery_list = ["milk", "bread", "eggs", "butter"]

# print("Original list:")
# print(grocery_list)
# print()

# # Add items to the list
# grocery_list.append("cheese")  # Add to end
# print("After adding cheese:")
# print(grocery_list)
# print()

# grocery_list.insert(1, "apples")  # Add at position 1
# print("After inserting apples at position 1:")
# print(grocery_list)
# print()

# # Remove items
# grocery_list.remove("bread")  # Remove by value
# print("After removing bread:")
# print(grocery_list)
# print()

# last_item = grocery_list.pop()  # Remove last item
# print(f"Removed last item: {last_item}")
# print("List after pop:")
# print(grocery_list)
# print()

# # Check if item exists
# if "milk" in grocery_list:
#     print("✓ Milk is in the list")
# else:
#     print("✗ Milk is NOT in the list")
# print()

# # Count items
# print(f"Total items: {len(grocery_list)}")
# print()

# # Sort the list
# grocery_list.sort()
# print("Sorted list (A-Z):")
# print(grocery_list)
# print()

# # Reverse the list
# grocery_list.reverse()
# print("Reversed list:")
# print(grocery_list)
# print()

# # Access specific items
# print(f"First item: {grocery_list[0]}")
# print(f"Last item: {grocery_list[-1]}")
# print(f"First 3 items: {grocery_list[:3]}")


#-----------------------------------------------------------------------------------------

"""
2. Write a program that finds the largest and smallest number in
list.

"""

# Create a list of numbers
numbers = [45, 12, 78, 3, 56, 89, 23, 67, 8, 91]

print("List of numbers:")
print(numbers)
print()

# Method 1: Using built-in functions (easiest way)
largest = max(numbers)
smallest = min(numbers)

print("=== Method 1: Using max() and min() ===")
print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print()

# Method 2: Using a loop (manual way)
print("=== Method 2: Using a loop ===")

# Assume first number is largest and smallest
largest = numbers[0]
smallest = numbers[0]

# Check each number in the list
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print(f"Largest number: {largest}")
print(f"Smallest number: {smallest}")
print()

# Bonus: Show their positions in the list
largest_index = numbers.index(max(numbers))
smallest_index = numbers.index(min(numbers))

print("=== Bonus Info ===")
print(f"Largest number {max(numbers)} is at position {largest_index}")
print(f"Smallest number {min(numbers)} is at position {smallest_index}")