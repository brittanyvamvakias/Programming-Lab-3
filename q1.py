# File: q1.py
# Author: Brittany Vamvakias
# Date: 02/11/2020
# Section: 501
# E-mail: brittvam@tamu.edu
# Description: This code evaluates an input for a subject course code for validity, asks for a different input if invalid, and returns information about the department if valid. It then asks for the course name and the three exam grades. It takes those exam grades and their respective weights to compute a class average and a letter grade.

valid = True
while valid == True:
    print("******************************* Section A ********************************")
    subject_code = input("Enter the subject's code that you are looking for: ")
    subject_code = subject_code.upper()

    if subject_code[0:4] == "CSCE":
        dept = "Computer Science"

    elif subject_code[0:4] == "MEEN":
        dept = "Mechanical Engineering"

    elif subject_code[0:4] == "VIZA":
        dept = "Visualization"

    elif subject_code[0:4] == "MATH":
        dept = "Mathematics"

    elif subject_code[0:4] == "STAT":
        dept = "Statistics"

    else:
        print("Invalid input. Start over.")
        continue

    print(f"{subject_code} is a course from the department of {dept}.")
    valid = False

print("******************************* Section B ********************************")


course_name = input("What is the course name? ")

course = True
while course == True:
    grades = input(f"Enter 3 grades for 3 subjects from the department of {subject_dept}: ").split()
    grade1 = int(grades[0])
    grade2 = int(grades[1])
    grade3 = int(grades[2])

    if grade1 > 100 or grade2 > 100 or grade3 > 100:
        print("Invalide grade/s, try again.")
        continue
    else:
        average = grade1 * .25 + grade2 * .35 + grade3 * .40
        print(f"Total Score: {average}")
        if average >= 90:
            print("Final Grade: A")
        elif average >= 80:
            print("Final Grade: B")
        elif average >= 70:
            print("Final Grade: C")
        elif average >= 60:
            print("Final Grade: D")
        else:
            print("Final Grade: F")
    print("*************************************************************************")
    course = False







