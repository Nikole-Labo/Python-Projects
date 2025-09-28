import unittest
from datetime import datetime
from repository import Repository
from services import Services
from domain import Reservation
from room import Room
from errors import Reservation_Validator, DateException


class TestReservationSystem(unittest.TestCase):

    def setUp(self):
        self.repository = Repository()
        self.services = Services(self.repository)
        self.repository.rooms = [
            Room(1, "single"),
            Room(2, "single"),
            Room(3, "double"),
            Room(4, "double"),
            Room(5, "family")
        ]
        self.repository.reservations = []

    def test_verify_valid_room(self):
        available_rooms = [Room(3, "double"), Room(4, "double"), Room(5, "family")]
        try:
            self.repository.verify(3, "John Doe", 2, available_rooms)
        except Reservation_Validator as e:
            self.fail(f"verify raised an exception unexpectedly: {e}")

    def test_verify_invalid_room(self):
        available_rooms = [Room(4, "double"), Room(5, "family")]
        with self.assertRaises(Reservation_Validator) as context:
            self.repository.verify(3, "John Doe", 2, available_rooms)
        self.assertEqual(str(context.exception), "That room is not available")

    def test_verify_invalid_name(self):
        available_rooms = [Room(3, "double"), Room(4, "double"), Room(5, "family")]
        with self.assertRaises(Reservation_Validator) as context:
            self.repository.verify(3, "Jo", 2, available_rooms)
        self.assertEqual(str(context.exception), "That was not a valid name")

    def test_verify_invalid_guest_count(self):
        available_rooms = [Room(3, "double"), Room(4, "double"), Room(5, "family")]
        with self.assertRaises(Reservation_Validator) as context:
            self.repository.verify(3, "John Doe", 3, available_rooms)
        self.assertEqual(str(context.exception), "The number of guests is not appropiate for this room")

    def test_available_rooms(self):
        self.repository.reservations = [
            Reservation(1013, 3, "John Doe", 2, datetime(2025, 2, 15), datetime(2025, 2, 16))
        ]
        arrival_date = datetime(2025, 2, 15)
        departure_date = datetime(2025, 2, 16)
        free_rooms = self.repository.available_rooms(arrival_date, departure_date)
        self.assertEqual(len(free_rooms), 4)  # Room 3 should be occupied

    def test_add_reservation(self):
        arrival_date = datetime(2025, 2, 15)
        departure_date = datetime(2025, 2, 16)
        name = "Jane Doe"
        room_number = 4
        guests = 2
        self.services.add_reservation(arrival_date, departure_date, name, room_number, guests)
        self.assertEqual(len(self.repository.reservations), 1)
        reservation = self.repository.reservations[0]
        self.assertEqual(reservation.name, name)
        self.assertEqual(reservation.room_nr, room_number)

    def test_verify_dates_valid(self):
        try:
            self.services.verify_dates("15-02-2025", "16-02-2025")
        except DateException as e:
            self.fail(f"verify_dates raised an exception unexpectedly: {e}")

    def test_verify_dates_invalid_format(self):
        with self.assertRaises(DateException) as context:
            self.services.verify_dates("15/02/2025", "16/02/2025")
        self.assertEqual(str(context.exception), "Those were not valid dates:(")

    def test_verify_dates_invalid_order(self):
        with self.assertRaises(DateException) as context:
            self.services.verify_dates("16-02-2025", "15-02-2025")
        self.assertEqual(str(context.exception), "The departure date can't be before the arrival date")

if __name__ == "__main__":
    unittest.main()
