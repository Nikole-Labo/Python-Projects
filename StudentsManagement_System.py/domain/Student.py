"""Manage a list of students. Each student has an id (integer, unique), a name (string) and a group (positive integer)."""
class Student:
    def __init__(self, id_, name, group):
        self.__id_ = id_
        self.__name = name
        self.__group = group

    @property
    def id_(self):
        return self.__id_

    @property
    def name(self):
        return self.__name

    @property
    def group(self):
        return self.__group


    def __str__(self):
        return "Id: " + str(self.id_) + ",  Name: " + self.__name +", Group: " + str(self.__group) +"\n"
    __repr__ = __str__

    def __eq__(self, other):
        return self.id_ == other.id_ and self.name == other.name and self.group == other.group
