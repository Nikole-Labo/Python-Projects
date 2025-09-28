class Room:

    def __init__(self, room_number, room_type):
        self.__room_number = room_number
        self.__type = room_type

    @property
    def room_number(self):
        return self.__room_number

    @room_number.setter
    def room_number(self, value):
        self.__room_number = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def __str__(self):
        return "Room number: " + str(self.room_number) + ", Room type: " + str(self.type) + "\n"

    __repr__ = __str__
