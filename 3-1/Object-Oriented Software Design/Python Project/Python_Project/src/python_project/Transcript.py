class Transcript:

    def __init__(self,student):
        self.student = student
        self.transcript_map = dict()
        self.transcript_map['ID'] = str(student.student_id)
        self.create_semester()


    def create_semester(self):
        semester_map = {"Courses": dict(), "Errors": list()}
        self.transcript_map["Semester-" + str(self.student.semester.semester_id)] = semester_map

    def add_course(self, course_id, letter_grade):
        self.transcript_map["Semester-" + str(self.student.semester.semester_id)]["Courses"][course_id] = letter_grade

    def add_error(self, error):
        self.transcript_map["Semester-" + str(self.student.semester.semester_id)]["Errors"].append(error.raise_error())

    def add_gpa(self, gpa, active_credit, cgpa, cumulative_credit):
        self.transcript_map["Semester-" + str(self.student.semester.semester_id)]["GPA"] = "{:.2f}".format(gpa)
        self.transcript_map["Semester-" + str(self.student.semester.semester_id)]["Active Credit"] = str(active_credit)
        self.transcript_map["CGPA"] = "{:.2f}".format(cgpa)
        self.transcript_map["Cumulative Credit"] = str(cumulative_credit)
