
"""Given the set of positive integers S, partition this set into two subsets S1 and S2 so that the difference between
the sum of the elements in S1 and S2 is minimal. For example, for set S = { 1, 2, 3, 4, 5 }, the two subsets could be
S1 = { 1, 2, 4 } and S2 = { 3, 5 }. Display at least one of the solutions."""
import constants
from itertools import combinations

def get_input(user_input="->"):
    return input(user_input)

def print_menu():
    print("_____________________________________")
    print("1.Give the set integers")
    print("2.Divide the sets naive approach")
    print("3.Divide the set Dynamic Programing")
    print("0.Exit program")
    print("_____________________________________")


def naive_partition_set_in_2_sum_equal_subsets(set_of_numbers):
    sets_length = len(set_of_numbers)
    total_sum = sum(set_of_numbers)
    minimum_difference = float('inf')
    best_subset1 = []
    best_subset2 = []

    for number_of_elements_for_subset in range(constants.null_element, sets_length // 2):
        for subset1 in combinations(set_of_numbers, number_of_elements_for_subset):
            sum_subset1 = sum(subset1)
            sum_subset2 = total_sum - sum_subset1

            current_subsets_difference = abs(sum_subset1 - sum_subset2)

            if current_subsets_difference < minimum_difference:
                minimum_difference = current_subsets_difference
                best_subset1 = list(subset1)
                best_subset2 = [element for element in set_of_numbers if element not in subset1]

    return best_subset1, best_subset2

def dynamic_programing_partition_the_set_in_2_sum_equal_subsets(set_of_numbers):
    total_sum = sum(set_of_numbers)
    set_length = len(set_of_numbers)

    target_sum = total_sum // 2

    achievable_sums_table = [[False] * (target_sum + 1) for _ in range(set_length + 1)]
    achievable_sums_table[constants.null_element][constants.null_element] = True

    for index_in_achievable_sums_table in range(1, set_length + 1):
        current_element = set_of_numbers[index_in_achievable_sums_table - 1]
        for current_sum in range(target_sum + 1):
            achievable_sums_table[index_in_achievable_sums_table][current_sum] = achievable_sums_table[index_in_achievable_sums_table - 1][current_sum]
            if current_sum >= current_element:
                achievable_sums_table[index_in_achievable_sums_table][current_sum] = achievable_sums_table[index_in_achievable_sums_table][current_sum] or achievable_sums_table[index_in_achievable_sums_table - 1][current_sum - current_element]

    closest_sum = constants.null_element
    for sum_possible in range(target_sum, -1, -1):
        if achievable_sums_table[set_length][sum_possible]:
            closest_sum = sum_possible
            break

    first_created_subset = []
    remaining_sum = closest_sum
    for index_in_achievable_sums_table in range(set_length, constants.null_element, -1):
        if remaining_sum == constants.null_element:
            break
        if not achievable_sums_table[index_in_achievable_sums_table - 1][remaining_sum]:
            first_created_subset.append(set_of_numbers[index_in_achievable_sums_table - 1])
            remaining_sum -= set_of_numbers[index_in_achievable_sums_table - 1]

    second_created_subset = [element for element in set_of_numbers if element not in first_created_subset]

    return first_created_subset, second_created_subset

def start():
    set_of_numbers = []
    while True:
        print_menu()
        user_option = get_input()
        if int(user_option) == constants.generate_set:
            print("Give the set's integers: ")
            set_of_numbers = list(map(int, input().split()))
        else:
            if int(user_option) == constants.exit_program:
                break
            else:
                if int(user_option) == constants.DynamicPrograming:
                    subset1, subset2 = dynamic_programing_partition_the_set_in_2_sum_equal_subsets(set_of_numbers)
                    print("The resulted subsets with a minimum sum difference are: \n")
                    print("Subset 1: ", subset1)
                    print("Subset 2: ", subset2)
                else:
                    if int(user_option) == constants.naive_approach:
                        subset1, subset2 = dynamic_programing_partition_the_set_in_2_sum_equal_subsets(set_of_numbers)
                        print("The resulted subsets with a minimum sum difference are: \n")
                        print("Subset 1: ", subset1)
                        print("Subset 2: ", subset2)

start()
