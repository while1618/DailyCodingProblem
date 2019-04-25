# Write a function that given a list of non negative integers,
# arranges them such that they form the largest possible number.
# For example, given [50, 2, 1, 9], the largest formed number is 95021.


def largest_possible_number(list_of_numbers):
    list_of_numbers.sort(reverse=True, key=first_digit)
    return list_of_numbers


def first_digit(number):
    while number > 9:
        number /= 10
    return number


print(largest_possible_number([50, 2, 1, 9, 5, 6]))
