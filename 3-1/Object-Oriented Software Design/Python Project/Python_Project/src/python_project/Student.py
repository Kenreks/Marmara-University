from Transcript import Transcript
from Grade import Grade


class Student:
    # Computed attributes may be declared as properties in methods
    # Semester, Instructor (nonprimitive types might be declared as properties)

    def __init__(self, student_id, name, surname, semester, advisor=None):
        # We can convert all course lists(Active, Past, Failed)
        # To map so that we can hold grades or keep going with 1 grade map as in JAVA
        self.name = name
        self.surname = surname
        self.student_id = student_id
        self.advisor = advisor
        self.active_courses = list()
        self.course_basket = list()
        self.past_courses = list()
        self.non_taken_courses = list()
        self.failed_courses = list()
        self.semester = semester
        self.gpa = 0
        self.cgpa = 0
        self.completed_credit = 0
        self.grade_map = dict()
        self.cumulative_credit = 0
        self.active_credit = 0
        self.cumulative_grade = 0
        self.active_grade = 0
        self.transcript = Transcript(self)

    def next_semester(self, semester):

        self.create_grades()
        self.calculate_gpa()
        self.calculate_cgpa()
        self.transcript.add_gpa(self.gpa, self.active_credit, self.cgpa, self.cumulative_credit)
        self.active_grade = 0
        self.active_credit = 0
        self.semester = semester
        self.transcript.create_semester()
        for course in self.active_courses:
            course.students.remove(self)
        self.active_courses.clear()

    def create_grades(self):
        for course in self.active_courses:
            grade = Grade()
            self.grade_map[course] = grade
            if grade.letter_grade == "FF":
                self.failed_courses.append(course)
            else:
                self.completed_credit += course.credit
                self.past_courses.append(course)
            self.active_grade += course.credit * grade.grade
            self.transcript.add_course(course.course_id, grade.letter_grade)
        self.cumulative_grade += self.active_grade

    def calculate_gpa(self):
        self.gpa = self.active_grade / self.active_credit

    def calculate_cgpa(self):
        self.cgpa = self.cumulative_grade / self.cumulative_credit

    def basket_to_active_course(self):
        """create grade
        We can assign next semester here but it is not logical
        clear basket"""
        self.active_courses.extend(self.course_basket)
        for course in self.course_basket:

            if course in self.failed_courses:
                self.cumulative_credit -= course.credit
                self.failed_courses.remove(course)
            self.active_credit += course.credit
            self.cumulative_credit += course.credit
            course.students.append(self)
        self.course_basket.clear()

    def add_error(self, error, course):
        self.non_taken_courses.append(course)
        self.transcript.add_error(error)

    def add_course_basket(self, course):
        self.course_basket.append(course)

    def remove_from_basket(self, will_be_removed):
        self.course_basket = list(set(self.course_basket) - set(will_be_removed))
