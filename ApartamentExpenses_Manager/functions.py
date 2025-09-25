from random import randint
import random
from copy import deepcopy
import constants

def generate_random_expenses (number_of_expenses :int) :
    expenses_list = []
    expense_types = ["water", "heating", "electricity", "gas", "other"]
    while number_of_expenses > constants.positive_number:
        apartment_number = randint(constants.positive_number, constants.maximum_apartment_number)
        expense_amount = randint(constants.positive_number, constants.maximum_expense_amount)
        expense_type = random.choice(expense_types)
        expense = create_new_expense(apartment_number, expense_amount, expense_type)
        expenses_list.append(expense)
        number_of_expenses -= 1
    return expenses_list

def create_new_expense(apartment_number: int, expense_amount: int, expense_type: str) :
    expense_types = ["water", "heating", "electricity", "gas", "other"]
    if apartment_number < constants.positive_number or expense_amount < constants.positive_number:
        raise ValueError("invalid data for apartment number or expense amount")
    if expense_type not in expense_types:
        raise ValueError("invalid expense type")
    return {"apartment_number": apartment_number, "expense_amount": expense_amount, "expense_type": expense_type}

def get_apartment_number( expense: dict):
    return expense["apartment_number"]

def get_expense_amount(expense: dict):
    return expense["expense_amount"]

def get_expense_type(expense: dict):
    return expense["expense_type"]

def add_new_expense(expenses_list, expense, expenses_history_list):
    expenses_history_list.append(deepcopy(expenses_list))
    expenses_list.append(expense)

def verify_if_apartment_exists(expenses_list, apartment_number):
    all_apartments = []
    for expense in expenses_list:
        all_apartments.append(get_apartment_number(expense))
    if apartment_number not in all_apartments:
        return False
    return True

def verify_if_expense_type_exists(expenses_list, expense_type):
    all_existent_types = []
    for expense in expenses_list:
        all_existent_types.append(get_expense_type(expense))
    if expense_type not in all_existent_types:
        return False
    return True

def remove_expenses(expenses_list, apartment_number, expenses_history_list):
    expenses_history_list.append(deepcopy(expenses_list))
    if verify_if_apartment_exists(expenses_list, apartment_number):
        for expense in expenses_list:
            if get_apartment_number(expense) == apartment_number:
                expenses_list.remove(expense)
    else:
        raise ValueError("This apartment does not exist!")

def remove_expenses_by_type(expenses_list, expense_type, expenses_history_list):
    expenses_history_list.append(deepcopy(expenses_list))
    if verify_if_expense_type_exists(expenses_list, expense_type):
        for expense in expenses_list:
            if get_expense_type(expense) == expense_type:
                expenses_list.remove(expense)
    else:
        raise ValueError("This type of expense does not exist in the list!")

def verify_command(command_words):
    expense_types = ["water", "heating", "electricity", "gas", "other"]
    if command_words[constants.base_of_the_list] in expense_types:
        return False
    return True

def replace_expense_amount(expenses_list, apartment_number, expense_type, new_expense_amount, expenses_history_list):
    expenses_history_list.append(deepcopy(expenses_list))
    all_expenses_for_this_apartment = get_expenses_by_apartment(expenses_list, apartment_number)
    for expense in all_expenses_for_this_apartment:
        if expense_type == get_expense_type(expense):
            expenses_list.remove(expense)
            updated_expense = create_new_expense(apartment_number, new_expense_amount, expense_type)
            expenses_list.append(updated_expense)
        else:
            raise ValueError("There is no such expense for this appartment!")


def get_expenses_by_apartment(expenses_list, apartment):
    all_expenses_for_this_apartment = []
    if verify_if_apartment_exists(expenses_list, apartment):
        for expense in expenses_list:
            if apartment == get_apartment_number(expense):
                all_expenses_for_this_apartment.append(expense)
    else:
        raise ValueError("That apartment does not exist!")
    return all_expenses_for_this_apartment

def calculate_total_expenses_amount_per_apartment(expenses_list, apartment_number):
    total_expense_amount = constants.base_case
    all_expenses_for_this_apartment = get_expenses_by_apartment(expenses_list, apartment_number)
    for expense in all_expenses_for_this_apartment:
        total_expense_amount += get_expense_amount(expense)
    return total_expense_amount

def get_apartments_and_their_total_expense_amount(expenses_list, total_amount, comparison_signe):
    apartments_list = []
    total_expenses_amount = []
    for expense in expenses_list:
        if get_apartment_number(expense) not in apartments_list:
            apartments_list.append(get_apartment_number(expense))
            total_expenses_amount.append(calculate_total_expenses_amount_per_apartment(expenses_list, get_apartment_number(expense)))

    if len(apartments_list) != len(total_expenses_amount):
        raise ValueError("The lengths of the two lists must be the same.")

    list_of_apartment_annd_total_expense = []
    for index in range(len(apartments_list)):
        apartment_data = {
            "apartment_number": apartments_list[index],
            "total_expense_amount": total_expenses_amount[index]
        }
        list_of_apartment_annd_total_expense.append(apartment_data)
    filtered_list_of_apartments_and_total_expense = []
    if comparison_signe == "=":
            for expense in list_of_apartment_annd_total_expense:
                if expense["total_expense_amount"] == total_amount:
                    filtered_list_of_apartments_and_total_expense.append(expense)
    elif comparison_signe == "<":
        for expense in list_of_apartment_annd_total_expense:
            if expense["total_expense_amount"] < total_amount:
                filtered_list_of_apartments_and_total_expense.append(expense)
    elif comparison_signe == ">":
        for expense in list_of_apartment_annd_total_expense:
            if expense["total_expense_amount"] > total_amount:
                filtered_list_of_apartments_and_total_expense.append(expense)
    else:
        raise ValueError("That was not a valid comparison signe")
    return filtered_list_of_apartments_and_total_expense

def filter_by_expense_amount(expenses_list, expense_amount):
    filtered_expenses = []
    for expense in expenses_list:
        if expense_amount == get_expense_amount(expense):
            filtered_expenses.append(expense)
    return filtered_expenses

def filter_by_expense_type(expenses_list, expense_type):
    if not verify_command(expense_type):
        raise ValueError ("That was not a valid expense type!")
    filtered_expenses = []
    for expense in expenses_list:
        if expense_type == get_expense_type(expense):
            filtered_expenses.append(expense)
    return filtered_expenses
