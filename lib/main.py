# main.py
from student_data import students
from data_processing import display_students, format_student_data
from filters import filter_students_by_major
from set_operations import unique_majors
from data_generator import student_generator

# Display all students
print("All Students:")
display_students(students)
print()

# Filter students by major
math_students = filter_students_by_major(students, "Mathematics")
print("Mathematics Students:")
display_students(math_students)
print()

# Unique majors
print("Unique Majors:", unique_majors(students))
print()

# Lazy generator for a major
print("Mathematics Students (Generator):")
for student in student_generator(students, "Mathematics"):
    print(format_student_data(student))