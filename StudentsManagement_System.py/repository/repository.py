from src.domain.students import Student
import copy
from src.error.MyException import Empty_history_exception, RepositoryException, NotFound
from random import randint, choice
import random
from src import constants
class Repository:
    def __init__(self):
        self._students_list = []
        self._history_list = []
        self.generate_n_students()

    def generate_random_student(self):
        # generate id
        id_used = []
        id_ = randint(constants.id_lower_bound, constants.id_upper_bound)
        while id_ in id_used:
            id_ = randint(constants.id_lower_bound, constants.id_upper_bound)
        id_used.append(id_)
        #generate name
        first_name = ["Alex", "Gloria", "Anne", "John", "Thomas", "Amy", "Aaron", "Michel", "Larisa", "David"]
        last_name = ["Pop", "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Lopez", "Davis"]
        name = random.choice(first_name) + " " + random.choice(last_name)
        # generate group
        group = randint(constants.first_group, constants.last_group)

        return Student(id_, name, group)

    def add_generated_student(self, new_student: Student):
        self._students_list.append(new_student)

    def generate_n_students(self):
        for each in range(constants.students_number):
            self.add_generated_student(self.generate_random_student())

    def undo_command(self):
        if len(self._history_list) < constants.minimum_program_state:
            raise Empty_history_exception("Empty history!")
        else:
            self._students_list = copy.deepcopy(self._history_list[constants.last_program_state])
            self._history_list.pop()


    def add_to_history_list(self):
        self._history_list.append(copy.deepcopy(self._students_list))

    def add_student(self, new_student: Student):
        self.add_to_history_list()
        self.verify_id_already_exists(new_student.id_)
        self._students_list.append(new_student)

    def verify_id_already_exists(self, _id):
        for student in self._students_list:
            if str(_id) == str(student.id_):
                raise RepositoryException(" OOps! :/ There already exists a student with this id!")


    def get_all_students(self):
        return self._students_list[:]

    def delete_students_from_group(self, group):
        self.add_to_history_list()
        all_students_verified = False
        students_list = self._students_list[:]
        while all_students_verified == False:
            all_students_verified = True
            for student in students_list:
                if str(student.group) == str(group):
                    students_list.remove(student)
                    all_students_verified = False
            self._students_list = students_list
        return students_list

class TextFileRepository (Repository):
    pass

class BinaryRepository (Repository):
    pass

