################ Function Definitions ################

# Shows the user what options they have
def displayMenu():
    print("1. Add a Student")
    print("2. Remove a Student")
    print("3. Add Quiz Grade for Student")
    print("4. List a Student's Quiz Grades")
    print("5. Get Student's Letter Grade")
    print("6. Quit")

# Prompts the user to enter a numeric grade
# This function works and ensures the user entered a valid float for the grade
def getNumberGradeFromUser():
    val = None

    while val is None:
        try:
            test = float(input("Enter a Grade: "))
            val = test
        except ValueError:
            val = None

    return val

# Function to add a student and their grades to a dictionary
def addStudent(student_dict):
    student_name = input("Enter the student's name: ")
    student_grades = []

    while True:
        grade = getNumberGradeFromUser()
        if grade >= 0 and grade <= 100:
            student_grades.append(grade)
            another_grade = input("Add another grade? (y/n): ")
            if another_grade.lower() != 'y':
                break
        else:
            print("Invalid grade. Please enter a valid numeric grade between 0 and 100.")

    student_dict[student_name] = student_grades
    print(f"{student_name} added with grades: {student_grades}")

# Function to remove a student from the dictionary
def removeStudent(student_dict):
    student_name = input("Enter the name of the student to remove: ")
    if student_name in student_dict:
        del student_dict[student_name]
        print(f"{student_name} has been removed.")
    else:
        print(f"Student {student_name} not found.")

# Function to add a quiz grade for a student
def addQuizGrade(student_dict):
    student_name = input("Enter the name of the student: ")
    if student_name in student_dict:
        grade = getNumberGradeFromUser()
        if grade >= 0 and grade <= 100:
            student_dict[student_name].append(grade)
            print(f"Added quiz grade {grade} for {student_name}.")
        else:
            print("Invalid grade. Please enter a valid numeric grade between 0 and 100.")
    else:
        print(f"Student {student_name} not found.")

# Function to list a student's quiz grades
def listStudentGrades(student_dict):
    student_name = input("Enter the name of the student: ")
    if student_name in student_dict:
        grades = student_dict[student_name]
        print(f"Quiz grades for {student_name}: {grades}")
    else:
        print(f"Student {student_name} not found.")

# Function to get a student's letter grade
def getLetterGrade(student_dict):
    student_name = input("Enter the name of the student: ")
    if student_name in student_dict:
        grades = student_dict[student_name]
        average_grade = sum(grades) / len(grades)
        if average_grade >= 90:
            letter_grade = 'A'
        elif average_grade >= 80:
            letter_grade = 'B'
        elif average_grade >= 70:
            letter_grade = 'C'
        elif average_grade >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'F'
        print(f"Letter grade for {student_name}: {letter_grade}")
    else:
        print(f"Student {student_name} not found.")

################ Main Program ################

student_dict = {}  # Create an empty dictionary to store student information

# Application Loop
while True:
    print()
    displayMenu()
    choice = input("Enter your choice (1-6): ")

    if choice == '1':
        addStudent(student_dict)
    elif choice == '2':
        removeStudent(student_dict)
    elif choice == '3':
        addQuizGrade(student_dict)
    elif choice == '4':
        listStudentGrades(student_dict)
    elif choice == '5':
        getLetterGrade(student_dict)
    elif choice == '6':
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please enter a valid option (1-6).")