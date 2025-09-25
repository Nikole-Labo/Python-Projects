"""
A number of n coins are given, with values of a1, ..., an and a value s. Display all payment modalities for the sum s.
If no payment modality exists print a message.
Backtracking : iterative and recursive alg
"""
import variables
def menu():
    print("________________________________")
    print("1.choose the list of coins ")
    print("2.Find all valid coin combinations using the recursive algorithm")
    print("3.Find all valid coin combinations using the iterative algorithm")
    print("0.Exit the program")
    print("________________________________")

def get_input(user_input="->"):
    return input(user_input)

def find_combinations_recursive(coins_list, target_sum):
    all_valid_coin_combination = []
    def backtrack_to_the_last_valid_combination(remaining_sum, current_index_for_coin, current_coin_combination):
        if remaining_sum == 0:
            all_valid_coin_combination.append(current_coin_combination[:])
            return
        if remaining_sum < 0:
            return
        for coin_index in range(current_index_for_coin, len(coins_list)):
            current_coin_combination.append(coins_list[coin_index])
            backtrack_to_the_last_valid_combination(remaining_sum - coins_list[coin_index], coin_index, current_coin_combination)
            current_coin_combination.pop()

    backtrack_to_the_last_valid_combination(target_sum, 0, [])
    if all_valid_coin_combination:
        for coin_combination in all_valid_coin_combination:
            print(coin_combination)
    else:
        print("No payment modality exists")


def find_combinations_iterative(coins_list, target_sum):
    all_valid_coin_combinations = []
    stack = [(target_sum, [], 0)]

    while stack:
        remaining_sum, current_coin_combination, current_coin_index = stack.pop()
        if remaining_sum == 0:
            all_valid_coin_combinations.append(current_coin_combination)
            continue
        else:
            if remaining_sum < 0:
                continue


        for coin_index in range(current_coin_index, len(coins_list)):
            stack.append((remaining_sum - coins_list[coin_index], current_coin_combination + [coins_list[coin_index]], coin_index))

    if all_valid_coin_combinations:
        for coin_combination in all_valid_coin_combinations:
            print(coin_combination)
    else:
        print("No payment modality exists")

def start():
    coin_list = []
    target_coin_sum = 0
    while True:
        menu()
        option = get_input()
        if int(option) == variables.choose_coins:
            print("Give the coins value: ")
            coin_list = list(map(int, input().split()))
            print("Give the target sum: ")
            target_coin_sum = int(get_input())
        else:
            if int(option) == variables.recursive:
                find_combinations_recursive(coin_list, target_coin_sum)
            else:
                if int(option) == variables.exit_program:
                    break
                else:
                    if int(option) == variables.iterative:
                        find_combinations_iterative(coin_list, target_coin_sum)

start()
