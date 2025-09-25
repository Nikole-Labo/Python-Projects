
from src.repository.Repo import Repository
from src.domain.students import Student
import os
from src import constants

class TextFileRepo(Repository):
    def __init__(self, file_name="students.txt"):
        super(TextFileRepo, self).__init__()
        self._file_name = file_name
        self.load_from_file()

    def load_from_file(self):
        lines_from_file = []

        try:
            file = open(self._file_name, 'rt')
            lines_from_file = file.readlines()
            file.close()
        except IOError:
            pass

        for to_read in lines_from_file:
            if to_read.strip():
                line = to_read.split(",")
                new_student = Student(int(line[constants.id_argument].strip()), line[constants.name_argument].strip(), int(line[constants.group_argument].strip()))
                super().add_student(new_student)

    def save_in_file(self):
        file = open(self._file_name, "wt")

        for student in self.get_all_students():
            students_list = str(student.id_) + ',' + str(student.name) + ',' + str(student.group) + "\n"
            file.write(students_list)
            file.flush()
            os.fsync(file.fileno())
        file.close()

    def add_student(self, new_student: Student):
        super().add_student(new_student)
        self.save_in_file()

    def delete_students_from_group(self, group):
        super().delete_students_from_group(group)
        self.save_in_file()

    def undo_command(self):
        super().undo_command()
        self.save_in_file()

    def clean_file(self):
        file = open(self._file_name, "wt")
        file_content = ""
        file.write(file_content)
        file.flush()
        os.fsync(file.fileno())
        file.close()
