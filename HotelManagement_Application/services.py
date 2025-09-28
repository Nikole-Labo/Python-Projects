from repository import Repository
from errors import DateException

class Services:

    def __init__(self, repository):
        self.__repository = repository

    def verify_rooms_services(self):
        self.__repository.verify_rooms()


    def verify_dates(self, start_date, end_date):
        if not self.__repository.is_valid_date_format(start_date) or not self.__repository.is_valid_date_format(end_date):
            raise DateException("Those were not valid dates:(")
        if start_date > end_date:
            raise DateException("The departure date can't be before the arrival date")

    def get_all_reservations(self, start_date, end_date):
        sorted_arrival = sorted(self.__repository.get_reservations(start_date, end_date), key=lambda x: x.arrival)
        sorted_result = sorted(sorted_arrival, key=lambda x: x.name)
        return sorted_result

    def get_all_reservations_room(self, start_date_obj, end_date_obj, room_nr):
        sorted_arrival = sorted(self.__repository.get_reservations_room(start_date_obj, end_date_obj, room_nr), key=lambda x: x.arrival)
        sorted_result = sorted(sorted_arrival, key=lambda x: x.name)
        return sorted_result

    def delete_for_dates(self, deleted_list):
        self.__repository.delete_by_dates(deleted_list)

    def get_month(self, lst):
        used_month = self.__repository.used_month(lst)
        return used_month

    def generate100(self):
        self.__repository.generate_1000()

    def get_available(self, arrival_date, departure_date):
        print("in get available services")
        return self.__repository.available_rooms(arrival_date, departure_date)

    def verify_data(self, room_number, name, guests, available_rooms):
        self.__repository.verify(room_number, name, guests, available_rooms)

    def add_reservation(self, arrival_date, departure_date, name, room_number, guests):
        self.__repository.make_reservation(arrival_date, departure_date, name, room_number, guests)


    def delete_reservation_by_id(self, reservation_id):
        self.__repository.delete(reservation_id)
