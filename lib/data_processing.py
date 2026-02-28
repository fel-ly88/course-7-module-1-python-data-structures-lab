# This module contains functions to process student data.

def format_student_data(student):
    """
    Format student data for display.
    The function should return a formatted string containing:
    - Student ID
    - Student Name
    - Major
    such as: "ID: 10 | Name: Louis Medina | Major: Computer Science"
    """
    return f"ID: {student[0]} | Name: {student[1]} | Major: {student[2]}"

def display_students(student_list):
    """
    Display all student records.
    Loop through the student_list and print each student using format_student_data().
    """
    for student in student_list:
        print(format_student_data(student))