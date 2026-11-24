
students = []


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


# Input data of 8 students
for i in range(8):
    print("\nEnter data for student", i + 1)

    name = input("Enter name: ")
    roll_no = input("Enter roll number: ")

    matric = int(input("Enter matric marks out of 1200: "))
    inter = int(input("Enter inter marks out of 1200: "))

    degree = input("Enter degree: ")
    university = input("Enter university: ")

    student = {
        "name": name,
        "roll_no": roll_no,
        "matric": matric,
        "inter": inter,
        "degree": degree,
        "university": university
    }

    students.append(student)


# Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Display all students")
    print("2. Find class topper")
    print("3. Check grades of all students")
    print("4. Check class average")
    print("5. Search student by roll number")
    print("6. Exit")

    choice = input("What do you want to check? Enter option: ")

    if choice == "1":
        for s in students:
            print("Name:", s["name"])
            print("Roll No:", s["roll_no"])
            print("Matric:", s["matric"], "/ 1200")
            print("Inter:", s["inter"], "/ 1200")
            print("Degree:", s["degree"])
            print("University:", s["university"])

    elif choice == "2":
        topper = max(
            students,
            key=lambda s: s["inter"] / 1200 * 100
        )

        percentage = topper["inter"] / 1200 * 100
        grade = calculate_grade(percentage)

        print("\n===== CLASS TOPPER =====")
        print("Name:", topper["name"])
        print("Roll No:", topper["roll_no"])
        print("Inter Marks:", topper["inter"], "/ 1200")
        print("Percentage:", round(percentage, 2), "%")
        print("Grade:", grade)
        print("Degree:", topper["degree"])
        print("University:", topper["university"])

    elif choice == "3":
        for s in students:
            percentage = s["inter"] / 1200 * 100
            grade = calculate_grade(percentage)

            print(s["name"],"| Percentage:", round(percentage, 2), "%","| Grade:", grade )

    elif choice == "4":
        total = 0

        for s in students:
            total += s["inter"] / 1200 * 100

        average = total / len(students)

        print("Class Average:", round(average, 2), "%")

    elif choice == "5":
        search_roll = input("Enter roll number to search: ")
        found = False

        for s in students:
            if s["roll_no"] == search_roll:
                print("\nName:", s["name"])
                print("Roll No:", s["roll_no"])
                print("Matric Marks:", s["matric"])
                print("Inter Marks:", s["inter"])
                print("Degree:", s["degree"])
                print("University:", s["university"])
                found = True
                break

        if not found:
            print("Student not found!")

    elif choice == "6":
        print("Program closed. Allah Hafiz!")
        break

    else:
        print("Invalid option! Please enter 1 to 6.")

