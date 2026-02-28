# This module contains functions to lazily generate and format student data.

def student_generator(student_list, major):
    """
    Lazily generate students filtered by major.
    Returns a generator expression.
    """
    return (student for student in student_list if student[2] == major)

def format_student_data(student):
    """
    Format student data for display.
    Expects student as a tuple: (id, name, major)
    Returns a string like:
    "ID: 101 | Name: Alice Johnson | Major: Computer Science"
    """
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"

def display_students(student_list):
    """
    Display all student records.
    Loops through the student_list and prints each student using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))