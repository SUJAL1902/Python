
def find_second_smallest(numbers):

    if len(numbers) < 2:
        print("The list must have at least two numbers.")
        return None

    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        print("All numbers in the list are the same.")
        return None

    unique_numbers.sort()

    return unique_numbers[1]

my_list = [4, 2, 7, 2, 5, 1]

result = find_second_smallest(my_list)

if result is not None:
    print("The second smallest number is:", result)
