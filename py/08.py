# SETS

# Sets:
# · A set of data within curly bracket { ... }
# . Unordered collection of elements

#-----------------------------------------

" Sets operations "

fruits = {"apple", "banana", "orange"}
numbers = {1, 2, 3, 4, 5}

# Set operations
fruits.add("grape")         # Add element
fruits.remove("banana")     # Remove element
fruits.discard("kiwi")      # Remove if exists (no error)

print(fruits)               

#-----------------------------------------


" Sets mathematic operations: "

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

print(set1.union(set2))             # {1, 2, 3, 4, 5, 6}
print(set1.intersection(set2))      # {3, 4}
print(set1.difference(set2))        # {1, 2}

#------------------------------------------

"""
Exercise:
1. Create a system that stores student grades as tuples (name, subject, grade)
and uses sets to find unique subjects and students.

grades = [
("Alice", "Math", 85),
("Bob", "Science", 92),
("Alice", "Science", 78),
("Charlie", "Math", 90),
("Bob", "Math", 88),
("Alice", "English", 95)
]

"""

# Student grades stored as tuples (name, subject, grade)
grades = [
    ("Alice", "Math", 85),
    ("Bob", "Science", 92),
    ("Alice", "Science", 78),
    ("Charlie", "Math", 90),
    ("Bob", "Math", 88),
    ("Alice", "English", 95)
]

print("All grades:")
for grade in grades:
    name, subject, score = grade
    print(f"{name} - {subject}: {score}")
print()

# Find unique students using a set
students = set()
for grade in grades:
    name = grade[0]  # First item in tuple is name
    students.add(name)

print("=== Unique Students ===")
print(students)
print(f"Total students: {len(students)}")
print()

# Find unique subjects using a set
subjects = set()
for grade in grades:
    subject = grade[1]  # Second item in tuple is subject
    subjects.add(subject)

print("=== Unique Subjects ===")
print(subjects)
print(f"Total subjects: {len(subjects)}")
print()

# Find all grades for a specific student
print("=== Alice's Grades ===")
for grade in grades:
    name, subject, score = grade
    if name == "Alice":
        print(f"{subject}: {score}")
print()

# Find all students who took Math
print("=== Students in Math ===")
math_students = set()
for grade in grades:
    name, subject, score = grade
    if subject == "Math":
        math_students.add(name)
print(math_students)
print()

# Calculate average grade for each student
print("=== Average Grades ===")
for student in students:
    total = 0
    count = 0
    for grade in grades:
        name, subject, score = grade
        if name == student:
            total += score
            count += 1
    average = total / count
    print(f"{student}: {average:.2f}")
print()

# Find highest grade
highest_grade = 0
top_student = ""
top_subject = ""

for grade in grades:
    name, subject, score = grade
    if score > highest_grade:
        highest_grade = score
        top_student = name
        top_subject = subject

print("=== Highest Grade ===")
print(f"{top_student} scored {highest_grade} in {top_subject}")