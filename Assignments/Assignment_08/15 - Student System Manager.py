class Course:
    def __init__ (self, course_name, instructor, capacity):
        self.course_name = course_name
        self.instructor = instructor
        self.capacity = capacity
        self.students = []

class Student:
    def __init__ (self, name):
        self.name = name
        self.grades = {}

    def is_full(self, course):
        return len(course.students) < course.capacity
    
    def enroll(self, course):
        if not self.is_full(course):
            print(f"Unfortunately, {self.name} is unable to enroll because the {course.course_name} class is already at its maximum capacity.")
        else:
            course.students.append(self)            
            print(f"{self.name} has been enrolled in {course.course_name}.")  

    def add_grade(self, course_name, grade):
        self.grades[course_name] = grade
        
    def show_grades(self):
        for course, grade in self.grades.items():
            print(f"{self.name}'s grade in {course}: {grade}")

class School:
    def __init__(self):
        self.courses = []
        self.students = []

    def add_course(self, course):
        self.courses.append(course)        
    
    def add_student(self, student):
        self.students.append(student)

    def enroll_student_in_course(self, student, course):
        student.enroll(course)

    def save_grade(self, student, course, grade):
        student.add_grade(course.course_name, grade)

    def show_students_in_course(self, course):
        print(f"Students enrolled in {course.course_name}:")
        for student in course.students:
            print(student.name)

if __name__ == "__main__":

    school_1 = School()

    meth_course = Course("Math", "Mr. Jones", 2)
    computer_course = Course("Computer", "Mr. Wolf", 3)

    school_1.add_course(meth_course)
    school_1.add_course(computer_course)

    student_1 = Student("James Jones")
    student_2 = Student("Bob Smith")
    student_3 = Student("William Wolf")

    school_1.add_student(student_1)
    school_1.add_student(student_2)
    school_1.add_student(student_3)

    school_1.enroll_student_in_course(student_1, meth_course)
    school_1.enroll_student_in_course(student_2, meth_course)
    school_1.enroll_student_in_course(student_3, meth_course)

    school_1.show_students_in_course(meth_course)