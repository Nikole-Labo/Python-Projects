from A8_2_2.repository.client_repository import Client_Repository
from A8_2_2.services.clients_services import Client_Services
from A8_2_2.domain.validators_exceptions import ClientValidatorException, InputError
from unittest.case import TestCase

import unittest

class TestClientServices(unittest.TestCase):
    def setUp(self):
        self.client_repository = Client_Repository()
        self.client_services = Client_Services(self.client_repository)

    def test_add_client_valid(self):
        client_id = "1234"
        name = "Test Client"
        self.client_services.add_client(client_id, name)
        added_client = self.client_services.find_client_id_services(client_id)
        self.assertTrue(added_client)

    def test_add_client_invalid_id(self):
        with self.assertRaises(ClientValidatorException):
            self.client_services.add_client("invalid_id", "Invalid Client")

    def test_add_client_existing_id(self):
        self.client_services.add_client("5678", "Existing Client")
        with self.assertRaises(ClientValidatorException):
            self.client_services.add_client("5678", "Duplicate Client")

    def test_add_client_empty_name(self):
        with self.assertRaises(ClientValidatorException):
            self.client_services.add_client("9999", "")

    def test_list_clients_with_clients(self):
        self.client_services.add_client("1234", "Client 1")
        self.client_services.add_client("5678", "Client 2")
        expected_result = self.client_repository.get_all_clients()
        result = self.client_services.list_clients()
        self.assertEqual(result, expected_result)

    def test_delete_client_valid(self):
        client_id = "1234"
        name = "Test Client"
        self.client_services.add_client(client_id, name)
        self.client_services.delete_client(client_id)
        with self.assertRaises(InputError):
            self.client_services.search_client_id_services(client_id)

    def test_delete_client_invalid_id(self):
        with self.assertRaises(InputError):
            self.client_services.delete_client("invalid_id")

    def test_delete_client_nonexistent(self):
        with self.assertRaises(InputError):
            self.client_services.delete_client("9999")

    def test_update_client_invalid_id(self):
        with self.assertRaises(ClientValidatorException):
            self.client_services.update_client("invalid_id", "Updated Client")

    def test_update_client_empty_name(self):
        client_id = "5678"
        name = "Test Client"
        self.client_services.add_client(client_id, name)

        with self.assertRaises(ClientValidatorException):
            self.client_services.update_client(client_id, "")

    if __name__ == "__main__":
        unittest.main()
