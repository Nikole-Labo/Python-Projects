from ui import *
from functions import *
import constants

def start_program():
    expenses_list = generate_random_expenses(constants.numbers_of_expenses)
    expenses_history_list = []
    expenses_history_list.append(deepcopy(expenses_list))
    while True:
        user_command = input(">")
        print(user_command)
        user_command = user_command.strip()
        command_words = user_command.split()
        user_command = command_words[0]

        if user_command == "list" and len(command_words) == constants.simple_list:
            list_UI(expenses_list)
        elif user_command == "exit" and len(command_words) == constants.exit_length:
            break
        elif user_command == "add" and len(command_words) == constants.add_command_length:
            read_and_add_expense_UI(expenses_list, command_words, expenses_history_list)
        elif user_command == "remove" and len(command_words) == constants.remove_command:
            remove_expenses_UI(expenses_list, command_words, expenses_history_list)
        elif user_command == "remove" and len(command_words) == constants.remove_range_command:
            remove_for_multiple_apartments_UI(expenses_list, command_words, expenses_history_list)
        elif user_command == "replace" and len(command_words) == constants.replace_expense:
            replace_expense_amount_UI(expenses_list, command_words, expenses_history_list)
        elif user_command == "list" and len(command_words) == constants.list_apartment:
            list_expenses_for_apartment(expenses_list, command_words)
        elif user_command == "list" and len(command_words) == constants.list_compared:
            list_by_total_expense_per_apartment(expenses_list, command_words)
        elif user_command == "filter" and len(command_words) == constants.filter_by_value:
            filter_expenses(expenses_list, command_words)
        elif user_command == "undo" and len(command_words) == constants.undo_command:
            undo(expenses_history_list, expenses_list)
        else:
            print("That was not a valid command :(")



start_program()
