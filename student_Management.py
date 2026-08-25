import csv
import os
FILE_NAME = "student.csv"
FIELDS = ["id", "name", "age", "course", "marks"]
def create_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
create_file()
print("Student CSV file created successfully.")
def add_student():
    student_id = input("Enter student ID: ")
    name = input("Enter student name: ")
    age = input("Enter student age: ")
    course = input("Enter student course: ")
    marks = input("Enter student marks: ")

    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "course": course,
        "marks": marks
    }

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDS)
        writer.writerow(student)

    print("Student added successfully!")

add_student()
def view_students():
    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        print("\nStudent Records")
        print("-" * 50)

        for student in reader:
            print(
                "ID:", student["id"],
                "| Name:", student["name"],
                "| Age:", student["age"],
                "| Course:", student["course"],
                "| Marks:", student["marks"]
            )
def search_student():
    search_id = input("Enter student ID to search: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)

        found = False

        for student in reader:
            if student["id"] == search_id:
                print("\nStudent Found")
                print("-" * 50)
                print("ID:", student["id"])
                print("Name:", student["name"])
                print("Age:", student["age"])
                print("Course:", student["course"])
                print("Marks:", student["marks"])

                found = True
                break

        if not found:
            print("Student not found!")

def update_student():
    student_id = input("Enter student ID to update: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    found = False

    for student in students:
        if student["id"] == student_id:
            print("Enter new details:")

            student["name"] = input("Enter new name: ")
            student["age"] = input("Enter new age: ")
            student["course"] = input("Enter new course: ")
            student["marks"] = input("Enter new marks: ")

            found = True
            break

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(students)

        print("Student updated successfully!")
    else:
        print("Student not found!")  
def delete_student():
    student_id = input("Enter student ID to delete: ")

    with open(FILE_NAME, "r", newline="") as file:
        reader = csv.DictReader(file)
        students = list(reader)

    found = False

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            found = True
            break

    if found:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(students)

        print("Student deleted successfully!")
    else:
        print("Student not found!")          

# CALL THE FUNCTION HERE
create_file()
add_student()
view_students()
search_student()
update_student()
delete_student()
create_file()

while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        search_student()

    elif choice == "4":
        update_student()

    elif choice == "5":
        delete_student()

    elif choice == "6":
        print("Thank you!") 
        break

    else:
        print("Invalid choice. Please try again.")
            