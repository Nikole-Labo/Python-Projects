from src.repository.Repo import Repository
from src.domain.students import Student
import pickle
import random
from random import randint, choice
from src.error.MyException import RepositoryException
from src import constants
class BinaryRepo(Repository):
    def __init__(self, file_name="students.bin"):
        super(BinaryRepo, self).__init__()
        self._file_name = file_name
        self._load_from_file()

    def _load_from_file(self):
        try:
            fin = open(self._file_name, 'rb')
            obj = pickle.load(fin)

        except EOFError:
            return

        for new_expense in obj:
            super().add_student(new_expense)
        fin.close()

    def save_in_file(self):
        file = open(self._file_name, "wb")
        pickle.dump(self.get_all_students(), file)
        file.close()


    def add_student(self, new_student):
        super().add_student(new_student)
        self.save_in_file()

    def delete_students_from_group(self, group):
        super().delete_students_from_group(group)
        self.save_in_file()

    def undo_command(self):
        super().undo_command()
        self.save_in_file()



