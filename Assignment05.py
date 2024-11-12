# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
# Adam Savage,20241110,adapted the script to using JSON
# ------------------------------------------------------------------------------------------ #

import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
json_data: str = ''
file = None
menu_choice: str = ''
student_data: dict = {}
students: list = []

# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file with error catching for a missing file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)  # read the JSON into the list of dictionaries
    file.close()
except FileNotFoundError as e:  # this exception block will create an empty file if none exists
    print("No file exists. Creating an empty file...\n")
    file = open(FILE_NAME, "w")  # opening a file that doesn't exist in write mode creates it
    file.close()
    file = open(FILE_NAME, "r")
except Exception as e:
    print("-- Technical Error Message -- ")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        student_first_name = input("Enter the student's first name: ")
        try:
            if not student_first_name.isalpha():
                raise ValueError  # define the exception
        except ValueError:
            print("\n=== Please include only alphabetic characters in name. ===")
            continue  # if the user entered non-alphabetic characters, reload the menu
        student_last_name = input("Enter the student's last name: ")
        try:
            if not student_last_name.isalpha():
                raise ValueError  # define the exception
        except ValueError:
            print("\n=== Please include only alphabetic characters in name. ===")
            continue  # if the user entered non-alphabetic characters, reload the menu
        course_name = input("Please enter the name of the course: ")
        student_data = {"first_name":student_first_name,"last_name":student_last_name,"course":course_name}  # creates a dictionary of the input data
        students.append(student_data)  # appends the dictionary to the list of students
        print(f"You have added {student_first_name} {student_last_name} for {course_name}.")
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-" * 50)
        for student in students:
            print(f"Student {student.get('first_name')} {student.get('last_name')} is enrolled in {student.get('course')}")
        print("-" * 50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        file = open(FILE_NAME, "w")
        try:
            json.dump(students, file)
        except Exception as e:
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        else:
            for student in students:
                print(f"Student {student.get('first_name')} {student.get('last_name')} is enrolled in {student.get('course')}")
            print("Data Saved!")
        finally: file.close()  # whether exceptions exist or not, close the file
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
