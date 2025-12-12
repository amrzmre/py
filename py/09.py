# DICTIONARIES

# Dictionaries:
# · Key-value data structure
# · Key need to be unique
# · Value can be duplicated


student = {
"name": "Alice",
"age": 20,
"grade": "A",
"courses": ["Math", "Science", "English"]
}

# Accessing and modifying
print(student["name"])                    # "Alice"
print(student.get("age"))                 # 20
student["age"] = 21                       # Modify value
student["email"] = "alice@email.com"      # Add new key-value

#--------------------------------------------

" Dictionaries Method: "

keys = student.keys ()      # Get all keys
values = student.values()   # Get all values
items = student.items()     # Get key-value pairs

print(keys)
print(values)
print(items)

#--------------------------------------------

" Iterating Dictionaries: "

# Iterating through dictionaries
for key in student:
    print(f"{key}: {student[key]}")

for key, value in student.items():
    print(f"{key}: {value}")

#--------------------------------------------

" Nested Dictionaries: "

# Nested dictionaries
company = {
    "employees": {
        "john": {"age": 30, "department": "IT"},
        "jane": {"age": 25, "department": "HR"}
    },
    "departments": ["IT", "HR", "Finance"]
}

print(company["employees"].items())
print(company["departments"])

#--------------------------------------------

" Exercises: "

"""
1. Create a dictionary called student_records with the following information:
"student_001": name is "John", age is 19, major is "Computer Science", grades are [85, 92, 78]
"student_002": name is "Sarah", age is 20, major is "Biology", grades are [90, 88, 95]

"""

# Create student records dictionary
student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}

# Display all student records
print("=== All Student Records ===")
for student_id, info in student_records.items():
    print(f"\nStudent ID: {student_id}")
    print(f"Name: {info['name']}")
    print(f"Age: {info['age']}")
    print(f"Major: {info['major']}")
    print(f"Grades: {info['grades']}")
print()

# Access specific student information
print("=== John's Information ===")
john = student_records["student_001"]
print(f"Name: {john['name']}")
print(f"Major: {john['major']}")
print()

# Calculate average grade for each student
print("=== Average Grades ===")
for student_id, info in student_records.items():
    grades = info['grades']
    average = sum(grades) / len(grades)
    print(f"{info['name']}: {average:.2f}")
print()

# Add a new student
student_records["student_003"] = {
    "name": "Mike",
    "age": 21,
    "major": "Mathematics",
    "grades": [88, 91, 87]
}

print("=== After Adding Mike ===")
print(f"Total students: {len(student_records)}")
print(f"New student: {student_records['student_003']['name']}")
print()

# Update John's age
student_records["student_001"]["age"] = 20
print("=== After Updating John's Age ===")
print(f"John's new age: {student_records['student_001']['age']}")
print()

# Find student with highest average grade
print("=== Highest Average Grade ===")
highest_avg = 0
top_student = ""

for student_id, info in student_records.items():
    grades = info['grades']
    average = sum(grades) / len(grades)
    if average > highest_avg:
        highest_avg = average
        top_student = info['name']

print(f"{top_student} has the highest average: {highest_avg:.2f}")
print()

# List all majors
print("=== All Majors ===")
for student_id, info in student_records.items():
    print(f"{info['name']}: {info['major']}")



"""
2. Add a new student "student_003" with name "Mike", age 18, major "Math", grades [82,
79, 91]

"""
# Create student records dictionary
student_records = {
    "student_001": {
        "name": "John",
        "age": 19,
        "major": "Computer Science",
        "grades": [85, 92, 78]
    },
    "student_002": {
        "name": "Sarah",
        "age": 20,
        "major": "Biology",
        "grades": [90, 88, 95]
    }
}

print("Before adding Mike:")
print(f"Total students: {len(student_records)}")
print()

# Add new student Mike
student_records["student_003"] = {
    "name": "Mike",
    "age": 18,
    "major": "Math",
    "grades": [82, 79, 91]
}

print("After adding Mike:")
print(f"Total students: {len(student_records)}")
print()

# Display Mike's information
print("Mike's information:")
mike = student_records["student_003"]
print(f"Name: {mike['name']}")
print(f"Age: {mike['age']}")
print(f"Major: {mike['major']}")
print(f"Grades: {mike['grades']}")
print()

# Display all students
print("All students:")
for student_id, info in student_records.items():
    print(f"{student_id}: {info['name']} - {info['major']}")


"""
3. Update John's age to 20

"""

# Update John's age to 20
print("Before update:")
print(f"John's age: {student_records['student_001']['age']}")

student_records["student_001"]["age"] = 20

print("\nAfter update:")
print(f"John's age: {student_records['student_001']['age']}")


"""
4. Loop through the dictionary and print each student's information in this format:
"Student ID: [id], Name: [name], Major: [major]"

"""

# Loop through and print each student's information
print("=== Student Information ===")
for student_id, info in student_records.items():
    print(f"Student ID: {student_id}, Name: {info['name']}, Major: {info['major']}")