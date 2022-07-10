import json
import os

class OutputWriter:

    def write_transcript(self, transcript_map):

        newpath = 'transcripts'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        with open('transcripts/' + str(transcript_map['ID']) + '.json', "w") as transcript_json:
            json.dump(transcript_map, transcript_json, indent=4)

    def write_department_output(self, department_output):
        with open('department_output.json', "w") as output_json:
            json.dump(department_output, output_json, indent=4)

    def start_writer(self, student_map):
        for student in list(student_map.values()):
            self.write_transcript(student.transcript.transcript_map)