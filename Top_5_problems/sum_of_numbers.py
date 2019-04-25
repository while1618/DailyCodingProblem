# Write three functions that compute the sum of the numbers in a given list using:
# for-loop, while-loop, and recursion.


def in_for_loop(list_of_numbers):
    sum_of_numbers = 0
    for i in range(0, len(list_of_numbers)):
        sum_of_numbers += list_of_numbers[i]
    return sum_of_numbers


def in_while_loop(list_of_numbers):
    sum_of_numbers = 0
    i = 0
    while i < len(list_of_numbers):
        sum_of_numbers += list_of_numbers[i]
        i += 1
    return sum_of_numbers


def recursion(list_of_numbers):
    if len(list_of_numbers) == 0:
        return 0
    else:
        return list_of_numbers[0] + recursion(list_of_numbers[1:])


print(in_for_loop([1, 2, 3, 4, 5, 6]))
print(in_while_loop([1, 2, 3, 4, 5, 6]))
print(recursion([1, 2, 3, 4, 5, 6]))
