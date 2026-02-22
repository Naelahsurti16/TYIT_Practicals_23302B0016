students = []

def add_student():
    name = input("Enter student name: ")
    marks = input("Enter marks: ")

    students.append((name, marks))
    print("Student added successfully!\n")

def view_students():
    if len(students) == 0:
        print("No records found\n")
    else:
        print("\n--- Student Records ---")
        for s in students:
            print("Name:", s[0], "| Marks:", s[1])

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_students()
    elif choice == "3":
        break
    else:
        print("Invalid choice")
