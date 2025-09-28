from prettytable import PrettyTable

from services import Services
from errors import NoRooms, Reservation_Validator, DateException
from datetime import datetime
class UI:

    def __init__(self, services):
        self.__services = services
        self.exit_flag = False

    def get_input (self, txt="->"):
        return input(txt)

    def menu(self):
        print("__________________________________________")
        print("1.show reservations")
        print("2. generate 100 reservations")
        print("3. make a reservation")
        print("4. delete a reservation")
        print("5. delete reservations by dates")
        print("0.exit")
        print("__________________________________________")

    def choose_option(self, option):
        if option == "1":
            self.show_reservations()
        elif option == "2":
            self.__services.generate100()
        elif option == "3":
            self.make_reservation_ui()
        elif option == "4":
            self.delete_reservation()
        elif option == "5":
            self.delete_by_date()
        elif option == "0":
            print("You stopped the program! Bye!")
            self.exit_flag = True
        else:
            print("That was not a valid option!")

    def menu_make_res(self, available_rooms):
        print("_________________________")
        for room in available_rooms:
            print(room)
        print("_________________________")
        print("Enter the room number or 0 if you want to cancel the reservation")


    def delete_reservation(self):
        reservation_id = self.get_input("Give the reservation number that you want to delete: ")
        try:
            self.__services.delete_reservation_by_id(int(reservation_id))
        except Reservation_Validator as ve:
            print(ve)

    def delete_by_date(self):
        start_date = self.get_input("give the start date: ")
        end_date = self.get_input("Give the end date: ")
        room_nr = self.get_input("Give the room for which you want to delete reservations: ")
        try:
            self.__services.verify_dates(start_date, end_date)
            start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
            end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")
            deleted_list = self.__services.get_all_reservations_room(start_date_obj, end_date_obj, int(room_nr))
            reservation_by_month = self.__services.get_month(deleted_list)
            self.display_in_table(reservation_by_month)
            self.__services.delete_for_dates(deleted_list)
        except DateException as ve:
            print(ve)

    def make_reservation_ui(self):
        arrival_date = self.get_input("Arrival date(dd-mm-Y): ")
        departure_date = self.get_input("Departure date(dd-mm-Y): ")
        try:
            self.__services.verify_dates(arrival_date, departure_date)
            arrival_date = datetime.strptime(arrival_date, "%d-%m-%Y")
            departure_date = datetime.strptime(departure_date, "%d-%m-%Y")
            available_rooms = self.__services.get_available(arrival_date, departure_date)
            self.menu_make_res(available_rooms)
            user_input = self.get_input()
            if user_input != "0":
                room_number = int(user_input)
                name = self.get_input("Reservation name: ")
                guests = self.get_input("Number of guests: ")
                self.__services.verify_data(int(room_number), name, int(guests), available_rooms)
                self.__services.add_reservation(arrival_date, departure_date, name, room_number, guests)

        except DateException as ve:
            print(ve)
        except Reservation_Validator as ve:
            print(ve)

    def show_reservations(self):
        start_date = self.get_input("Give the start_date(dd-mm): ") + "-2025"
        end_date = self.get_input("Give the end_date(dd-mm): ") + "-2025"

        try:
            self.__services.verify_dates(start_date, end_date)
            start_date_obj = datetime.strptime(start_date, "%d-%m-%Y")
            end_date_obj = datetime.strptime(end_date, "%d-%m-%Y")
            all_reservations = self.__services.get_all_reservations(start_date_obj, end_date_obj)
            reservation_by_month = self.__services.get_month(all_reservations)
            self.display_in_table(reservation_by_month)
        except DateException as ve:
            print(ve)

    def display_in_table(self, reservations_by_month):
        for month, reservations in sorted(reservations_by_month.items()):
            table = PrettyTable()
            table.field_names = [datetime(2025, month, 1).strftime("%B"), "Name", "Guests"]
            for reservation in sorted(reservations, key=lambda r: (r.arrival, r.name.split()[-1])):
                start = reservation.arrival.strftime("%d.%m")
                end = reservation.departure.strftime("%d.%m")
                table.add_row([f"{start} - {end}", reservation.name, f"{reservation.guests} persons"])
            print(table)

    def start(self):
        while not self.exit_flag:
            self.menu()
            option = self.get_input()
            self.choose_option(option)


