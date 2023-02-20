def input_students():
    students = []
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        id = input("Enter student id: ")
        name = input("Enter student name: ")
        dob = input("Enter student date of birth: ")
        student = {"id": id, "name": name, "dob": dob, "marks": {}}
        students.append(student)
    return students

def input_courses():
    courses = []
    num_courses = int(input("Enter number of courses: "))
    for i in range(num_courses):
        id = input("Enter course id: ")
        name = input("Enter course name: ")
        course = {"id": id, "name": name}
        courses.append(course)
    return courses

def input_marks(students, courses):
    for course in courses:
        list_students(students)
        student_index = int(input("Select student: ")) - 1
        student_id = students[student_index]["id"]
        mark = input(f"Enter {student_id}'s mark for {course['id']}: ")
        students[student_index]["marks"][course['id']] = mark

def list_courses(courses):
    print("Courses:")
    for i, course in enumerate(courses):
        print(f"{i+1}. {course['id']}: {course['name']}")

def list_students(students):
    print("Students:")
    for i, student in enumerate(students):
        print(f"{i+1}. {student['id']}: {student['name']}")

def show_marks(students, courses):
    list_courses(courses)
    course_index = int(input("Select a course: ")) - 1
    course_id = courses[course_index]["id"]
    print(f"Marks for course {course_id}:")
    for student in students:
        mark = student["marks"].get(course_id, "-")
        print(f"{student['id']}: {mark}")

def show_student_marks_for_course(students, courses):
    list_students(students)
    student_index = int(input("Select a student: ")) - 1
    student_id = students[student_index]["id"]
    list_courses(courses)
    course_index = int(input("Select a course: ")) - 1
    course_id = courses[course_index]["id"]
    mark = students[student_index]["marks"].get(course_id, "-")
    print(f"{student_id}'s mark for {course_id}: {mark}")

students = input_students()
courses = input_courses()

input_marks(students, courses)
show_marks(students, courses)
show_student_marks_for_course(students, courses)
