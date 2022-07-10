import random


class Registrator:
    """ Registrator object registers a student to current semester. Registration process happens in three steps:
        Try to register student to failed courses
        Try to register student to non taken courses (Courses that advisor didn't allow student to take)
        Try to register student to current semester courses
            If an elective course must be taken, select a random elective course and try to register
        After selecting courses send course basket to advisors approval
            (Courses those are not approved by advisor will be deleted from course basket)
        Add course basket to student's active course list """

    def __init__(self, courses, semesters):
        self.courses = courses
        self.semesters = semesters

    def select_course(self, course_list, student):
        """ Selects course from given list and checks if student can take that course """
        list_copy = course_list.copy()

        for course in list_copy:
            if course.course_type != 'Must':

                while True:
                    selected_course = random.choice(self.courses[course.course_type])
                    if selected_course.approve_course(student):
                        break
                try:
                    student.non_taken_courses.remove(selected_course)
                except Exception:
                    pass
                student.add_course_basket(selected_course)
            elif course.approve_course(student):

                try:
                    student.non_taken_courses.remove(course)
                except Exception:
                    pass
                student.add_course_basket(course)

    def start_registration(self, student):
        for course in student.failed_courses:
            if course.approve_course(student):
                student.add_course_basket(course)

        self.select_course(student.non_taken_courses, student)
        self.select_course(self.semesters[student.semester.semester_id].course_list, student)
        student.advisor.approve_student_basket(student)
        student.basket_to_active_course()