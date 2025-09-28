class Reservation:

    def __init__(self, reservation_number, room_number, family_name, guests, arrival_date, departure_date):
        self.__reservation_nr = reservation_number
        self.__room_nr = room_number
        self.__name = family_name
        self.__guests = guests
        self.__arrival = arrival_date
        self.__departure = departure_date

    @property
    def reservation_nr(self):
        return self.__reservation_nr

    @reservation_nr.setter
    def reservation_nr(self, value):
        self.reservation_nr = value

    @property
    def room_nr(self):
        return self.__room_nr

    @room_nr.setter
    def room_nr(self, value):
        self.__room_nr = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def guests(self):
        return self.__guests

    @guests.setter
    def guests(self, value):
        self.__guests = value

    @property
    def arrival(self):
        return self.__arrival

    @arrival.setter
    def arrival(self, value):
        self.__arrival = value

    @property
    def departure(self):
        return self.__departure

    @departure.setter
    def departure(self, value):
        self.__departure = value

    def __str__(self):
        return "Reservation number: " + str(self.reservation_nr) + ", Room number: " + str(self.room_nr) + \
            ", Name :" + str(self.name) + ", number ofe guests: " + str(self.guests) + ", Arrival date: " + \
            str(self.arrival) + ", Departure date: " + str(self.departure) + "\n"

    __repr__ = __str__



