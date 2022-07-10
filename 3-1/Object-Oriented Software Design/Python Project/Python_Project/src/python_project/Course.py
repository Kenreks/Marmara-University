import capacity as capacity
from Error import Error
from Schedule import Schedule


class Course:

    def __init__(self, course_id, name, course_type, capacity=0, instructor=None, credit=0, ects=0, schedule_list=None):
        self.course_id = course_id
        self.name = name
        self.course_type = course_type
        self.capacity = int(capacity)
        self.instructor = instructor
        self.credit = credit
        self.ects = ects
        self.students = list()
        self.prerequisites = list()
        self.schedule = dict()  # { "Day": Schedule() }
        self.set_schedule(schedule_list)
        self.error_map = {'Quota': [], 'Prerequisite': [], 'Project': [], 'Collision': [], 'Uncompleted Credits': [],
                          'Graduation Year': [], 'Two Technical Elective': []}

    def add_student(self, student):
        self.students.append(student)

    def set_schedule(self, schedule_list):
        """This method creates each schedule object of course"""
        for val in schedule_list:
            day = val['Day']
            self.schedule[day] = Schedule(val['Day'], val['Start'], val['End'])

    def compare(self, second_course):
        for sch in list(self.schedule.values()):
            try:
                second_sch = second_course.schedule[sch.day]
                if sch.compare(second_sch):
                    return True
            except KeyError:
                continue

    def approve_course(self, student):
        """ This method checks if given student satisfies registration criterias of this course """
        capacity_check = True
        elective_check = True
        prerequisite_check = True

        # Capacity check
        if self.capacity != 0 and self.capacity <= len(self.students):
            # Quota error call transcript
            err = Error('System', self, 'Quota')
            self.error_map['Quota'].append(err)
            student.add_error(err,self)
            capacity = False

        # Prerequisite Check
        if not all(course in student.past_courses for course in self.prerequisites):
            # prerequisite error
            #print(self)
            err = Error('System', self, 'Prerequisite')
            self.error_map['Prerequisite'].append(err)
            student.add_error(err,self)
            prerequisite_check = False

        if (self.course_type != "Must") and (self in student.past_courses or self in student.course_basket):
            elective_check = False

        return capacity_check and elective_check and prerequisite_check

    def __str__(self) -> str:
        return f'Course_id={self.course_id}, name={self.name}, instructor={self.instructor}, schedule={self.schedule}'

    def __repr__(self) -> str:
        return f'Course_id={self.course_id}, name={self.name}, instructor={self.instructor}, schedule={self.schedule}'
