import random
import timeit
import variables
def quicksort(array_to_be_sorted):
    def partition(lower_bound, upper_bound):
        pivot = array_to_be_sorted[upper_bound]
        index = lower_bound - 1

        for element in range(lower_bound, upper_bound):
            if array_to_be_sorted[element] <= pivot:
                index += 1
                array_to_be_sorted[index], array_to_be_sorted[element] = array_to_be_sorted[element], array_to_be_sorted[index]
        array_to_be_sorted[index + 1], array_to_be_sorted[upper_bound] = array_to_be_sorted[upper_bound], array_to_be_sorted[index + 1]
        return index + 1
    def quicksort_recursive(lower_bound, upper_bound):
        if lower_bound < upper_bound:
            partition_index = partition(lower_bound, upper_bound)
            quicksort_recursive(lower_bound, partition_index - 1)
            quicksort_recursive(partition_index + 1, upper_bound)
    quicksort_recursive(0, len(array_to_be_sorted) - 1)
    return array_to_be_sorted

def quicksort_descending(list_of_numbers):
    def partition(lower_bound, upper_bound):
        pivot = list_of_numbers[upper_bound]
        index = lower_bound - 1

        for element in range(lower_bound, upper_bound):
            if list_of_numbers[element] >= pivot:
                index += 1
                list_of_numbers[index], list_of_numbers[element] = list_of_numbers[element], list_of_numbers[index]
        list_of_numbers[index + 1], list_of_numbers[upper_bound] = list_of_numbers[upper_bound], list_of_numbers[index + 1]
        return index + 1
    def quicksort_recursive(lower_bound, upper_bound):
        if lower_bound < upper_bound:
            partition_of_the_list\
                = partition(lower_bound, upper_bound)
            quicksort_recursive(lower_bound, partition_of_the_list - 1)
            quicksort_recursive(partition_of_the_list + 1, upper_bound)
    quicksort_recursive(0, len(list_of_numbers) - 1)
    return list_of_numbers


def print_menu():
    print("________________________")
    print("1.Generate a list of random numbers (1-1000) / Command: generate list")
    print("2.Exponential search / Command: search")
    print("3.BOGOsort / Command: bogo sort")
    print("4.Stooge Sort / Command: stooge sort")
    print("5.best case / Command: best case")
    print("6.average case / Command: average case")
    print("7.worst case / Command: worst case")
    print("0.Exit program / Command: exit")
    print("________________________")


def get_input(txt="->"):
    return input(txt)


def generate_numbers(list_size):
    list_of_numbers = [random.randint(0, 1000) for _ in range(list_size)]
    return list_of_numbers


def check_sorted(list_of_numbers):
    length = len(list_of_numbers)
    for index in range(0, length - 1):
        if list_of_numbers[index] > list_of_numbers[index + 1]:
            return False
    return True


def exponential_search(list_of_numbers, searched_number):
    list_length = len(list_of_numbers)
    if list_of_numbers[0] == searched_number:
        return 1

    index = 1
    while index < list_length and list_of_numbers[index] <= searched_number:
        index *= 2

    upper_bound = min(index, list_length - 1)
    lower_bound = index // 2
    while upper_bound >= lower_bound:
        middle = lower_bound + (upper_bound - lower_bound)//2

        if list_of_numbers[middle] == searched_number:
            return middle + 1

        if list_of_numbers[middle] > searched_number:
            upper_bound = middle - 1

        else:
            lower_bound = middle + 1

    return -1
#best case: O(1) first  element to be checked
#worst case: O(log n) the searched element is not present or is the last one

def bogosort(list_of_numbers, step):
    length = len(list_of_numbers)
    steps_made = 0
    while not check_sorted(list_of_numbers):
        for index in range(0, length - 1):
            random_position = random.randint(0, length - 1)
            auxiliar = list_of_numbers[index]
            list_of_numbers[index] = list_of_numbers[random_position]
            list_of_numbers[random_position] = auxiliar
        steps_made += 1
        if(steps_made == step):
            print(list_of_numbers)
            steps_made = 0

    return list_of_numbers
#best case: O(n) list is already sorted only checking onec
#worst case: O(infinity) never generate the sorted array

def stooge_sort(list_of_numbers, step):
    swap_counter = [0]

    def sort_recursive(first, last):
        if first >= last:
            return

        if list_of_numbers[first] > list_of_numbers[last]:
            list_of_numbers[first], list_of_numbers[last] = list_of_numbers[last], list_of_numbers[first]
            swap_counter[0] += 1
            if swap_counter[0] == step:
                print(list_of_numbers)
                swap_counter[0] = 0

        if last - first + 1 > 2:
            third = (last - first + 1) // 3
            sort_recursive(first, last - third)
            sort_recursive(first + third, last)
            sort_recursive(first, last - third)

    sort_recursive(0, len(list_of_numbers) - 1)

    return list_of_numbers
# best case: O(n^2.709) even if the list is already sorted the sort still performs its recursive operations
#worst case: O(n^2.709) when the array is sorted in reverse, still does the same thing as in the best case but now the
#element positions are changed after each check

def get_elapsed_time(list_of_numbers, searched_number, algorithm):
    default_time = timeit.default_timer()
    if algorithm == 'search':
        exponential_search(list_of_numbers, searched_number)
    else:
        if algorithm == 'bogo':
            bogosort(list_of_numbers, variables.null_step)
        else:
            stooge_sort(list_of_numbers, variables.null_step)
    end_time = timeit.default_timer()
    total_time = end_time - default_time
    return total_time

def generate_5_lists(first_length, second_length, third_length, forth_length, fifth_length):
    first_list = generate_numbers(first_length)
    second_list = generate_numbers(second_length)
    third_list = generate_numbers(third_length)
    forth_list = generate_numbers(forth_length)
    fifth_length = generate_numbers(fifth_length)
    return first_list, second_list, third_list, forth_list, fifth_length
def do_best_case_for_everything():
    list_of_50_elements, list_of_100_elements, list_of_200_elements, list_of_400_elements, list_of_800_elements = generate_5_lists(variables.list_of_50, variables.list_of_100, variables.list_of_200, variables.list_of_400, variables.list_of_800)
    print("time elapsed for best case in exponential search with 50 elements is: ",
          get_elapsed_time(quicksort(list_of_50_elements), list_of_50_elements[variables.first_element], 'search'))
    print("time elapsed for best case in exponential search with 100 elements is: ",
          get_elapsed_time(quicksort(list_of_100_elements), list_of_100_elements[variables.first_element], 'search'))
    print("time elapsed for best case in exponential search with 200 elements is: ",
          get_elapsed_time(quicksort(list_of_200_elements), list_of_200_elements[variables.first_element], 'search'))
    print("time elapsed for best case in exponential search with 400 elements is: ",
          get_elapsed_time(quicksort(list_of_400_elements), list_of_400_elements[variables.first_element], 'search'))
    print("time elapsed for best case in exponential search with 800 elements is: ",
          get_elapsed_time(quicksort(list_of_800_elements), list_of_800_elements[variables.first_element], 'search'))
    print("time elapsed for best case in bogo sort with 50 elements is: ",
          get_elapsed_time(quicksort(list_of_50_elements), variables.null_number, 'bogo'))
    print("time elapsed for best case in bogo sort with 100 elements is: ",
          get_elapsed_time(quicksort(list_of_100_elements), variables.null_number, 'bogo'))
    print("time elapsed for best case in bogo sort with 200 elements is: ",
          get_elapsed_time(quicksort(list_of_200_elements), variables.null_number, 'bogo'))
    print("time elapsed for best case in bogo sort with 400 elements is: ",
          get_elapsed_time(quicksort(list_of_400_elements), variables.null_number, 'bogo'))
    print("time elapsed for best case in bogo sort with 800 elements is: ",
          get_elapsed_time(quicksort(list_of_800_elements), variables.null_number, 'bogo'))
    print("time elapsed for best case in stooge sort with 50 elements is: ",
          get_elapsed_time(quicksort(list_of_50_elements), variables.null_number, 'stooge'))
    print("time elapsed for best case in stooge sort with 100 elements is: ",
          get_elapsed_time(quicksort(list_of_100_elements), variables.null_number, 'stooge'))
    print("time elapsed for best case in stooge sort with 200 elements is: ",
          get_elapsed_time(quicksort(list_of_200_elements), variables.null_number, 'stooge'))
    print("time elapsed for best case in stooge sort with 400 elements is: ",
          get_elapsed_time(quicksort(list_of_400_elements), variables.null_number, 'stooge'))
    print("time elapsed for best case in stooge sort with 800 elements is: ",
          get_elapsed_time(quicksort(list_of_800_elements), variables.null_number, 'stooge'))

def do_worst_case_for_everything():
    list_of_50_numbers, list_of_100_numbers, list_of_200_numbers, list_of_400_numbers, list_of_800_numbers = generate_5_lists(variables.list_of_50, variables.list_of_100, variables.list_of_200, variables.list_of_400, variables.list_of_800)
    print("time elapsed for worst case in exponential search with 50 elements is: ",
          get_elapsed_time(quicksort(list_of_50_numbers), list_of_50_numbers[len(list_of_50_numbers)-1], 'search'))
    print("time elapsed for worst case in exponential search with 100 elements is: ",
          get_elapsed_time(quicksort(list_of_100_numbers), list_of_100_numbers[len(list_of_100_numbers)-1], 'search'))
    print("time elapsed for worst case in exponential search with 200 elements is: ",
          get_elapsed_time(quicksort(list_of_200_numbers), list_of_200_numbers[len(list_of_200_numbers) - 1], 'search'))
    print("time elapsed for worst case in exponential search with 400 elements is: ",
          get_elapsed_time(quicksort(list_of_400_numbers), list_of_400_numbers[len(list_of_400_numbers) - 1], 'search'))
    print("time elapsed for worst case in exponential search with 800 elements is: ",
          get_elapsed_time(quicksort(list_of_800_numbers), list_of_800_numbers[len(list_of_800_numbers) - 1], 'search'))
    list_of_2_numbers, list_of_4_numbers, list_of_6_numbers, list_of_8_numbers, list_of_10_numbers = generate_5_lists(variables.list_of_2, variables.list_of_4, variables.list_of_6, variables.list_of_8, variables.list_of_10)
    print("time elapsed for worst case in bogo sort with 2 elements is: ",
          get_elapsed_time(list_of_2_numbers, variables.null_number, 'bogo'))
    print("time elapsed for worst case in bogo sort with 4 elements is: ",
          get_elapsed_time(list_of_4_numbers, variables.null_number, 'bogo'))
    print("time elapsed for worst case in bogo sort with 6 elements is: ",
          get_elapsed_time(list_of_6_numbers, variables.null_number, 'bogo'))
    print("time elapsed for worst case in bogo sort with 8 elements is: ",
          get_elapsed_time(list_of_8_numbers, variables.null_number, 'bogo'))
    print("time elapsed for worst case in bogo sort with 10 elements is: ",
          get_elapsed_time(list_of_10_numbers, variables.null_number, 'bogo'))
    print("time elapsed for worst case in stooge sort with 50 elements is: ",
          get_elapsed_time(quicksort_descending(list_of_50_numbers), variables.null_number, 'stooge'))
    print("time elapsed for worst case in stooge sort with 100 elements is: ",
          get_elapsed_time(quicksort_descending(list_of_100_numbers), variables.null_number, 'stooge'))
    print("time elapsed for worst case in stooge sort with 200 elements is: ",
          get_elapsed_time(quicksort_descending(list_of_200_numbers), variables.null_number, 'stooge'))
    print("time elapsed for worst case in stooge sort with 400 elements is: ",
          get_elapsed_time(quicksort_descending(list_of_400_numbers), variables.null_number, 'stooge'))
    print("time elapsed for worst case in stooge sort with 800 elements is: ",
          get_elapsed_time(quicksort_descending(list_of_800_numbers), variables.null_number, 'stooge'))

def do_average_case_for_everything():
    list_of_50_elements, list_of_100_elements, list_of_200_elements, list_of_400_elements, list_of_800_elements = generate_5_lists(variables.list_of_50, variables.list_of_100, variables.list_of_200, variables.list_of_400, variables.list_of_800)
    print("time elapsed for average case in exponential search with 50 elements is: ",
          get_elapsed_time(quicksort(list_of_50_elements), list_of_50_elements[random.randint(0, len(list_of_50_elements))], 'search'))
    print("time elapsed for average case in exponential search with 100 elements is: ",
          get_elapsed_time(quicksort(list_of_100_elements), list_of_100_elements[random.randint(0, len(list_of_100_elements))], 'search'))
    print("time elapsed for average case in exponential search with 200 elements is: ",
          get_elapsed_time(quicksort(list_of_200_elements), list_of_200_elements[random.randint(0, len(list_of_200_elements))], 'search'))
    print("time elapsed for average case in exponential search with 400 elements is: ",
          get_elapsed_time(quicksort(list_of_400_elements), list_of_400_elements[random.randint(0, len(list_of_400_elements))], 'search'))
    print("time elapsed for average case in exponential search with 800 elements is: ",
          get_elapsed_time(quicksort(list_of_800_elements), list_of_800_elements[random.randint(0, len(list_of_800_elements))], 'search'))
    list_of_2_numbers, list_of_4_numbers, list_of_6_numbers, list_of_8_numbers, list_of_10_numbers = generate_5_lists(variables.list_of_2, variables.list_of_4, variables.list_of_6, variables.list_of_8, variables.list_of_10)
    print("time elapsed for average case in bogo sort with 2 elements is: ",
          get_elapsed_time(list_of_2_numbers, variables.null_number, 'bogo'))
    print("time elapsed for average case in bogo sort with 4 elements is: ",
          get_elapsed_time(list_of_4_numbers, variables.null_number, 'bogo'))
    print("time elapsed for average case in bogo sort with 6 elements is: ",
          get_elapsed_time(list_of_6_numbers, variables.null_number, 'bogo'))
    print("time elapsed for average case in bogo sort with 8 elements is: ",
          get_elapsed_time(list_of_8_numbers, variables.null_number, 'bogo'))
    print("time elapsed for average case in bogo sort with 10 elements is: ",
          get_elapsed_time(list_of_10_numbers, variables.null_number, 'bogo'))
    print("time elapsed for average case in stooge sort with 50 elements is: ",
          get_elapsed_time(list_of_50_elements, variables.null_number, 'stooge'))
    print("time elapsed for average case in stooge sort with 100 elements is: ",
          get_elapsed_time(list_of_100_elements, variables.null_number, 'stooge'))
    print("time elapsed for average case in stooge sort with 200 elements is: ",
          get_elapsed_time(list_of_200_elements, variables.null_number, 'stooge'))
    print("time elapsed for average case in stooge sort with 400 elements is: ",
          get_elapsed_time(list_of_400_elements, variables.null_number, 'stooge'))
    print("time elapsed for average case in stooge sort with 800 elements is: ",
          get_elapsed_time(list_of_800_elements, variables.null_number, 'stooge'))

def main():
    list_of_random_numbers = []
    while True:
        print_menu()
        user_option = get_input()
        if int(user_option) == variables.exit_program:

            break
        else:
            if int(user_option) == variables.generate_list:
                print("How many numbers do you want to generate?")
                list_length = int(get_input())
                list_of_random_numbers = generate_numbers(list_length)
                print(list_of_random_numbers)
            else:
                if int(user_option) == variables.exponential_search:
                    if check_sorted(list_of_random_numbers):
                        print("Give the number that you are looking for: ")
                        searched_number = int(get_input())
                        wasTheNumberFound = exponential_search(list_of_random_numbers, searched_number)
                        if wasTheNumberFound == -1:
                            print("The number is not in the list!")
                        else:
                            print("The number was found at position: ", wasTheNumberFound)
                    else:
                        print("The list must be sorted before a search!")

                else:
                    if int(user_option) == variables.bogo_sort:
                        print("Give the step:")
                        step = int(get_input())
                        print(bogosort(list_of_random_numbers, step))

                    else:
                        if int(user_option) == variables.stooge_sort:
                            print("Give the step: ")
                            step = int(get_input())
                            stooge_sort(list_of_random_numbers, step)
                            print(list_of_random_numbers)
                        else:
                            if int(user_option) == variables.best_case:
                                do_best_case_for_everything()
                            else:
                                if int(user_option) == variables.worst_case:
                                    do_worst_case_for_everything()
                                else:
                                    if int(user_option) == variables.average_case:
                                      do_average_case_for_everything()
                                    else:
                                        print("Invalid user_option!")


if __name__ == '__main__':
    main()
