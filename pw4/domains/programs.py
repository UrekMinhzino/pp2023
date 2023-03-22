from .students import Students
from .courses import Courses

class Program:
    def __init__(self):
        self.students = []
        self.courses = []

    def input_students(self):
        num_students = int(input('Enter the number of students: '))
        for i in range(num_students):
            id = input('Enter student id: ')
            name = input('Enter student name: ')
            dob = input('Enter student date of birth: ')
            student = Students(id, name, dob)
            self.students.append(student)
            
    def input_courses(self):
        num_courses = int(input('Enter the number of courses: '))
        for i in range(num_courses):
            id = input('Enter course id: ')
            name = input('Enter course name: ')
            course = Courses(id, name)
            self.courses.append(course)

    def list_students(self):
        print("Student: ")
        for i, student in enumerate(self.students):
            print(f"{i+1}. {student}")

    def list_courses(self):
        print("Course: ")
        for i, course in enumerate(self.courses):
            print(f"{i+1}. {course}")

    def input_mark(self):
        for course in self.courses:
            self.list_students()
            student_index = int(input("Select student: ")) - 1
            student_id = self.students[student_index].id
            mark = input(f"Enter {student_id}'s mark for {course.id}: ")
            credit = input(f"Enter {course.id}'s credit for {student_id}: ")
            self.students[student_index].marks[course.id] = float(mark)
            self.students[student_index].credits[course.id] = float(credit)


    def show_marks(self):
        self.list_courses()
        course_index = int(input("Select a course: ")) - 1
        course_id = self.courses[course_index].id
        print(f'Mark for course {course_id}: ')
        for student in self.students:
            mark = student.marks.get(course_id, "-")
            print(f"{student}: {mark}")

    def show_student_marks_for_course(self):
        self.list_students()
        student_index = int(input("Select a student: ")) - 1
        student_id = self.students[student_index].id
        self.list_courses()
        course_index = int(input("Select a course: ")) - 1
        course_id = self.courses[course_index].id
        mark = self.students[student_index].marks.get(course_id, "-")
        print(f"{student_id}'s mark for {course_id}: {mark}")
    
    def calculate_gpa(self):
        for student in self.students:
            total_credits = 0
            total_weighted_marks = 0
            for course in self.courses:
                mark = student.marks.get(course.id, "-")
                if mark != "-":
                    credit = float(student.credits.get(course.id))
                    total_credits += credit
                    total_weighted_marks += float(mark) * credit
            if total_credits != 0:
                gpa = round(total_weighted_marks / total_credits, 1)
                student.gpa = gpa

    def sort_students_by_gpa(self):
        self.students.sort(key=lambda student: student.gpa, reverse=True)
        for student in self.students:
            print(student)

    def run_please(self):
        self.input_students()
        self.input_courses()
        self.input_mark()
        self.show_marks()
        self.show_student_marks_for_course()
        self.calculate_gpa()
        self.sort_students_by_gpa()

program = Program()
program.run_please()