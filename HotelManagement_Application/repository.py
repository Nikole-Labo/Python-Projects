import random

from domain import Reservation
from room import Room
from errors import NoRooms, Reservation_Validator
from datetime import date, datetime, timedelta

class Repository:

    def __init__(self):
        self.reservations = []
        self.rooms = []
        self.load_from_file()
        self.load_rooms()

    def is_valid_date_format(self, date_str):
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return True
        except ValueError:
            return False

    def verify_id(self, id):
        for reservation in self.reservations:
            if reservation.reservation_nr == id:
                return False
        return True

    def check_empty(self, arrival_date, departure_date, room_number):
        for reservation in self.reservations:
            if reservation.arrival >= arrival_date and reservation. arrival < departure_date and reservation.reservation_nr% 100 == room_number:
                return False
            if reservation.departure > arrival_date and reservation.departure <= departure_date and reservation.reservation_nr % 100 == room_number:
                return False
        return True


    def generate_reservation(self):
        room_number = random.randint(1, 5)
        reservation_id = int(str(random.randint(100, 999)) + str(room_number))
        while not self.verify_id(reservation_id):
            room_number = random.randint(1, 5)
            reservation_id = int(str(random.randint(100, 999)) + str(room_number))
        print(f"generated the valid id: {reservation_id}")

        year = 2025
        arrival_date = datetime(year, random.randint(1, 12), random.randint(1, 28))
        departure_date = arrival_date + timedelta(days = random.randint(1, 5))
        while not self.check_empty(arrival_date, departure_date, room_number):
            arrival_date = datetime(year, random.randint(1, 12), random.randint(1, 28))
            departure_date = arrival_date + timedelta(days=random.randint(1, 5))
        print(f"generated the valid dates: {arrival_date}, {departure_date}")

        first_name = ["Luca", "Ioana", "Andrei", "Vasile", "Maria", "Carla", "Dorina", "Alex", "Ion", "Mihai", "Mihaela", "Roxana", "Eliza", "Cosmin", "Bogdan", "Mara", "Ariana", "Patricia", "Eduard", "Rares", "David", "Daria", "Doina", "Anastasia", "Elena", "Emanuel", "Artur", "Olimpiu", "Nikole"]
        last_name = ["Labo", "Bandla", "Damsa", "Brumar", "Pop", "Popescu", "Mare", "Nicoara", "Grosu", "Lungu", "Cadar", "Ciorca", "Barbanta", "Culcer", "Chereches", "Aioanei", "Peter", "Bubuiug", "Ciupe", "Laza", "Ilies", "Manciu", "Sarca"]
        name = random.choice(first_name) + " " + random.choice(last_name)
        print(f"generated the name: {name}")
        if room_number < 3:
            guests = 1
        elif room_number == 3 or room_number == 4:
            guests = random.randint(1, 2)
        else:
            guests = random.randint(1, 4)
        return Reservation(reservation_id, room_number, name, guests, arrival_date, departure_date)

    def generate_1000(self):
        number = 100
        while number != 0:
            self.reservations.append(self.generate_reservation())
            number -= 1
        self.save_in_file()

    def load_from_file(self):
        try:
            with open("reservation.txt", 'rt') as file:
                self.reservations = []  # Clear the current reservations list
                for line in file:
                    # Split the line into fields based on the delimiter
                    fields = line.strip().split(', ')

                    if len(fields) == 6:
                        reservation_nr = int(fields[0])
                        room_nr = int(fields[1])
                        name = fields[2]
                        guests = int(fields[3])
                        arrival = datetime.strptime(fields[4], '%d-%m-%Y')
                        departure = datetime.strptime(fields[5], '%d-%m-%Y')

                        reservation = Reservation(reservation_nr, room_nr, name, guests, arrival, departure)

                        self.reservations.append(reservation)
        except FileNotFoundError:
            print("The file 'reservation.txt' does not exist.")
        except IOError as e:
            print(f"Error loading reservations from file: {e}")
        except ValueError as e:
            print(f"Error parsing reservation data: {e}")


    def load_rooms(self):
        try:
            with open("rooms.txt", 'rt') as file:
                self.rooms = []  # Clear the current reservations list
                for line in file:
                    fields = line.strip().split(', ')
                    if len(fields) == 2:
                        room_nr = int(fields[0])
                        room_type = fields[1]
                        room = Room(room_nr, room_type)

                        self.rooms.append(room)
                        print(room)
        except FileNotFoundError:
            print("The file 'reservation.txt' does not exist.")
        except IOError as e:
            print(f"Error loading reservations from file: {e}")
        except ValueError as e:
            print(f"Error parsing reservation data: {e}")

    def save_in_file(self):
        try:
            with open("reservation.txt", 'wt') as file:
                for reservation in self.reservations:
                    reservation_fields = (
                        f"{reservation.reservation_nr}, {reservation.room_nr}, {reservation.name}, "
                        f"{reservation.guests}, {reservation.arrival.strftime('%d-%m-%Y')}, "
                        f"{reservation.departure.strftime('%d-%m-%Y')}\n"
                    )
                    file.write(reservation_fields)
        except IOError as e:
            print(f"Error saving reservations to file: {e}")

    def get_reservations(self, start_date, end_date):
        result = []
        for reservation in self.reservations:
            if reservation.arrival >= start_date and reservation.arrival <= end_date:
                result.append(reservation)
        return result

    def get_reservations_room(self, start_date_obj, end_date_obj, room_nr):
        result = []
        for reservation in self.reservations:
            if reservation.arrival >= start_date_obj and reservation.arrival <= end_date_obj and reservation.room_nr == room_nr:
                result.append(reservation)
        return result

    def used_month(self, lst):
        result = {}
        for reservation in lst:
            reservation_month = reservation.arrival.month
            if reservation_month not in result:
                result[reservation_month] = []
            result[reservation_month].append(reservation)
        for e in result:
            print(e)
        return result

    def available_rooms(self, arrival_date, departure_date):
        free_rooms = []
        for room in self.rooms:
            if self.check_empty(arrival_date, departure_date, room.room_number):
                free_rooms.append(room)
        return free_rooms

    def verify(self, room_nr, name, guests, available_rooms):
        ok = 0
        for room in available_rooms:
            if room_nr == room.room_number:
                ok = 1
        if ok == 0:
            raise Reservation_Validator("That room is not available")
        if len(name) < 3 or name == "":
            raise Reservation_Validator("That was not a valid name")
        if room_nr < 3 and guests != 1:
            raise Reservation_Validator("The number of guests is not appropiate for this room")
        if room_nr == 3 or room_nr == 4:
            if guests > 2 or guests < 1:
                raise Reservation_Validator("The number of guests is not appropiate for this room")
        if room_nr == 5:
            if guests > 4 or guests < 1:
                raise Reservation_Validator("The number of guests is not appropiate for this room")

    def make_reservation(self, arrival_date, departure_date, name, room_number, guests):
        reservation_id = int(str(random.randint(100, 999)) + str(room_number))
        self.reservations.append(Reservation(reservation_id, room_number, name, guests, arrival_date, departure_date))
        self.save_in_file()

    def delete(self, reservation_id):
        if self.verify_id(reservation_id):
            raise Reservation_Validator("There is no reservation with this id")
        for reservation in self.reservations:
            if reservation.reservation_nr == reservation_id:
                self.reservations.remove(reservation)
        self.save_in_file()

    def delete_by_dates(self, deleted_list):
        for reservation in deleted_list:
            if reservation in self.reservations:
                self.reservations.remove(reservation)
        self.save_in_file()





