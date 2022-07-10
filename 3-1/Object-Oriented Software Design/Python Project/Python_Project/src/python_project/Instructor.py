from Error import Error


class Instructor:

    def __init__(self, id, name, surname):
        self.id = id
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname

    def check_two_technical(self, student):
        """
           course variable gets in to course_basket via for loop
           new_course_basket list gets created for courses which will not be deleted
           courses_count is a count check for number of taken TE courses
           first if statement checks for the course type
           second if statement checks for the courses_count ,creates the error and adds course to the student's non_taken_courses
        """
        will_be_removed = list(filter(lambda course: course.course_type == 'TE', student.course_basket))[2:]
        for course in will_be_removed:
            err = Error('Advisor', course, "Two Technical Elective")
            course.error_map["Two Technical Elective"].append(err)
            student.add_error(err)
            student.add_non_taken(course)
        student.remove_from_basket(will_be_removed)

    def check_fte(self, student):
        """
           filtered variable filters the FTE courses in course_basket
           try except statement makes the error creation
           try -> looks for list(filtered)[0] and creates the error and adds course to the student's non_taken_courses
           except -> will be filled in terms of IndexError
        """
        course_basket = student.course_basket
        filtered = filter(lambda course: course.course_type == 'FTE', course_basket)

        # instead of using for we can use try except
        try:
            course = list(filtered)[0]
            err = Error('Advisor', course, "Graduation Year")
            course.error_map["Graduation Year"].append(err)
            student.add_error(err)
            student.add_non_taken(course)
            student.remove_from_basket(list(filtered))
        except IndexError:
            pass

    def check_graduation_project(self, student):
        """
           filtered variable filters the cse4197 course_id
           if statement checks for students completed credits and if it is smaller than 165 it gets in to try except statement
           try -> looks for list(filtered)[0] and creates the error and adds course to the student's non_taken_courses
           except -> will be filled in terms of IndexError
        """
        course_basket = student.course_basket
        filtered = filter(lambda course: course.course_id == 'CSE4297' or course.course_id == 'CSE4298', course_basket)
        if student.completed_credit < 165:
            try:
                course = list(filtered)[0]
                err = Error('Advisor', course, 'Project')
                course.error_map['Project'].append(err)
                student.add_error(err, course)
                student.will_be_removed(list(filtered))
            except IndexError:
                pass

    def check_minimum_credit(self, student):
        """
           course variable gets in to course_basket via for loop
           if statement checks if course_type equals to TE and completed_credit < minimum_credit
           creates the error and adds course to the student's non_taken_courses
        """
        course_basket = student.course_basket
        will_be_removed = list()
        for course in course_basket:
            if course.course_type == 'TE' and student.completed_credit < course.mimimum_credit:
                err = Error('Advisor', course, "Uncompleted Credit")
                course.error_map["Uncompleted Credit"].append(err)
                student.add_error(err, course)
                will_be_removed.append(course)
        student.remove_from_basket(will_be_removed)

    def check_collision(self, course_basket, student):
        will_be_removed = list()
        for main_course in course_basket:
            if main_course in will_be_removed:
                continue
            for second_course in course_basket:
                if main_course is second_course or second_course in will_be_removed:
                    continue
                if main_course.compare(second_course):
                    if main_course.course_type == 'Must':
                        err = Error('Advisor', second_course, 'Collision')
                        second_course.error_map['Collision'].append(err)
                        student.add_error(err, second_course)
                        will_be_removed.append(second_course)
                    else:
                        err = Error('Advisor', main_course, 'Collision')
                        main_course.error_map['Collision'].append(err)
                        student.add_error(err, main_course)
                        will_be_removed.append(main_course)
        student.remove_from_basket(will_be_removed)

    def approve_student_basket(self, student):
        """first if statement checks for the season, if it is fall it calls the check_two_technical method
           second if statement checks for the semester_id equals 7 or 8, if it is not equal them and season is Fall, check_fte method gets called
           """
        season = student.semester.season
        semester_id = student.semester.semester_id

        if season == 'Fall':
            self.check_two_technical(student)

        if not (semester_id == 7 or semester_id == 8) and season == 'Fall':
            self.check_fte(student)

        self.check_graduation_project(student)
        self.check_minimum_credit(student)

        course_basket = student.course_basket
        self.check_collision(course_basket, student)
