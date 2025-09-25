#
# This is the program's UI module. The user interface and all interaction with the user (print and input statements) are found here
#
from functions import *
from copy import deepcopy
import constants
def show_dictionary():
    print("____________________________________________")
    print("add - To add a new transaction (eg: add 25 gas 100)")
    print("remove - Used to remove all the expenses for an apartment")
    print("replace - used to replace the amount of a utility for an appartment")
    print("list - Display apartments having different properties")
    print("____________________________________________")

def list_UI(expenses_list: list):
    for expense in expenses_list:
        print(expense)

def read_and_add_expense_UI (expenses_list, command_words, expenses_history_list) :
    try :
        apartment_number = int(command_words[constants.base_of_the_list])
        expense_type = command_words[constants.second_element_from_the_list]
        expense_amount = int(command_words[constants.third_element_from_list])
        expense = create_new_expense(apartment_number, expense_amount, expense_type)
        add_new_expense(expenses_list, expense, expenses_history_list)

    except ValueError as ve:
        print("There was an error!")
        print(str(ve))

def remove_expenses_UI(expenses_list, command_words, expenses_history_list):
    if verify_command(command_words):
        try:
            remove_expenses(expenses_list, int(command_words[constants.base_of_the_list]), expenses_history_list)
        except ValueError as ve:
            print("There was an error!")
            print(str(ve))
    else:
        try:
            remove_expenses_by_type(expenses_list, command_words[constants.base_of_the_list], expenses_history_list)
        except ValueError as ve:
            print("There was an error!")
            print(ve)

def remove_for_multiple_apartments_UI(expenses_list, command_words, expenses_history_list):
    try:
        first_apartment = int(command_words[constants.base_of_the_list])
        last_apartment = int(command_words[constants.third_element_from_list])
        for apartment in range(first_apartment, last_apartment):
            remove_expenses(expenses_list, apartment, expenses_history_list)
    except ValueError as ve:
        print("There was an error!")
        print(ve)

def replace_expense_amount_UI(expenses_list, command_words, expenses_history_list):
    try:
        apartment_number = int(command_words[constants.base_of_the_list])
        expense_type = command_words[constants.second_element_from_the_list]
        new_expense_amount = int(command_words[constants.forth_element_from_list])
        replace_expense_amount(expenses_list, apartment_number, expense_type, new_expense_amount, expenses_history_list)
    except ValueError as ve:
        print("There was an error!")
        print(ve)

def list_expenses_for_apartment(expenses_list, command_words):
    try:
        apartment_number = int(command_words[constants.base_of_the_list])
        expenses = get_expenses_by_apartment(expenses_list, apartment_number)
        list_UI(expenses)
    except ValueError as ve:
        print("There was an error!")
        print(ve)

def list_by_total_expense_per_apartment(expenses_list, command_words):
    try:
        total_expense = int(command_words[constants.second_element_from_the_list])
        comparison_signe = command_words[constants.base_of_the_list]
        apartments_list = get_apartments_and_their_total_expense_amount(expenses_list, total_expense, comparison_signe)
        list_UI(apartments_list)
    except ValueError as ve:
        print("There was an error!")
        print(ve)

def filter_expenses(expenses_list, command_words):
    try:
        if not verify_command(command_words[constants.base_of_the_list]):
            filtered_expenses_list = filter_by_expense_amount(expenses_list, int(command_words[constants.base_of_the_list]))
            list_UI(filtered_expenses_list)
        else:
            filtered_expenses_list = filter_by_expense_type(expenses_list, command_words[constants.base_of_the_list])
            list_UI(filtered_expenses_list)
    except ValueError as ve:
        print("There was an error!")
        print(ve)

def add_list_history(history, expenses_list):
    history.append(deepcopy(expenses_list))

def undo(history, expenses_list):
    if len(history) > constants.base_of_the_list:
        history.pop()
        previous_state = deepcopy(history[-1])
        expenses_list.clear()
        expenses_list.extend(previous_state)
    else:
        print("Cannot undo further.")
