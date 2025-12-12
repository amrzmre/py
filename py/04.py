
# #  CONDITIONAL STATEMENTS

# # if-else: 2 conditions
# # if-elif-else: more than 2 conditions

# age = 18

# if age >= 18:
#     print("you are an adult.")
# else:
#     print("you are a minor.")

# score = 85 

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F" 

# print(f"your grade is: {grade}")


# # and: both conditions must be true
# # or: at least one condition must be true

# user_age = 12
# has_license = True

# if user_age >= 18 and has_license:
#     print("you can drive.")
# else:
#     print("you cannot drive.")


# day = "sunday"

# if day == "saturday" or day == "sunday":
#     print("it's the weekend!")
# else:
#     print("it's a weekday.")


# # nested conditionals: conditional within conditional

# weather = "sunny"
# temperature = 86

# if weather == "sunny":
#     if temperature > 70:
#         print("it's sunny and warm.")
#     else:
#         print("it's sunny but cool.")



# # exercises:

"""
1.write a program that catergorizes BMI (Body Mass Index)
into underweigh(<18.5), normal weight(24.9), overweight(<29.9),
obersity(<30.0).
formula = kg/m^2

"""

weight = float(input("enter your weight in kg: "))
height = float(input("enter your height in meters: "))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print(f'BMI: {bmi:.2f} - Underweight')
elif bmi < 24.9:
    print(f'BMI: {bmi:.2f} - Normal weight')
elif bmi < 29.9:
    print(f'BMI: {bmi:.2f} - Overweight')
else:
    print(f'BMI: {bmi:.2f} - Obesity')