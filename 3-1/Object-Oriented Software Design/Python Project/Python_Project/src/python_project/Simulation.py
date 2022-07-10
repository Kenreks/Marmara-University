from InputReader import InputReader
from Department import Department
from OutputWriter import OutputWriter


class Simulation:
    def __init__(self):
        self.input_reader = InputReader()
        self.department = Department()

    def simulate_semester(self):
        self.department.start_registration()
        self.department.next_semester()


    def initialize_department(self):
        config = self.input_reader.read_config()
        self.input_reader.read_instructor(self.department)
        self.input_reader.read_courses(self.department)
        self.input_reader.read_prerequisite(self.department)

        if config['Generation'] == 1:
            firs_student = 999
            last_student = 999
            if config['Season'] == 'Fall':
                last_semester = 7
            elif config['Season'] == 'Spring':
                last_semester = 8
            else:
                last_semester = 0
                # Error
            for i in range(1, last_semester):
                if i % 2 == 1:
                    last_student = self.input_reader.read_students(self.department, last_student)
                self.simulate_semester()
            if config['Season'] == 'Fall':
                # Check duplicate code
                last_student = self.input_reader.read_students(self.department, last_student)
        else:
            """
            Read students from transcript files
            """

            pass

    def start_simulation(self):
        #self.initialize_department()
        self.input_reader.read_instructor(self.department)
        self.input_reader.read_courses(self.department)
        self.input_reader.read_prerequisite(self.department)
        self.input_reader.read_students(self.department,0)

        for i in range(1,7):
            self.simulate_semester()
        writer = OutputWriter()
        writer.start_writer(self.department.students)


