
# # LOOPS

# # for loop: known iteration
# # while loop: unknown iteration

# """
# Rule of Thumb:
# if you can count it use fir loop
# if you are waiting for a condition use while loop

# """


# # for loop

# for i in range(5):                   # 0,1,2,3,4
#     print(i)

# for i in range(1, 6):                # 1,2,3,4,5
#     print(i)

# for i in range(0, 10, 2):            # 0,2,4,6,8
#     print(i)


# # while loop

# count = 0
# while count < 5:
#     print(count)
#     count += 1


# # loop control statements:

# for i in range(10):
#     if i == 3:
#         continue     # skip iteration
#     if i == 7:
#         break        # exit loop
#     print(i)


# # nested loops

# for i in range(2):
#     for j in range(3):
#         print(f'i: {i}, j: {j}')


# # exercise

# """
# 1. create a multiplication table generator
# """
# # Simple approach - fixed number
# print("Multiplication Table for 5:")
# for i in range(1, 11):
#     result = 5 * i
#     print(f"5 x {i} = {result}")

# print("\n" + "="*30 + "\n")

# # User input approach
# number = int(input("enter a number for multiplication table: "))
# print(f"\nMultiplication Table for {number}:")
# for i in range(1, 11):
#     result = number * i
#     print(f"{number} x {i} = {result}")

# print("\n" + "="*30 + "\n")



"""
2. Write a program that finds all prime numbers up to a given 
number. (limit = 20)

"""

# Find all prime numbers up to 20

limit = 20

print(f"Prime numbers up to {limit}:")

# Check each number from 2 to limit
for num in range(2, limit + 1):
    is_prime = True
    
    # Check if num is divisible by any number from 2 to num-1
    for i in range(2, num):
        if num % i == 0:  # If divisible, not prime
            is_prime = False
            break
    
    # If still prime, print it
    if is_prime:
        print(num)
