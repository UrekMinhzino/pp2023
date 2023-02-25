class Students:
    def __init__(self, id: str, name: str, dob: int):
        self.id = id
        self.name = name
        self.dob = dob
        self.mark = {}

    #assert dob >= 0, f'dob must > 0'
    
    def __repr__(self):
        return f"Student(id='{self.id}', name='{self.name}', dob={self.dob}, marks={self.mark})"

class Courses:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"Course(id='{self.id}', name='{self.name}')"

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
        num_students = int(input('Enter the number of courses: '))
        for i in range(num_students):
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
            self.students[student_index].mark[course.id] = mark

    def show_marks(self):
        self.list_courses()
        course_index = int(input("Select a course: ")) - 1
        course_id = self.courses[course_index].id
        print(f'Mark for course {course_id}: ')
        for student in self.students:
            mark = student.mark.get(course_id, "-")
            print(f"{student}: {mark}")

    def show_student_marks_for_course(self):
        self.list_students()
        student_index = int(input("Select a student: ")) - 1
        student_id = self.students[student_index].id
        self.list_courses()
        course_index = int(input("Select a course: ")) - 1
        course_id = self.courses[course_index].id
        mark = self.students[student_index].mark.get(course_id, "-")
        print(f"{student_id}'s mark for {course_id}: {mark}")

    def run_please(self):
        self.input_students()
        self.input_courses()
        self.input_mark()
        self.show_marks()
        self.show_student_marks_for_course()

program = Program()
program.run_please()








    
